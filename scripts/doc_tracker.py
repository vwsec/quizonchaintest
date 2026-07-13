#!/usr/bin/env python3
"""
Doc Section Tracker for QuizOnChain pool generation.

Tracks which doc URLs + sections/headings have been used to generate questions,
so future generation runs avoid re-using the same content.

Log format: JSON Lines (one JSON object per line) at data/doc-tracking/{ecosystem}.jsonl
Each line: {"url": "...", "section": "...", "heading": "...", "question_id": N, "generated_at": "ISO8601", "ecosystem": "..."}

Pool JSON enhancement: each question gets a `source` field:
  "source": {"url": "...", "section": "...", "heading": "...", "fetched_at": "..."}
"""

import json
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional
from dataclasses import dataclass, asdict


TRACKING_DIR = Path(__file__).parent.parent / "data" / "doc-tracking"
TRACKING_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class DocSection:
    """A documentation section identified by URL + heading path."""
    url: str
    section: str      # e.g. "## Getting Started" or "# Overview > ## Installation"
    heading: str      # the specific heading text used
    fetched_at: str   # ISO8601 timestamp

    def key(self) -> str:
        """Unique key for deduplication: url#section"""
        return f"{self.url}#{self.section}"


@dataclass
class TrackedSection:
    """A section that has been used to generate a question."""
    url: str
    section: str
    heading: str
    question_id: int
    generated_at: str
    ecosystem: str

    def to_jsonl(self) -> str:
        return json.dumps(asdict(self), separators=(",", ":"))


def get_tracking_path(ecosystem: str) -> Path:
    """Get the JSONL tracking file path for an ecosystem."""
    return TRACKING_DIR / f"{ecosystem.lower()}.jsonl"


def load_tracked_sections(ecosystem: str) -> set[str]:
    """Load all tracked section keys for an ecosystem. Returns set of 'url#section' strings."""
    path = get_tracking_path(ecosystem)
    if not path.exists():
        return set()

    keys = set()
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                keys.add(f"{data['url']}#{data['section']}")
            except json.JSONDecodeError:
                continue
    return keys


def track_section(ecosystem: str, section: DocSection, question_id: int) -> None:
    """Record that a section was used to generate a question. Appends to JSONL file."""
    entry = TrackedSection(
        url=section.url,
        section=section.section,
        heading=section.heading,
        question_id=question_id,
        generated_at=datetime.now(timezone.utc).isoformat(),
        ecosystem=ecosystem,
    )
    path = get_tracking_path(ecosystem)
    with path.open("a", encoding="utf-8") as f:
        f.write(entry.to_jsonl() + "\n")


def extract_sections_from_markdown(markdown: str, url: str) -> list[DocSection]:
    """
    Extract sections from Jina Reader markdown output.
    Jina Reader returns markdown with headings (# ## ###).
    We split by headings and return each section with its heading path.
    """
    sections = []

    # Split by headings, keeping the heading markers
    # Pattern matches # ## ### headings
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)

    matches = list(heading_pattern.finditer(markdown))
    if not matches:
        # No headings found - treat whole page as one section
        sections.append(DocSection(
            url=url,
            section="(full page)",
            heading="(full page)",
            fetched_at=datetime.now(timezone.utc).isoformat(),
        ))
        return sections

    for i, match in enumerate(matches):
        heading_level = len(match.group(1))
        heading_text = match.group(2).strip()
        start = match.start()

        # Find end of this section (next heading of same or higher level, or end of doc)
        end = len(markdown)
        for j in range(i + 1, len(matches)):
            next_level = len(matches[j].group(1))
            if next_level <= heading_level:
                end = matches[j].start()
                break

        section_content = markdown[start:end].strip()

        # Build section path (e.g., "## Overview > ### Installation")
        section_path = f"{match.group(1)} {heading_text}"

        sections.append(DocSection(
            url=url,
            section=section_path,
            heading=heading_text,
            fetched_at=datetime.now(timezone.utc).isoformat(),
        ))

    return sections


def get_unused_sections(ecosystem: str, url: str, markdown: str) -> list[DocSection]:
    """
    Given a URL and its markdown content, return sections that haven't been used yet.
    """
    tracked_keys = load_tracked_sections(ecosystem)
    all_sections = extract_sections_from_markdown(markdown, url)

    unused = []
    for section in all_sections:
        if section.key() not in tracked_keys:
            unused.append(section)

    return unused


def build_source_field(section: DocSection) -> dict:
    """Build the `source` field for a pool question JSON."""
    return {
        "url": section.url,
        "section": section.section,
        "heading": section.heading,
        "fetched_at": section.fetched_at,
    }


# ──────────────────────────────────────────────
# CLI for manual inspection
# ──────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python doc_tracker.py <ecosystem> [url]")
        sys.exit(1)

    ecosystem = sys.argv[1].lower()

    if len(sys.argv) == 2:
        # List all tracked sections for ecosystem
        keys = load_tracked_sections(ecosystem)
        print(f"Tracked sections for {ecosystem}: {len(keys)}")
        for k in sorted(keys):
            print(f"  {k}")
    else:
        # Test extraction for a URL (requires fetching)
        url = sys.argv[2]
        print(f"Fetching {url} via Jina Reader...")
        import requests
        resp = requests.get(f"https://r.jina.ai/{url}", timeout=30)
        resp.raise_for_status()
        sections = extract_sections_from_markdown(resp.text, url)
        unused = get_unused_sections(ecosystem, url, resp.text)
        print(f"Total sections: {len(sections)}, Unused: {len(unused)}")
        for s in unused[:10]:
            print(f"  UNUSED: {s.section} - {s.heading}")
        for s in sections:
            if s.key() not in [u.key() for u in unused]:
                print(f"  USED:   {s.section} - {s.heading}")