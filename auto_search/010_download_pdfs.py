import json
import os

for row in open('09_final_search_results.jsonl'):
    data = json.loads(row)
    pii = data['pii']
    exists = any([pii in x for x in os.listdir('pdfs')])
    while not exists:
        print(f'Download: https://www.sciencedirect.com/science/article/pii/{pii}/pdf')
        input('next...')
        exists = any([pii in x for x in os.listdir('pdfs')])
