class Morph:
    surface = ""
    base = ""
    pos = ""
    pos1 = ""

    def __init__(self, r):
        self.surface = r[0]
        self.base = r[7]
        self.pos = r[1]
        self.pos1 = r[2]


def loaddics(fl):
    res = []
    tmpres = []
    while True:
        line = fl.readline().replace("\t", ",").replace("\n", "")
        if line:
            if not (line[0] == "*" or line == "EOS"):
                tmpres.append(line.split(","))
            elif line == "EOS":
                if len(tmpres) > 0:
                    res.append(tmpres)
                tmpres = []
        else:
            break
            print(res)
    return res


def output(dic):
    for i in range(len(dic)):
        print("size:",len(dic[i]))
        for j in range(len(dic[i])):
            print("表層系:", Morph(dic[i][j]).surface, "\t基本形:", Morph(dic[i][j]).base, "\t品詞:", Morph(dic[i][j]).pos,
                  "\t品詞細分類:", Morph(dic[i][j]).pos1)
        print()


f = open("ai.ja.txt.parsed", 'r', encoding='UTF-8')
t = loaddics(f)
output(t)
print(t[0][0])

print(Morph(t[0][0]).base)
