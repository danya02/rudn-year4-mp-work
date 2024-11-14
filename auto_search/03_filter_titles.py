import collections
import json
import random

keywords = set(map(lambda x: x.lower(), open('03_banned_title_keywords.txt').read().split()))
print("Keywords:", keywords)

in_lines = 0
out_lines = 0
out_titles = []
with open('02_merged_search_results.jsonl') as i, open('03_filtered_search_results.jsonl', 'w') as o, open('03_filtered_search_titles.txt', 'w') as o2, open('03_title_frequencies.txt', 'w') as o3:
    for line in i:
        in_lines += 1
        data = json.loads(line)
        title = data['dc:title'].lower()
        skip = False
        for keyword in keywords:
            if keyword in title:
                skip = True
                break

        if skip: continue
        o.write(line)
        out_titles.append(data['dc:title'].strip())
        out_lines += 1

    random.shuffle(out_titles)
    for title in out_titles:
        o2.write(title + '\n')

    title_freq = collections.Counter()
    for title in out_titles:
        for word in title.split():
            title_freq[word.strip().lower()] += 1

    for word, count in title_freq.most_common():
        o3.write(word + '\t' + str(count) + '\n')
print("In:", in_lines)
print("Out:", out_lines)
print("Retained:", round(out_lines * 100 / in_lines, 3), '%')

