import json

with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc.json') as f:
    orig = json.load(f)

with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json') as f:
    batch1 = json.load(f)

existing = {q['question'] for q in orig['quizzes']}

overlapping = []
clean_quizzes = []
for q in batch1['quizzes']:
    if q['question'] in existing:
        overlapping.append(q['question'])
        print(f"OVERLAP: id={q['id']} - {q['question']}")
    else:
        clean_quizzes.append(q)

# Re-assign IDs
for i, q in enumerate(clean_quizzes):
    q['id'] = i

batch1['quizzes'] = clean_quizzes
batch1['meta']['totalQuizzes'] = len(clean_quizzes)

with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json', 'w') as f:
    json.dump(batch1, f, indent=2)

print(f'\nRemoved {len(overlapping)} overlapping questions')
print(f'New total: {len(clean_quizzes)} questions')

from collections import Counter
dist = Counter(q['correctIndex'] for q in clean_quizzes)
print(f'Distribution: {dict(sorted(dist.items()))}')
