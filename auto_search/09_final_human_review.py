import json
import os

def glue_all_text(struct):
    if isinstance(struct, list):
        return ' '.join(glue_all_text(x) for x in struct if x)
    elif isinstance(struct, dict):
        return ' '.join(glue_all_text(x) for x in struct.values() if x)
    else:
        if len(str(struct).split()) < 2:
            return ''
        return str(struct)

try:
    with open('09_cached_answers.json') as f:
        cached = json.load(f)
except FileNotFoundError:
    cached = {}
    with open('09_cached_answers.json', 'w') as f:
        json.dump(cached, f, indent=4)

try:
    os.unlink('09_final_search_results.jsonl')
except FileNotFoundError:
    pass

with open('08_filtered_search_results.jsonl') as i:
    for line in i:
        data = json.loads(line)
        os.system('clear')
        print(data['dc:title'])
        print(glue_all_text(data['abstract']))
        print('---')

        answer = ''
        with open('09_cached_answers.json') as f:
            cached = json.load(f)
            if cached.get(data['pii']):
                answer = cached[data['pii']]

        while answer not in ['yes', 'no', 'skip']:
            answer = input('yes/no/skip: ')
        
        if answer == 'skip':
            continue

        if answer == 'yes':
            with open('09_cached_answers.json', 'r') as f:
                cached = json.load(f)
            cached[data['pii']] = 'yes'
            with open('09_cached_answers.json', 'w') as f:
                json.dump(cached, f, indent=4)
            with open('09_final_search_results.jsonl', 'a') as o:
                o.write(line)

        if answer == 'no':
            with open('09_cached_answers.json', 'r') as f:
                cached = json.load(f)
            cached[data['pii']] = 'no'
            with open('09_cached_answers.json', 'w') as f:
                json.dump(cached, f, indent=4)