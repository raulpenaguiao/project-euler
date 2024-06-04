#Code written on the 2023/11/03
#Generates all possible non-self intersecting paths
#We are only interested in the pairs of cells that are adjacent, so we delete paths that repeat this feature
#This takes care of rotations and reflections, as well as paths that look different but have the same connections
#For each protein and path, we compute the number of bounds, and the average of the best is the answer
#Possible optimizations: the number of bounds of a protein on a path is the
# same as the number of bounds of the reverse protein in the reverse path, this cuts time in half
#Possible optimization: stop considering a protein when it has already gotten the maximal nubmer of bonds
#Runs in 255 seconds


import time
start = time.time()
from decimal import *

N = 15

def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]

def Bonds(p, dk):
    count = 0
    for i, j in p:
        if (dk[i] == dk[j] and dk[i] == 1):
            count += 1
    return count

def generateAllPaths(N):
    if N == 1:
        return [[tuple([0, 0])]]
    ans = []
    for path in generateAllPaths(N-1):
        head = path[-1]
        nvis = tuple([head[0], head[1]+1])
        if not(nvis in path):
            ans.append( path[:]+[nvis])
        nvis = tuple([head[0], head[1]-1])
        if not(nvis in path):
            ans.append( path[:]+[nvis])
        nvis = tuple([head[0]-1, head[1]])
        if not(nvis in path):
            ans.append( path[:]+[nvis])
        nvis = tuple([head[0]+1, head[1]])
        if not(nvis in path):
            ans.append( path[:]+[nvis])
    return ans

def bondedSides(path):
    ans = []
    for i in range(len(path)):
        for j in range(i-1):
            boolFlag = False
            boolFlag = boolFlag or (( path[i][0] == path[j][0] ) and ( path[i][1] == path[j][1] + 1 ))
            boolFlag = boolFlag or (( path[i][0] == path[j][0] ) and ( path[i][1] == path[j][1] - 1 ))
            boolFlag = boolFlag or (( path[i][0] == path[j][0] + 1 ) and ( path[i][1] == path[j][1] ))
            boolFlag = boolFlag or (( path[i][0] == path[j][0] - 1 ) and ( path[i][1] == path[j][1] ))
            if(boolFlag):
                ans.append(tuple([i, j]))
    return ans


def eraseCopies(ls):
    if (ls == []):
        return []
    ls.sort()
    ans = [ls[0]]
    for i in range(len(ls)-1):
        if not(ls[i] == ls[i+1]):
            ans.append(ls[i+1])
    return ans


allPaths = [bondedSides(p) for p in generateAllPaths(N)]

allPaths = eraseCopies(allPaths)
print("number of paths = ", len(allPaths), " | number of proteins = ", 2**N)
maxBonds = [0 for _ in range(2**N)]


for k in range(2**N):
    dk = digits(k, 2)
    dk = [0]*(N-len(dk)) + dk
    for p in allPaths:
        bonds = Bonds(p, dk)
        if bonds > maxBonds[k]:
            maxBonds[k] = bonds

sm = 0
for k in range(2**N):
    dk = digits(k, 2)
    tot = 0
    for i in range(len(dk)-1):
        tot += dk[i]*dk[i+1]
    sm += tot + maxBonds[k]

getcontext().prec = 40
ans = Decimal(sm)/Decimal(2**N)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")