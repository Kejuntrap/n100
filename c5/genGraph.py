from graphviz import Digraph
from graphviz import Graph



dict = []
g = Graph(format='pdf')
dg = Digraph(format='pdf')
dg.attr('node', shape='box', fontname='MS Gothic')

# graphizのdotファイルからグラフを作成
# コマンドラインからでも作れるようにしたかったけどそこまでの需要がなかった

def loadfile(name):
    f = open(name,encoding="utf-8")
    cont = f.readlines()
    for i in range(len(cont)):
        cont[i] = cont[i].strip('\n')
        cont[i] = cont[i].strip(';')
        cont[i] = cont[i].replace(" ", "")
        cont[i] = cont[i].replace("\"", "")
        cont[i] = cont[i].replace("->", ",")
        cont[i] = cont[i].replace("「", "")
        cont[i] = cont[i].replace("」", "")
        cont[i] = cont[i].replace(":","&#58;")
    f.close()
    return cont


def detectGraph(str):
    strs = str.split()
    if strs[0][0:2] == 'di':
        return "digraph"
    else:
        return "graph"


def genDic(loaddic):
    if detectGraph(loaddic[0]) == "digraph":
        dics = loaddic[1].split(',')
        for i in range(len(dics)):
            dg.node(dics[i])
        for i in range(len(loaddic) - 3):
            spr = (loaddic[i + 2].replace("->", ",")).split(",")
            dg.edge(spr[0], spr[1])
        dg.view()
    elif detectGraph(loaddic[0]) == "graph":
        dics = loaddic[1].split(',')
        for i in range(len(dics)):
            g.node(dics[i])
        for i in range(len(loaddic) - 3):
            spr = (loaddic[i + 2].replace("->", ",")).split(",")
            g.edge(spr[0], spr[1])
        g.view()


dict = loadfile("Sample.dot")
genDic(dict)
