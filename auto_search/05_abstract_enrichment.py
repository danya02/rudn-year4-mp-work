import time
import requests
import uncurl
import os
import json

os.system('find -empty -print -delete')
curl = input("Paste here an abstract GET request using 'copy to curl': ")
if curl:
    ctx = uncurl.parse_context(curl)

    s = requests.Session()
    s.proxies = {'http': 'socks5://localhost:6666', 'https': 'socks5://localhost:6666'}
    s.headers = ctx.headers
    try:
        del s.headers['Accept-Encoding']
    except KeyError:
        pass


def get_abstract(pii):
    try:
        with open(f'05_abstracts/{pii}.json') as o:
            return json.load(o)
    except FileNotFoundError:
        print("Fetching abstract for", pii)
        if not curl:
            print("...but curl data is unavailable, skipping")
            return None
        time.sleep(1)
        req = s.get(f'https://www.sciencedirect.com/search/api/abstract?pii={pii}')
        print(req, req.status_code, req.headers, req.text)
        if req.status_code != 200:
            print("Failed to fetch abstract for", pii)
            if req.status_code == 404:
                return None
            print(req.text)
            # skipping for now
            return None
        with open(f'05_abstracts/{pii}.json', 'w') as o:
            o.write(json.dumps(req.json()))
        return req.json()

with open('04_filtered_search_results.jsonl') as i, open('05_enriched_search_results.jsonl', 'w') as o:
    for row in i:
        data = json.loads(row)
        is_scidir = False
        for i in data['link']:
            if i['@ref'] == 'scidir':
                is_scidir = True
                break

        if not is_scidir:
            continue

        pii = data['pii']
        abstract = get_abstract(pii)

        data['abstract'] = abstract

        o.write(json.dumps(data) + '\n')