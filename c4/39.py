import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams


rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
rcParams['font.sans-serif'] = ['Yu Gothic', 'Meirio', 'Noto Sans CJK JP']
fig = plt.figure(figsize=(12.0, 9.0))
plt.suptitle("Zipf's law")
plt.xlabel("登場順位")
plt.ylabel("登場回数")
f = open("neko.txt.mecab", 'r', encoding='UTF-8')

blacklist = set(["、", "", "。", "「", "」", "\u3000"])  # スペースが一番多いとかそういうのありえないから！


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


def derujun(maps):
    res = {}
    for t in maps:
        if t["surface"] in res and t["surface"] not in blacklist:
            res[t["surface"]] = res[t["surface"]] + 1
        elif t["surface"] not in res and t["surface"] not in blacklist:
            res[t["surface"]] = 1
    his = list(res.values())
    his = sorted(his,reverse=True)
    print(his)
    return his


def genhist(dj):
    ax = plt.gca()
    ax.set_yscale('log')
    ax.set_xscale('log')
    x = np.arange(1, len(dj) + 1 , 1)
    plt.scatter(x,dj)
    plt.show()






tmp = func(f)
res = derujun(tmp)
genhist(res)
