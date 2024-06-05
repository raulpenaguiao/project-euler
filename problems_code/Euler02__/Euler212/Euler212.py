import time
start = time.time()
from ....CL.CL_Sets import Set
import math


def IsInCube(P, C):
    if not(C[0][0] <= P[0] <= C[0][0] + C[1][0]):
        return False
    if not(C[0][1] <= P[1] <= C[0][1] + C[1][1]):
        return False
    if not(C[0][2] <= P[2] <= C[0][2] + C[1][2]):
        return False
    return True


def CubeVertices(C):
    ans = []
    ans.append([C[0][0], C[0][1], C[0][2]])
    ans.append([C[0][0] + C[1][0], C[0][1], C[0][2]])
    ans.append([C[0][0], C[0][1] + C[1][1], C[0][2]])
    ans.append([C[0][0] + C[1][0], C[0][1] + C[1][1], C[0][2]])
    ans.append([C[0][0], C[0][1], C[0][2] + C[1][2]])
    ans.append([C[0][0] + C[1][0], C[0][1], C[0][2] + C[1][2]])
    ans.append([C[0][0], C[0][1] + C[1][1], C[0][2] + C[1][2]])
    ans.append([C[0][0] + C[1][0], C[0][1] + C[1][1], C[0][2] + C[1][2]])
    return ans


def AreConnected(C1, C2):
    for P in CubeVertices(C1):
        if IsInCube(P, C2):
            return True
    for P in CubeVertices(C2):
        if IsInCube(P, C1):
            return True
    return False


def DeletedCopies(lst):
    if lst == []:
        return []
    lst.sort()
    ans = [lst[0]]
    l = len(lst)
    for i in range(1, l):
        if not ans[-1] == lst[i]:
            ans.append(lst[i])
    return ans


def IntersectionCubes(C1, C2):
    x0 = max(C1[0][0], C2[0][0])
    y0 = max(C1[0][1], C2[0][1])
    z0 = max(C1[0][2], C2[0][2])
    x1 = min(C1[0][0]+C1[1][0], C2[0][0]+C2[1][0])
    y1 = min(C1[0][1]+C1[1][1], C2[0][1]+C2[1][1])
    z1 = min(C1[0][2]+C1[1][2], C2[0][2]+C2[1][2])
    if x1 < x0 or y1 < y0 or z1 < z0:
        print(C1)
        print(C2)
        print(AreConnected(C1, C2))
    return [[x0, y0, z0], [x1-x0, y1-y0, z1-z0]]


def VolumeCube(C):
    return C[1][0]*C[1][1]*C[1][2]


def TotalCubesVolume(Cubes, SideLength, BiggestCube, numCubes):
    splits = SideLength//BiggestCube
    splitbounds = [math.floor(i*SideLength/splits) + 0.5 for i in range(splits+1)]
    splitbounds[0] = -0.5
    splx = [Set(elements = []) for _ in range(splits)]
    sply = [Set(elements = []) for _ in range(splits)]
    splz = [Set(elements = []) for _ in range(splits)]

    C = [0] + Cubes #Indexing issues
    #Create the splits
    for s in range(splits):
        lb = splitbounds[s]
        ub = splitbounds[s+1]
        for i in range(1, numCubes+1):
            #Find all squares that intersect the boundaries of the split s in the dimension x
            if lb <= C[i][0][0] + C[i][1][0] and C[i][0][0] <= ub:
                splx[s].append(i)
            #Find all squares that intersect the boundaries of the split s in the dimension y
            if lb <= C[i][0][1] + C[i][1][1] and C[i][0][1] <= ub:
                sply[s].append(i)
            #Find all squares that intersect the boundaries of the split s in the dimension z
            if lb <= C[i][0][2] + C[i][1][2] and C[i][0][2] <= ub:
                splz[s].append(i)

    #Find all overlapping cubes
    edges = []
    for s1 in range(splits):
        for s2 in range(splits):
            cubesxy = splx[s1].Intersection(sply[s2])
            for s3 in range(splits):
                cubes = cubesxy.Intersection(splz[s3])
                c = cubes.lst()
                c.sort()
                lencubes = len(c)
                for i in range(lencubes):
                    for j in range(i):
                        if AreConnected(C[c[j]], C[c[i]]):
                            edges.append([c[j], c[i]])

    edges = DeletedCopies(edges)
    print("Number of edges = ", len(edges))
    neigs = [Set(elements = []) for _ in range(numCubes+1)]
    for e in edges:
        neigs[e[0]].append(e[1])
        neigs[e[1]].append(e[0])
    if numCubes < 100:
        print(neigs)
    #First order aproximation
    ans = 0
    for i in range(1, numCubes+1):
        ans += VolumeCube(C[i])
        #print(VolumeCube(C[i]))

    #We use an inclusion-exclusion correction, 2nd order
    prevcliques = []
    for e in edges:
        cb = IntersectionCubes(C[e[0]], C[e[1]])
        nbs = neigs[e[0]].Intersection(neigs[e[1]])
        prevcliques.append([e, cb, nbs])

    k = 2
    sign = -1
    while True:
        #In this loop we will be looking for k-cliques
        currcliques = []
        print(k,"-cliques to analyse = ", len(prevcliques))
        if k == 4:
            print(prevcliques)
        for p in prevcliques:
            v = VolumeCube(p[1]) 
            if v < 0:
                for i in p[0]:
                    print(C[i])
            ans += sign * VolumeCube(p[1]) 
            m = min(p[0])
            for v in p[2].bag:
                if v < m:
                    currcliques.append([p[0]+[v], IntersectionCubes(C[v], p[1]), nbs.Intersection(neigs[v])])
        if currcliques == []:
            break
        else:
            prevcliques = currcliques[:]
            k += 1
            sign *= -1
    return ans


MOD = 1_000_000
Mod = 10_000
mod = 399

LIM = 50_000
#LIM = 1579
#LIM = 100

S = [0] + [(100003 - 200003*k+300007*k*k*k)%MOD for k in range(1, 55+1)]
for i in range(56, LIM*6+1):
    S.append((S[i-24]+S[i-55])%MOD)

#C= [[[x, x, x], [2, 2, 2]] for x in range(10)]
#print(TotalCubesVolume(C, Mod, mod, 10))


C = [[[S[6*i-5]%Mod, S[6*i-4]%Mod, S[6*i-3]%Mod], [1 + S[6*i-2]%mod, 1 + S[6*i-1]%mod, 1 + S[6*i]%mod]] for i in range(1, LIM+1)]
print("Answer = ", TotalCubesVolume(C, Mod, mod, LIM))

print(C[42693])
print(C[49888])
print(C[38296])
print(C[23770])

end = time.time()
print("Time elapsed ", end - start, " seconds")