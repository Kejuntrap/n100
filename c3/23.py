import json
import re  # regexp

f = open('jawiki-country.json', 'r')
lv = re.compile('^=+.*=+$')

for line in f:

    edl = (json.loads(line)['text']).split('\n')
    res = {}
    for p in edl:
        if re.search(lv, p):
            content = (re.search(lv, p)).group()
            m = ((re.search(lv, p)).group()).count("=") // 2 - 1
            res[content.replace('=', '')] = m
    if len(res) > 0:
        print((json.loads(line)['title']), res)
