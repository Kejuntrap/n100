import json
import re  # regexp

f = open('jawiki-country.json', 'r')
target = re.compile(u'イギリス')

for line in f:
    jl = json.loads(line)
    if target.search(jl['text']):
        print(jl)
