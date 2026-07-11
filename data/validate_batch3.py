import json
from collections import Counter

with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch3.json') as f:
    d = json.load(f)

qs = d['quizzes']
print(f'Meta: {json.dumps(d["meta"], indent=2)}')
print()

# Structure checks
errors = []
for q in qs:
    if len(q['options']) != 4:
        errors.append(f'Q {q["id"]}: Need 4 options, got {len(q["options"])}')
    if len(set(q['options'])) != 4:
        errors.append(f'Q {q["id"]}: Duplicate options')
    if not (0 <= q['correctIndex'] <= 3):
        errors.append(f'Q {q["id"]}: Invalid correctIndex {q["correctIndex"]}')
    if not isinstance(q['id'], int):
        errors.append(f'Q has non-int id')
    if not q['question']:
        errors.append(f'Q {q["id"]}: Empty question')

if errors:
    for e in errors:
        print(f'ERROR: {e}')
else:
    print('All structure checks PASSED')

# Uniqueness
questions = [q['question'] for q in qs]
unique = len(set(questions))
print(f'Unique questions: {unique}/{len(qs)}', '(PASS)' if unique == len(qs) else 'FAIL')

# Distribution
dist = Counter(q['correctIndex'] for q in qs)
print(f'CorrectIndex distribution: {dict(sorted(dist.items()))}')

# Sequential IDs
ids = [q['id'] for q in qs]
assert ids == list(range(len(qs))), f'IDs not sequential: {ids[:5]}...{ids[-3:]}'
print('IDs are sequential from 0 (PASS)')

print(f'\nTotal: {len(qs)} questions')
