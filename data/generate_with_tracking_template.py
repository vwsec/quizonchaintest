#!/usr/bin/env python3
"""
Template: How to integrate doc_section_tracker.py into pool generation scripts.

This shows the pattern to use in generate_batch1.py, gen_base_batch1.py, etc.
"""

import json
from pathlib import Path
from datetime import datetime, timezone

# Import the tracker
import sys
sys.path.insert(0, str(Path(__file__).parent))
from doc_section_tracker import (
    fetch_markdown_via_jina,
    get_unused_sections,
    track_section,
    build_source_field,
    DocSection,
)


def generate_questions_for_ecosystem(ecosystem: str, doc_urls: list[str]) -> list[dict]:
    """
    Main generation loop with doc tracking.

    For each doc URL:
      1. Fetch markdown via Jina Reader
      2. Extract unused sections
      3. For each unused section, generate questions
      4. Track the section as used
    """
    all_questions = []
    question_id = 0

    for url in doc_urls:
        print(f"\n[{ecosystem}] Processing: {url}")

        try:
            markdown = fetch_markdown_via_jina(url)
        except Exception as e:
            print(f"  ERROR fetching: {e}")
            continue

        unused_sections = get_unused_sections(ecosystem, url, markdown)
        print(f"  Found {len(unused_sections)} unused sections")

        if not unused_sections:
            print(f"  All sections already used, skipping")
            continue

        for section in unused_sections:
            # ─── YOUR QUESTION GENERATION LOGIC HERE ───
            # Use section.heading, section.section, and section_content
            # to generate questions with your LLM or templates
            #
            # Example:
            # section_content = extract_section_content(markdown, section)
            # questions = generate_questions_from_content(section_content, section.heading)
            #
            # For this template, we'll just create placeholder questions:
            questions = [
                {
                    "question": f"Question about {section.heading} on {ecosystem}?",
                    "options": ["Option A", "Option B", "Option C", "Option D"],
                    "correctIndex": 0,
                }
            ]
            # ────────────────────────────────────────────

            for q in questions:
                q["id"] = question_id
                q["source"] = build_source_field(section)  # Add source tracking
                all_questions.append(q)
                question_id += 1

                # Track this section as used for THIS question
                track_section(ecosystem, section, q["id"])

            print(f"  Generated {len(questions)} questions from: {section.section}")

    return all_questions


def write_pool_json(ecosystem: str, questions: list[dict], batch_id: str) -> None:
    """Write the pool JSON file with source tracking."""
    output = {
        "meta": {
            "ecosystem": ecosystem,
            "batchId": batch_id,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "totalQuizzes": len(questions),
            "questionsPerSession": 5,
        },
        "quizzes": questions,
    }

    output_path = Path(__file__).parent / f"quizzes-{ecosystem.lower()}-{batch_id}.json"
    with output_path.open("w") as f:
        json.dump(output, f, indent=2)

    print(f"\n✅ Written {len(questions)} questions to {output_path}")


# Example usage
if __name__ == "__main__":
    # Import your docs pages (adjust import path as needed)
    # from lib.docsPages import SONEIUM_DOCS_PAGES, BASE_DOCS_PAGES, ARC_DOCS_PAGES
    # Or define inline:
    SONEIUM_DOCS_PAGES = [
        "https://docs.soneium.org/docs/builders/overview",
        "https://docs.soneium.org/docs/builders/bridging",
        # ...
    ]

    # Generate for Soneium
    questions = generate_questions_for_ecosystem("Soneium", SONEIUM_DOCS_PAGES)
    write_pool_json("Soneium", questions, f"batch-{datetime.now().strftime('%Y%m%d')}")