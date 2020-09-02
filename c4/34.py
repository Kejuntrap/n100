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


def renzoku(phrases):
    renzokudic = []
    maxrenzoku = 0
    for i in range(len(phrases)):
        if phrases[i]["pos"] == "名詞":
            if maxrenzoku == 0:
                maxrenzoku += 1
                renzokudic.append(set())
                renzokudic[0].add(i)
            elif maxrenzoku > 0:
                added = False
                for j in range(len(renzokudic)):
                    if i - j - 1 in renzokudic[j]:
                        renzokudic[j].discard(i - j - 1)
                        if j + 1 == maxrenzoku:
                            renzokudic.append(set())
                            maxrenzoku += 1
                            renzokudic[j + 1].add(i - j - 1)
                        else:
                            renzokudic[j + 1].add(i - j - 1)
                        added = True

                if added == False:
                    renzokudic[0].add(i)
    return renzokudic

def outputmax(res):
    for i in res[len(res) - 1]:
        for j in range(len(res)):
            print(tmp[i + j])
        print()
    print(len(renzoku(tmp)))

tmp = func(f)
res = renzoku((tmp))
outputmax(res)



