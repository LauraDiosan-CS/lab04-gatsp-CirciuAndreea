from math import sqrt

def dist(x1,y1,x2,y2):
    return round(sqrt((x1-x2)*(x1-x2)+ (y1-y2)*(y1-y2)))

def parseFile(fileName):
    net = {}
    n=51
    tpl=[]
    with open(fileName,"r") as f:
        for line in range(n):
            node,x,y=f.readline().split(" ")
            tpl.append((int(node),int(x),int(y)))

    matrix= [[0 for _ in range(n)] for _ in range(n)]
    for pct1 in tpl:
        for pct2 in tpl:
            matrix[pct1[0] -1][pct2[0] -1]=dist(pct1[1],pct2[1],pct1[2],pct2[2])
            matrix[pct1[0] -1][pct2[0] -1]=dist(pct1[1], pct2[1], pct1[2], pct2[2])

    net["mat"] = matrix
    net["noNodes"] = 51
    return net

def readNet(fileName):
    f= open(fileName, "r")
    net={}

    n= int(f.readline())
    distances=[]
    i=0
    for line in f:
        while line != "" and line != "\n" and i<n:
            stringElems= line.split(",")
            elems=[]
            for elem in stringElems:
                elems.append(int(elem))
            distances.append(elems)
            line= f.readline().strip()
            i+=1
    net["noNodes"]=n
    net["mat"]= distances

    degrees= []
    noEdges = 0
    for i in range(n):
        d=0
        for j in range(n):
            if(distances[i][j]==1):
                d+=1
            if(j> i):
                noEdges +=distances[i][j]
        degrees.append(d)
    net["noEdges"]= noEdges
    net["degrees"]= degrees
    f.close()
    return net