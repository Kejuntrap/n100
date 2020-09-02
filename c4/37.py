import MeCab





f = open("neko.txt", 'r', encoding='UTF-8')


def edits(para):        # いい感じにへんしゅうする
    para = para.strip()
    para = para.replace("「","")
    para = para.replace("」", "")
    para = para.replace("、", "")
    para = para.replace("。", "")
    para = para.replace("\u3000", "")
    return para

def makelines():
    res = []
    while True:
        line = f.readline()
        if line:
            if edits(line) != "":
                res.append(edits(line))
        else:
            break
    return res


def tangowake(paragraph,searchword):
    m = MeCab.Tagger("mecabrc")
    res1 = m.parse(paragraph).replace("\t",",").split("\n")
    res2 = set()
    for i in range(len(res1) - 2 ):
        t = res1[i].split(",")
        if t[1] == "名詞":
            res2.add(t[0])
    targetcontains = False
    if searchword in res2:
        targetcontains = True

    #print(res2)

    if targetcontains == False:
        return {}
    else:
        return res2


def kyouki1(pgs,word):
    res = []
    for i in pgs:
        t = tangowake(i,word)
        if t != {}:
            res.append(t)
    return res


def kyouki2(lists,word):
    data = {}

    for i in lists:
        for t in i:
            if t != word:
                if t not in data:
                    data[t] = 1
                else:
                    data[t] = data[t] + 1

    dic = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return dic


def kyoukihindo(word):
    return kyouki2(kyouki1(makelines(),word),word)

print(kyoukihindo("吾輩"))
