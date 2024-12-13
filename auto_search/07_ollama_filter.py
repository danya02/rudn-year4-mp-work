import json
import os
import requests
import hashlib

s = requests.Session()
#s.proxies = {'http': 'socks5://localhost:6666', 'https': 'socks5://localhost:6666'}

def glue_all_text(struct):
    if isinstance(struct, list):
        return ' '.join(glue_all_text(x) for x in struct if x)
    elif isinstance(struct, dict):
        return ' '.join(glue_all_text(x) for x in struct.values() if x)
    else:
        if len(str(struct).split()) < 2:
            return ''
        return str(struct)

def ask_abstract(abstract, seed):
    print("Asking with seed", seed)
    print(abstract)
    system_prompt = '''
In this scoping review, the Population is Wireless Mesh Networks, especially ad-hoc and IoT.
Other kinds of networks, such as those using mobile phones, are excluded.
The Context is IoT, autonomous robots and similar industrial applications.
Emergency response networks, military operations, or urban infrastructure are excluded.
The Concept is Routing protocols, dealing with changing and unknown network topology, fault tolerance.
Techniques for improving throughput, such as multipath routing are excluded.
Please review the following abstract to determine if it is relevant to the scoping review.
First provide your reasoning, then say "In conclusion, the answer is [yes/no]".
'''.split()
    system_prompt = ' '.join(system_prompt)

    response = s.post(
        # 'http://10.69.69.69:11434/api/chat',
        'http://localhost:11434/api/chat',
        json={
            'model': 'llama3.2',
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': abstract}
            ],
            'stream': False,
            'options': {'seed': seed}
        })
    response.raise_for_status()
    print(response.text)
    return response


def lfsr(seed, mask):
    result = seed
    nbits = mask.bit_length()-1
    while True:
        result = (result << 1)
        xor = result >> nbits
        if xor != 0:
            result ^= mask
        yield result

os.makedirs('ollama-state', exist_ok=True)


try: os.unlink('07_filtered_by_llm.jsonl')
except FileNotFoundError: pass

for item in open('06_filtered_by_abstracts.jsonl'):
    data = json.loads(item)
    if 'abstract' not in data: continue
    abstract = glue_all_text(data['abstract'])

    try:
        with open(f'ollama-state/{data["pii"]}.json') as f:
            state = json.loads(f.read())
    except FileNotFoundError:
        state = {'votes': [], 'verdict': None}

    pii_hash = hashlib.sha256(data['pii'].encode()).hexdigest()
    pii_hash = int(pii_hash, 16)
    mask = 0xffff
    pii_hash = pii_hash & mask
    rng = lfsr(pii_hash, mask)
    for vote in range(3):
        seed = next(rng)
        asked = False

        try:
            new_vote = state['votes'][vote]
        except IndexError:
            response = ask_abstract(abstract, seed)
            new_vote = response.json()
            asked = True
            
        msg = new_vote['message']['content']
        msg = ' '.join(msg.split())
        msg = list(msg)
        import string
        msg = [i for i in msg if i in string.ascii_letters + ' ']
        msg = ''.join(msg).lower()
        print("MSG", msg)
        if 'the answer is yes' in msg:
            new_vote['verdict'] = True
        elif 'the answer is no' in msg:
            new_vote['verdict'] = False
        else:
            new_vote['verdict'] = None
        if asked:
            state['votes'].append(new_vote)

        # The verdict is the majority of the votes
        verdict_score = 0
        for vote in state['votes']:
            if vote['verdict'] == True:
                verdict_score += 1
            if vote['verdict'] == False:
                verdict_score -= 1

        if verdict_score > 0:
            state['verdict'] = True
        elif verdict_score < 0:
            state['verdict'] = False
        else:
            state['verdict'] = None

        with open(f'ollama-state/{data["pii"]}.json', 'w') as f:
            f.write(json.dumps(state))

    print(state)
    if state['verdict'] == True:
        with open('07_filtered_by_llm.jsonl', 'a+') as o:
            o.write(json.dumps(data) + '\n')
