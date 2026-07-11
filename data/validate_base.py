#!/usr/bin/env python3
"""Final validation of Base batch1 quiz file."""
import json
from collections import Counter

with open("/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch1.json") as f:
    data = json.load(f)

meta = data["meta"]
quizzes = data["quizzes"]

print(f"=== META ===")
print(f"Ecosystem: {meta['ecosystem']}")
print(f"Batch ID: {meta['batchId']}")
print(f"Generated: {meta['generatedAt']}")
print(f"Total: {meta['totalQuizzes']}")
print(f"Questions per session: {meta['questionsPerSession']}")

print(f"\n=== STRUCTURAL VALIDATION ===")
errors = []
for q in quizzes:
    if len(q["options"]) != 4:
        errors.append(f"ID {q['id']}: {len(q['options'])} options (must be 4)")
    if q["correctIndex"] not in [0, 1, 2, 3]:
        errors.append(f"ID {q['id']}: invalid correctIndex {q['correctIndex']}")
    if not q["question"].strip().endswith("?"):
        errors.append(f"ID {q['id']}: missing ?: {q['question'][:70]}")
    for i, opt in enumerate(q["options"]):
        if not isinstance(opt, str):
            errors.append(f"ID {q['id']}: option {i} not a string (type {type(opt).__name__})")

if errors:
    print(f"FAILED: {len(errors)} structural errors")
    for e in errors[:20]:
        print(f"  - {e}")
else:
    print("PASSED: All structural checks OK")

print(f"\n=== DUPLICATE CHECK ===")
seen = {}
dups = []
for q in quizzes:
    txt = q["question"].lower().strip()
    if txt in seen:
        dups.append(f"ID {q['id']} dupes ID {seen[txt]}: {q['question'][:70]}")
    seen[txt] = q["id"]
if dups:
    print(f"FAILED: {len(dups)} duplicates")
    for d in dups[:10]:
        print(f"  - {d}")
else:
    print("PASSED: No duplicates")

print(f"\n=== DISTRIBUTION ===")
dist = Counter(q["correctIndex"] for q in quizzes)
print(f"correctIndex: {dict(sorted(dist.items()))}")
print(f"Total: {sum(dist.values())}")

print(f"\n=== SAMPLE QUESTIONS ===")
import random
random.seed(123)
samples = random.sample(quizzes, 5)
for s in samples:
    print(f"\nID {s['id']} (correct={s['correctIndex']}): {s['question']}")
    for i, opt in enumerate(s['options']):
        marker = "✓" if i == s['correctIndex'] else " "
        print(f"  [{i}] {marker} {opt[:80]}")
