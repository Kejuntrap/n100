import json
import re  # regexp

f = open('jawiki-country.json', 'r')
target = re.compile('\[\[Category:.+\]\]')
t2 = re.compile(':.+(\]\]|(\|\*))')

for line in f:
    jl = json.loads(line)
    if re.search(target, line):
        m = re.search(target, line)
        t = m.group().replace("|*", "")
        t = t.replace("|!", "")
        t = t.replace("\\n", "")
        t = t.replace("Category:", "")
        t = t.replace("[[", "")
        t = t.replace("]]", " ")
        print(jl["title"], t.split())
