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


def extractVsurface(molist):
    result = set()
    for t in molist:
        if t["pos"] == "動詞":
            result.add(t["surface"])
    return result


def extractVbase(molist):
    result = set()
    for t in molist:
        if t["pos"] == "動詞":
            result.add(t["base"])
    return result


tmp = func(f)
po1 = extractVsurface(tmp)
print(po1)
print("使われた表層形の種類: ", len(po1))

po2 = extractVbase(tmp)
print(po2)
print("使われた動詞の原形の種類: ", len(po2))
