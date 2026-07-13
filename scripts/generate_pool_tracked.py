#!/usr/bin/env python3
"""
Quiz Pool Generator with Doc Tracking — Template for Hermes Agent subagents.

Usage in your generation script:
    from scripts.doc_tracker import (
        get_unused_sections,
        track_section,
        build_source_field,
        DocSection,
    )

    # 1. Fetch doc page via Jina Reader
    markdown = fetch_via_jina(url)

    # 2. Get unused sections for this ecosystem
    unused = get_unused_sections(ecosystem, url, markdown)

    # 3. Pick a section, generate question from its content
    section = pick_section(unused)
    question = generate_question_from_section(section)

    # 4. Track the section so it won't be reused
    track_section(ecosystem, section, question_id)

    # 5. Add source to question JSON
    question["source"] = build_source_field(section)
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional
from dataclasses import dataclass, asdict

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.doc_tracker import (
    get_unused_sections,
    track_section,
    build_source_field,
    DocSection,
    load_tracked_sections,
    extract_sections_from_markdown,
)


# ──────────────────────────────────────────────
# Example: Generation workflow for one ecosystem
# ──────────────────────────────────────────────

DOCS_PAGES = {
    "arc": [
        "https://docs.arc.io/arc-chain",
        "https://docs.arc.io/arc/concepts/system-overview",
        "https://docs.arc.io/arc/references/gas-and-fees",
        "https://docs.arc.io/arc/references/connect-to-arc",
        "https://docs.arc.io/arc/tutorials/deploy-contracts",
    ],
    "base": [
        "https://docs.base.org/base-chain/quickstart/why-base",
        "https://docs.base.org/base-account/overview/what-is-base-account",
        "https://docs.base.org/base-chain/network-information/bridges",
        "https://docs.base.org/base-chain/network-information/network-faucets",
        "https://docs.base.org/get-started/block-explorers",
    ],
    # Add other ecosystems...
}


def fetch_via_jina(url: str) -> str:
    """Fetch a URL via Jina Reader and return markdown text."""
    import requests
    resp = requests.get(f"https://r.jina.ai/{url}", timeout=30)
    resp.raise_for_status()
    return resp.text


def generate_questions_for_ecosystem(ecosystem: str, target_count: int = 1000) -> list[dict]:
    """
    Main generation loop for an ecosystem.
    Returns list of question dicts with `source` field.
    """
    urls = DOCS_PAGES.get(ecosystem.lower(), [])
    if not urls:
        raise ValueError(f"No doc URLs configured for ecosystem: {ecosystem}")

    questions = []
    question_id = 0

    # Load existing pool to get current count
    pool_path = Path(__file__).parent.parent / "data" / f"quizzes-{ecosystem.lower()}.json"
    if pool_path.exists():
        with pool_path.open() as f:
            existing = json.load(f)
            question_id = len(existing.get("quizzes", []))

    print(f"[{ecosystem}] Starting at question_id={question_id}, target={target_count}")

    for url in urls:
        if question_id >= target_count:
            break

        print(f"[{ecosystem}] Fetching {url}...")
        try:
            markdown = fetch_via_jina(url)
        except Exception as e:
            print(f"  ERROR fetching {url}: {e}")
            continue

        unused_sections = get_unused_sections(ecosystem, url, markdown)
        print(f"  Found {len(unused_sections)} unused sections")

        for section in unused_sections:
            if question_id >= target_count:
                break

            # Generate question from this section's content
            # (Replace with actual LLM call or your generation logic)
            question = generate_question_from_section(section, ecosystem)

            if question:
                question["id"] = question_id
                question["source"] = build_source_field(section)

                # Track this section as used
                track_section(ecosystem, section, question_id)

                questions.append(question)
                question_id += 1

                if question_id % 50 == 0:
                    print(f"  Generated {question_id} questions...")

    return questions


def generate_question_from_section(section: DocSection, ecosystem: str) -> Optional[dict]:
    """
    Generate a single question from a doc section.
    Replace this with your actual LLM-based generation logic.
    """
    # Example: extract key facts from section content and create MCQ
    # This is a stub - you'll call your LLM here
    content = fetch_section_content(section.url, section.section)  # You'd need to implement this

    # For now, return a template
    return {
        "question": f"[GENERATED] What does the '{section.heading}' section of {ecosystem} docs cover?",
        "options": [
            "Option A (correct)",
            "Option B",
            "Option C",
            "Option D",
        ],
        "correctIndex": 0,
    }


def fetch_section_content(url: str, section_path: str) -> str:
    """Fetch just the content for a specific section. Implement based on your needs."""
    # You could re-fetch the page and extract just that section
    # Or pass the full markdown from the caller
    return ""


# ──────────────────────────────────────────────
# Pool JSON Writer
# ──────────────────────────────────────────────

def write_pool_json(ecosystem: str, questions: list[dict], batch_id: str) -> None:
    """Write the pool JSON file with metadata."""
    from datetime import datetime, timezone

    pool_data = {
        "meta": {
            "ecosystem": ecosystem.capitalize(),
            "batchId": batch_id,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "totalQuizzes": len(questions),
            "questionsPerSession": 5,
        },
        "quizzes": questions,
    }

    output_path = Path(__file__).parent.parent / "data" / f"quizzes-{ecosystem.lower()}.json"
    with output_path.open("w") as f:
        json.dump(pool_data, f, separators=(",", ":"), ensure_ascii=False)

    print(f"[{ecosystem}] Wrote {len(questions)} questions to {output_path}")


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate quiz pool with doc tracking")
    parser.add_argument("ecosystem", help="Ecosystem key (arc, base, litvm, etc.)")
    parser.add_argument("--target", type=int, default=1000, help="Target question count")
    parser.add_argument("--batch-id", default=None, help="Batch ID (default: auto)")
    args = parser.parse_args()

    batch_id = args.batch_id or f"{args.ecosystem.lower()}-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}-tracked"

    questions = generate_questions_for_ecosystem(args.ecosystem, args.target)
    write_pool_json(args.ecosystem, questions, batch_id)
    print(f"Done! Generated {len(questions)} questions for {args.ecosystem}")