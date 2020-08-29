f = open("neko.txt.mecab", 'r', encoding='utf-8')


def func(fls):
    result = []
    for line in fls:
        line = line.replace("\n", "")
        line = line.replace('\t', ',')
        line = line.split(",")
        if len(line) == 1:
            continue
        else:
            tmpdict = {
                "surface": line[0],
                "base": line[7],
                "pos": line[1],
                "pos1": line[2]
            }
            result.append(tmpdict)
    return result


def konoyu(words):
    res = []
    ireko = []
    tmpcnt = 0

    for t in words:
        if tmpcnt == 0:
            if t["pos"] == "名詞":
                ireko = []
                ireko.append(t)
                tmpcnt += 1
            else:
                tmpcnt = 0
        elif tmpcnt == 1:
            if t["pos"] == "助詞" and t["surface"] == "の":
                ireko.append(t)
                tmpcnt += 1
            else:
                ireko = []
                tmpcnt = 0
        elif tmpcnt == 2:
            if t["pos"] == "名詞":
                ireko.append(t)
                res.append(ireko)
                ireko = []
                tmpcnt = 0
            else:
                ireko = []
                tmpcnt = 0
    return res

def chomp(worddic):
    res = []
    for t in worddic:
        res.append(t[0]["surface"]+t[1]["surface"]+t[2]["surface"])
    return res



tmp = func(f)
res = konoyu(tmp)
t = chomp(res)
print(t)
print(len(t))