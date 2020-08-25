
f = open("neko.txt.mecab",'r',encoding='utf-8')


# MeCab HPより
# 表層\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
"""
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ
"""

def func(fls):
    result = []
    for line in fls:
        line = line.replace("\n","")
        line = line.replace('\t',',')
        line = line.split(",")
        if len(line) == 1:
            continue
        else:
            tmpdict = {
                "surface" : line[0],
                "base" : line[7],
                "pos" : line[1],
                "pos1": line[2]
            }
            result.append(tmpdict)
    return result

po = func(f)
print(po)