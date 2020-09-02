import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
rcParams['font.sans-serif'] = ['Yu Gothic', 'Meirio', 'Noto Sans CJK JP']
fig = plt.figure(figsize=(12.0, 9.0))
plt.ylim(0, 10000)

plt.suptitle("単語の出現頻度")
plt.xlabel("単語名")
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

    dic2 = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return dic2


def gengraph(deruj, kazu):
    vol = []
    name = []
    num = int(kazu)
    for i in range(num):
        vol.append(deruj[i][1])
        name.append(deruj[i][0])
    autolabel(plt.bar(name, vol, width=0.5))
    plt.show()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')


tmp = func(f)
res = derujun(tmp)
gengraph(res, 30)
