import json
import re  # regexp

f = open('jawiki-country.json', 'r')
target = re.compile('\[\[File:.+\]\]')
target2 = re.compile('.+|')

for line in f:
    jl = json.loads(line)
    di = set()
    lis = line.split("\n")
    for j in lis:
        if re.search(target, j):
            m = re.search(target, j)
            t = m.group().replace("|*", "")
            t = t.replace("[[", "")
            t = t.replace("]]", "")
            t = t.replace("\\n", "")
            t = t.replace("File:", "")
            t = t.split("|")[0]
            t = t.replace("}}", "")
            t = t.replace("{{", "")
            if re.search(target2, t):
                t = re.search(target2, t)
                di.add(t.group())
    if len(di) > 0:
        print(jl["title"], di)
