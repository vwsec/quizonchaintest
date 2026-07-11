#!/usr/bin/env python3
"""Check and fix batch1 quiz file."""
import json

with open("/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch1.json") as f:
    data = json.load(f)

quizzes = data["quizzes"]

# Check duplicate questions
seen = {}
for q in quizzes:
    txt = q["question"].lower().strip()
    if txt in seen:
        print(f"DUPLICATE: ID {q['id']} and ID {seen[txt]}: {q['question'][:80]}")
    seen[txt] = q["id"]

# Check missing question marks
missing_q = [q for q in quizzes if not q["question"].strip().endswith("?")]
print(f"\nMissing ? marks: {len(missing_q)}")
for q in missing_q:
    print(f"  ID {q['id']}: {q['question'][:80]}")

# Check correctIndex distribution
from collections import Counter
dist = Counter(q["correctIndex"] for q in quizzes)
print(f"\nCorrectIndex dist: {dict(sorted(dist.items()))}")
print(f"Total: {len(quizzes)}")

# Find options with nested lists
for q in quizzes:
    for i, opt in enumerate(q["options"]):
        if isinstance(opt, list):
            print(f"ID {q['id']} option {i} is a list: {opt}")
            q["options"][i] = opt[0] if opt else "Option error"
