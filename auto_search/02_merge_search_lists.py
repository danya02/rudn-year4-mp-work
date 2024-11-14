import os
import json

seen_article_urls = set()

with open('02_merged_search_results.jsonl', 'w') as o:
    for file in os.listdir('.'):
        if file.startswith('01_search_results'):
            for line in open(file):
                data = json.loads(line)
                link = data['link'][0]['@href']
                if link in seen_article_urls:
                    continue
                seen_article_urls.add(link)
                o.write(json.dumps(data) + '\n')