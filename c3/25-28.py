import json
import re  # regexp

f = open('jawiki-country.json', 'r')
target = re.compile(u'基礎情報.+==[ ]国名[ ]==')

for line in f:
    jl = json.loads(line)
    tmp = jl['text'].replace("\n", "←")
    countrydata = {}
    if re.search(target, tmp):
        m = ((re.search(target, tmp)).group()[2:])
        m = m.replace("'", "")
        m = m.replace("{{", "")
        m = m.replace("}}", "")
        m = m.replace("[[", "")
        m = m.replace("]]", "")
        m = m.replace("ファイル:", "")
        m = m.replace("File:", "")
        m = re.sub('\|[0-9]+px\|.+', '', m)
        m = re.sub('[Ll]ang\|[A-Z a-z]{2}\|', '', m)
        m = re.sub('[A-Z a-z]{2}\|', '', m)
        m = re.sub('<.+>', '', m)
        mlist = m.split("←")
        for i in range(len(mlist)):
            tmpl = mlist[i].split("=")
            if len(tmpl) >= 2:
                if tmpl[0].replace("|", "").replace(" ", "") != "":
                    countrydata[tmpl[0].replace("|", "").replace(" ", "")] = tmpl[1]
        print(jl["title"], " : ", countrydata)
