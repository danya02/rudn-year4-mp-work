import collections
import json
import random

keywords = set(map(lambda x: x.lower(), open('06_banned_abstract_keywords.txt').read().splitlines()))
print("Keywords:", keywords)

in_lines = 0
out_lines = 0
out_abst = []

def glue_all_text(struct):
    if isinstance(struct, list):
        return ' '.join(glue_all_text(x) for x in struct if x)
    elif isinstance(struct, dict):
        return ' '.join(glue_all_text(x) for x in struct.values() if x)
    else:
        if len(str(struct).split()) < 2:
            return ''
        return str(struct)

with open('05_enriched_search_results.jsonl') as i, open('06_filtered_by_abstracts.jsonl', 'w') as o, open('06_filtered_abstracts.txt', 'w') as o2, open('06_abstract_frequencies.txt', 'w') as o3:
    for line in i:
        in_lines += 1
        data = json.loads(line)
        publication_date = data['load-date'].split('-')[0]
        publication_date = int(publication_date)
        # if publication_date not in [2018,2019,2020,2021,2022,2023,2024]:
        #     continue

        abstractRaw = glue_all_text(data['abstract']).replace('\n', ' ')
        # print(abstractRaw)
        abstract = abstractRaw.lower()
        skip = False
        for keyword in keywords:
            if keyword in abstract:
                skip = True
                break

        if skip: continue
        o.write(line)
        out_abst.append(abstractRaw.strip())
        out_lines += 1

    random.shuffle(out_abst)
    for abst in out_abst:
        o2.write(abst + '\n')

    title_freq = collections.Counter()
    for abst in out_abst:
        for word in abst.split():
            title_freq[word.strip().lower()] += 1

    for word, count in title_freq.most_common():
        o3.write(word + '\t' + str(count) + '\n')
print("In:", in_lines)
print("Out:", out_lines)
print("Retained:", round(out_lines * 100 / in_lines, 3), '%')

