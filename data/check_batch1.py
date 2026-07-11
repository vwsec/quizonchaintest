import json
from collections import Counter

with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json') as f:
    d = json.load(f)

questions = [q['question'] for q in d['quizzes']]
print(f'Valid JSON: {len(d["quizzes"])} questions')
print(f'Unique questions: {len(set(questions))}')

dist = Counter(q['correctIndex'] for q in d['quizzes'])
print(f'Distribution: {dict(sorted(dist.items()))}')

for q in d['quizzes']:
    if len(set(q['options'])) != 4:
        print(f'DUPLICATE OPTIONS in question {q["id"]}: {q["question"]}')
        
print('All checks passed' if len(set(questions)) == len(d['quizzes']) else 'Has duplicates')
