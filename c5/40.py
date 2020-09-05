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


f = open("ai.ja.txt.parsed", 'r', encoding='UTF-8')
t = loaddics(f)
print(t[0][0])

print(Morph(t[0][0]).base)
