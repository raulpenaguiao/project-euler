#Code written on the 2023/12/18
#Observe that there is a bijection between squares and finite strings of two characters "U" and "R"
#This bijection behaves very well with the index: the tindex of a string is the pair of occurrences of "U" and "R"
#We generate all the strings with 3 "R" and 3 "U", compute the side length of each of the corresponding squares
#The smallest such square serves as a limit to stop the search
#For the search, we use a priority queue to only expore a square when no larger square exists
#Priority queue, computational geometry, quadratic formula
#Runs in 4.39 s


import time
start = time.time()
from math import sqrt
from queue import PriorityQueue
from decimal import Decimal, getcontext   
getcontext().prec = 40

ans = 0

def U(sqr):
    x1 = sqr[0][0]
    y2 = sqr[1][1]
    x1p = x1
    y1p = y2
    alpha = x1p-y1p
    x2p = (alpha + Decimal(sqrt(alpha*alpha + Decimal(4))))/Decimal(2)
    y2p = x2p - alpha
    return [[x1p, y1p], [x2p, y2p]]

def R(sqr):
    y1 = sqr[0][1]
    x2 = sqr[1][0]
    x1p = x2
    y1p = y1
    alpha = x1p-y1p
    x2p = (alpha + Decimal(sqrt(alpha*alpha + Decimal(4))))/Decimal(2)
    y2p = x2p - alpha
    return [[x1p, y1p], [x2p, y2p]]

FIRSTSQUARE = R([[Decimal(0), Decimal(0)], [Decimal(1), Decimal(1)]])

def StrToPoint(st):
    sqr = FIRSTSQUARE
    for ch in st:
        if ch == "U":
            sqr = U(sqr)
        if ch == "R":
            sqr = R(sqr)
    return sqr

def SideLength(sqr):
    return (sqr[1][0]-sqr[0][0])


def GeneratePaths(a, b):
    if a == 0:
        ans = ""
        for _ in range(b):
            ans += "R"
        return [ans]
    if b == 0:
        ans = ""
        for _ in range(a):
            ans += "U"
        return [ans]
    ansList = []
    for p in GeneratePaths(a-1, b):
        ansList.append("U"+p)
    for p in GeneratePaths(a, b-1):
        ansList.append("R"+p)
    return ansList

WithIndex = [[SideLength(StrToPoint(st)), st] for st in GeneratePaths(3, 3)]
WithIndex.sort()
smallestSideLenth = WithIndex[0][0]

q = PriorityQueue()
q.put([SideLength(FIRSTSQUARE), FIRSTSQUARE])
count = 0
while(not q.empty()):
    sqWL = q.get()
    sl = sqWL[0]
    sq = sqWL[1]
    count += 1
    sqU = U(sq)
    slU = SideLength(sqU)
    if slU >= smallestSideLenth:
        q.put([slU, sqU])
    sqR = R(sq)
    slR = SideLength(sqR)
    if slR >= smallestSideLenth:
        q.put([slR, sqR])




print("Answer = ", count)
end = time.time()
print("Time elapsed ", end - start, " seconds")