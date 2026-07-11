#!/usr/bin/env python3
"""Fix correctIndex distribution skew in batch1 file."""
import json

with open("/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch1.json") as f:
    data = json.load(f)

quizzes = data["quizzes"]

from collections import Counter
dist = Counter(q["correctIndex"] for q in quizzes)
print(f"Before: {dict(sorted(dist.items()))}")

# Find questions where correctIndex=0 that could reasonably be moved
# We'll change a few where the answer position 0 could be position 1, 2, or 3 by reordering options
changes = 0

# Strategy: find correctIndex=0 questions and swap their correct answer to another position
# by reordering the options array. This keeps the same correct answer text but changes its index.

index0_questions = [q for q in quizzes if q["correctIndex"] == 0]
print(f"Questions with correctIndex=0: {len(index0_questions)}")

# For about 20 of them, rotate the options so correct answer moves to index 1, 2, or 3
target_idx = 1
moved = 0
for q_item in index0_questions:
    if moved >= 20:
        break
    # Current: correct answer is at [0], other options at [1], [2], [3]
    # Move to target: place correct answer at target_idx, shift others
    current_correct = q_item["options"][0]
    others = q_item["options"][1:4]
    # Rebuild: put correct answer at target_idx
    new_options = list(q_item["options"])
    # Swap position 0 and target_idx
    new_options[0], new_options[target_idx] = new_options[target_idx], new_options[0]
    q_item["options"] = new_options
    q_item["correctIndex"] = target_idx
    moved += 1
    target_idx = (target_idx % 3) + 1  # cycle 1,2,3

print(f"Rebalanced {moved} questions")

dist = Counter(q["correctIndex"] for q in quizzes)
print(f"After: {dict(sorted(dist.items()))}")

# Save
with open("/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch1.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved!")
