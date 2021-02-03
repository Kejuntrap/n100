#41-44を使いやすく改良したもの

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

    def show(self):
        print("表層系:", self.surface, "\t基本形:", self.base, "\t品詞:", self.pos,
              "\t品詞細分類:", self.pos1)


class Chunk:
    morphs = []  # 文節
    dst = -1  # 係り先インデックス
    srcs = []  # 係り元インデックス
    id = -1

    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []
        self.id = -1


def kakariuke(text):
    struct = Chunk()
    paragraphchunks = []  # Chunkの集合で文全体の情報を持つ
    sectionparagraphs = []  # 文章の情報を持ち、全体の情報を持つ
    isEOS = False

    for line in text[:-1]:  # ここで係り先だけを記録
        if line == "EOS":  # End Of Sequenceの時
            if not isEOS:
                paragraphchunks.append(struct)
                sectionparagraphs.append(paragraphchunks)
                readparagraph(sectionparagraphs[len(sectionparagraphs) - 1])
                paragraphchunks = []
                struct = Chunk()
                isEOS = True
        else:
            isEOS = False
            if len(line) == 0 or line[0] == '\t' or line[0] == '\r':
                continue
            elif line[0] == '*':  # Chunkの句切れ
                paragraphchunks.append(struct)
                struct = Chunk()
                struct.id = int(line.split(" ")[1])
                struct.dst = int(line.split(" ")[2][:-1])

            else:
                tmp = line.split("\t")[0]+","+line.split("\t")[1]
                struct.morphs.append(tmp)

    for i in range(len(sectionparagraphs)):  # 係り先を記録後に係り元の記録をする
        sectionparagraphs[i].pop(0)
        for j in range(len(sectionparagraphs[i])):
            if sectionparagraphs[i][j].dst != -1:
                sectionparagraphs[i][sectionparagraphs[i][j].dst].srcs.append(sectionparagraphs[i][j].dst)

    return sectionparagraphs


def TT(a):  # 連結に使っている
    source = []
    for i in range(len(a.morphs)):
        source.append(a.morphs[i])
    return source


def graph(res):
    for i in range(len(res)):
        if res[i].dst != -1:
            print(TT(res[i]), " -> ", TT(res[res[i].dst]))


f = open("john.txt.parsed", 'r', encoding='UTF-8')
text = f.read().split("\n")
res = kakariuke(text)

for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j].morphs)

graph(res[0])
