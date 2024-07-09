pol1 = { "A" : (3,3), "B" : (2,7), "C" : (4,9), "D" : (0,4),  "E" : (2,3)}
def PlotDot(pol1):
    for x in pol1:
        for i in range(pol1 [x] [0]):
            print(" , " , end ="")
        print("* " + x)

def PlotDotUp(pol):
        ls = sorted(pol, key = lambda x: pol [x] [1], reverse = True)
        print(ls)
        for x in ls:
            print(" " * pol[x][0], end = "")
            print ("*" + x)
def maxEdge(pol):
        max = 0
        ls = list(pol)
        L = len(pol)
        for i in range(L):
            d2 = (pol [ls {
