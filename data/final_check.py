import json
from collections import Counter

# Check original file intact
with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc.json') as f:
    orig = json.load(f)
print(f'Original file intact: {len(orig["quizzes"])} questions')

# Validate new file
with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json') as f:
    batch1 = json.load(f)

qs = batch1['quizzes']
print(f'Batch1 file: {len(qs)} questions')

# Structure checks
for q in qs:
    assert len(q['options']) == 4, f'Q {q["id"]}: Must have 4 options, got {len(q["options"])}'
    assert 0 <= q['correctIndex'] <= 3, f'Q {q["id"]}: Invalid correctIndex {q["correctIndex"]}'
    assert len(set(q['options'])) == 4, f'Q {q["id"]}: Duplicate options'
    assert isinstance(q['id'], int), f'Q has non-int id'
    assert q['question'], f'Q {q["id"]}: Empty question'

# Uniqueness
questions = [q['question'] for q in qs]
assert len(set(questions)) == len(qs), 'Duplicate questions found!'
print(f'All {len(qs)} questions are unique')

# Distribution
dist = Counter(q['correctIndex'] for q in qs)
print(f'Correct answer distribution: {dict(sorted(dist.items()))}')

# Sequential IDs
ids = [q['id'] for q in qs]
assert ids == list(range(len(qs))), f'IDs not sequential: {ids[:5]}...{ids[-3:]}'
print('IDs are sequential from 0')

# Check we don't overlap with existing
existing_questions = {q['question'] for q in orig['quizzes']}
overlap = [q['question'] for q in qs if q['question'] in existing_questions]
if overlap:
    print(f'WARNING: {len(overlap)} questions overlap with original file')
else:
    print('No overlap with original file')

print('\nAll validations PASSED')
