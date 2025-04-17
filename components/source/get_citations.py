import sys
import re

text = ""
with open(sys.argv[1], "r") as f:
    text = f.read()

cite_regex = r"@\w+"

citations = re.findall(cite_regex, text)

for c in citations:
    print(c)