import json
import time
import requests
import requests.auth
from getpass import getpass

from urllib.parse import quote

APIKEY = open('APIKEY').read().strip()

s = requests.Session()
# username = '1032212280@pfur.ru'
# password = getpass()
# proxy_url = f'http://{quote(username)}:{quote(password)}@37.18.79.68:3128/'
# print(proxy_url)

# launch proxy with ssh -D 6666 cepheus.zt.roboticlab.ru
proxy_url = 'socks5://127.0.0.1:6666'
s.proxies = {'http': proxy_url, 'https': proxy_url}
s.headers = {'Accept': 'application/json', 'X-ELS-APIKey': APIKEY}

# import pprint
# pprint.pprint(s.get('http://api.elsevier.com/content/abstract/pii/S187705091931988X?view=META').json())
# exit()

def search_elsevier_sciencedirect(query):
    with open(f'01_search_results_scidir_{query}.jsonl', 'w') as o:
        url = 'https://api.elsevier.com/content/search/sciencedirect'
        params = {
            'query': query,
            'count': 100,
            'view': 'COMPLETE'
        }
        print("Getting initial data")
        response = s.get(url, params=params)
        response.raise_for_status()
        print(response.json())
        print(response.headers)
        data = response.json()['search-results']

        for item in data['entry']:
            o.write(json.dumps(item) + '\n')

        next_link = None
        for link in data['link']:
            if link['@ref'] == 'next':
                next_link = link['@href']
                break

        while next_link:
            time.sleep(1)
            print("Getting next data:", next_link)
            response = s.get(next_link)
            print(response.headers)
            response.raise_for_status()

            data = response.json()['search-results']
            print('Current position:', [(i, data[i]) for i in data if i.startswith('opensearch')])

            print('Got', len(data['entry']), 'items')
            for item in data['entry']:
                o.write(json.dumps(item) + '\n')

            next_link = None
            for link in data['link']:
                if link['@ref'] == 'next':
                    next_link = link['@href']
                    break

search_elsevier_sciencedirect(input('Query: '))