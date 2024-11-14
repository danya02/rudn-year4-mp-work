import json

in_lines = 0
out_lines = 0
with open('03_filtered_search_results.jsonl') as i, open('04_filtered_search_results.jsonl', 'w') as o:
    for line in i:
        in_lines += 1
        data = json.loads(line)
        if data['openaccess']:
            o.write(line)
            out_lines += 1

print('In:', in_lines)
print('Out:', out_lines)
print('Retained:', round(100*out_lines / in_lines, 3), '%')