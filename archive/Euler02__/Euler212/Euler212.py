#Code written on the 2024/06/06
#Inclusion exclusion to compute the volume of the union
#Intersection of cubes is only tested when cubes ocupy the same section.
#We split the 10k x 10k x 10k region into 15k regions, and only test intersection of cubes that occupy the same regions
#Once all intersecting pairs of cubes are create, we generate all cliques in the resulting graph
#Inclusion exclusion corresponds to an alternating sum in these cliques
#Runs in 1.240 seconds


import time
start = time.time()
from ....CL.CL_Sets import Set
from itertools import combinations



def DeletedCopies(lst):
    if lst == []:
        return []
    lst.sort()
    ans = [lst[0]]
    l = len(lst)
    for i in range(1, l):
        if not lst[i-1] == lst[i]:
            ans.append(lst[i])
    return ans


class Clique:
    def __init__(self, *args, **kwargs):
        self.list = args[0]
        self.cube = args[1]
        self.neigs = args[2]


class Point:
    def __init__(self, *args, **kwargs):
        self.x = args[0]
        self.y = args[1]
        self.z = args[2]
    
    def lst(self):
        return [self.x, self.y, self.z]
    
    def __repr__(self):
        return "("+str(self.x) + ", " +str(self.y) + ", " +str(self.z) + ")"
    

class Cube:
    def __init__(self, *args, **kwargs):
        if kwargs["type"] == "length":
            self.low_x = args[0][0]
            self.low_y = args[0][1]
            self.low_z = args[0][2]
            self.hig_x = args[0][0] + args[1][0]
            self.hig_y = args[0][1] + args[1][1]
            self.hig_z = args[0][2] + args[1][2]
            self.width_x = args[1][0]
            self.width_y = args[1][1]
            self.width_z = args[1][2]
        if kwargs["type"] == "bounds":
            self.low_x = args[0][0]
            self.low_y = args[0][1]
            self.low_z = args[0][2]
            self.hig_x = args[1][0]
            self.hig_y = args[1][1]
            self.hig_z = args[1][2]
            self.width_x = args[1][0] - args[0][0]
            self.width_y = args[1][1] - args[0][1]
            self.width_z = args[1][2] - args[0][2]
    
    def Copy(self):
        return Cube([[self.low_x, self.low_y, self.low_z], [self.hig_x, self.hig_y, self.hig_z]], type = "bounds")
    

    def areConnected(self, other):
        if self.low_x >= other.hig_x or other.low_x >= self.hig_x:
            return False
        if self.low_y >= other.hig_y or other.low_y >= self.hig_y:
            return False
        if self.low_z >= other.hig_z or other.low_z >= self.hig_z:
            return False
        return True
    

    def volume(self):
        return self.width_x*self.width_y*self.width_z
    

    def Intersection(self, other):
        return Cube([max(self.low_x, other.low_x), max(self.low_y, other.low_y), max(self.low_z, other.low_z)], 
                    [min(self.hig_x, other.hig_x), min(self.hig_y, other.hig_y), min(self.hig_z, other.hig_z)], type = "bounds")
    
    def __repr__(self):
        return "[" + str(self.low_x) + ", " + str(self.hig_x) + "] x [" + str(self.low_y) + ", " + str(self.hig_y) + "] x [" + str(self.low_z) + ", " + str(self.hig_z) + "]"


def LargestLengths(cubeList):
    ub = Point(cubeList[0].width_x, cubeList[0].width_y, cubeList[0].width_z)
    for cube in cubeList:
        ub.x = max(ub.x, cube.width_x)
        ub.y = max(ub.y, cube.width_y)
        ub.z = max(ub.z, cube.width_z)
    return ub


def BoundingBox(cubeList):
    ub = Point(cubeList[0].hig_x, cubeList[0].hig_y, cubeList[0].hig_z)
    lb = Point(cubeList[0].low_x, cubeList[0].low_y, cubeList[0].low_z)
    for cube in cubeList:
        ub.x = max(ub.x, cube.hig_x)
        ub.y = max(ub.y, cube.hig_y)
        ub.z = max(ub.z, cube.hig_z)
        lb.x = min(lb.x, cube.low_x)
        lb.y = min(lb.y, cube.low_y)
        lb.z = min(lb.z, cube.low_z)
    return ub, lb


def CubesInBars(cubeList, cutsx, cutsy, cutsz):
    nSplits = [len(cutsx)-1, len(cutsy)-1, len(cutsz)-1]
    cubesInBarsx = [Set(elements = []) for _ in range(nSplits[0])]
    cubesInBarsy = [Set(elements = []) for _ in range(nSplits[1])]
    cubesInBarsz = [Set(elements = []) for _ in range(nSplits[2])]
    for index, cube in enumerate(cubeList):
        flag = False
        for split in range(nSplits[0]):
            if flag or cube.low_x <= cutsx[split+1]:
                flag = True
                if cube.hig_x < cutsx[split]:
                    break
                cubesInBarsx[split].append(index)
        flag = False
        for split in range(nSplits[1]):
            if flag or cube.low_y <= cutsy[split+1]:
                flag = True
                if cube.hig_y < cutsy[split]:
                    break
                cubesInBarsy[split].append(index)
        flag = False
        for split in range(nSplits[2]):
            if flag or cube.low_z <= cutsz[split+1]:
                flag = True
                if cube.hig_z < cutsz[split]:
                    break
                cubesInBarsz[split].append(index)
    return cubesInBarsx, cubesInBarsy, cubesInBarsz


def UnionCubesVolume(cubeList):
    ub, lb = BoundingBox(cubeList)
    lenLim = LargestLengths(cubeList)
    nSplits = [(ubi - lbi)//lenLimi for ubi, lbi, lenLimi in zip(ub.lst(), lb.lst(), lenLim.lst())]
    cutsx, cutsy, cutsz = [[lbi + lenLimi*i for i in range(nSplit)] + [ubi] for ubi, lbi, nSplit, lenLimi in zip(ub.lst(), lb.lst(), nSplits, lenLim.lst())]
    cubesInBarsx, cubesInBarsy, cubesInBarsz = CubesInBars(cubeList, cutsx, cutsy, cutsz)
    edges = []
    for splitx in range(nSplits[0]):
        cubesInSplitsx = cubesInBarsx[splitx]
        for splity in range(nSplits[1]):
            cubesInSplitsxy = cubesInSplitsx.Intersection(cubesInBarsy[splity])
            for splitz in range(nSplits[2]):
                cubesInSplitsxyz = cubesInSplitsxy.Intersection(cubesInBarsz[splitz])
                for index_1, index_2 in combinations(cubesInSplitsxyz.lst(), 2):
                    cube_1 = cubeList[index_1]
                    cube_2 = cubeList[index_2]
                    if cube_1.areConnected(cube_2):
                        edges.append([min(index_1, index_2), max(index_1, index_2)])

    edges = DeletedCopies(edges)

    neigs = [Set(elements = []) for _ in cubeList]
    for e in edges:
        neigs[e[0]].append(e[1])  

    ans = 0
    for cube in cubeList:
        ans += cube.volume()

    previousCliques = []
    for e in edges:
        cb = cubeList[e[0]].Intersection(cubeList[e[1]])
        nbs = neigs[e[0]].Intersection(neigs[e[1]])
        previousCliques.append(Clique(e, cb, nbs))
    
    sign = -1
    k = 2
    while previousCliques:
        currCliques = []
        for clique in previousCliques:
            ans += sign*clique.cube.volume()
            for nb in clique.neigs.lst():
                cliqueSet = clique.list[:]
                cliqueSet.append(nb)
                cube = clique.cube.Intersection(cubeList[nb])
                newneigs = clique.neigs.Intersection(neigs[nb])
                currCliques.append(Clique(cliqueSet, cube, newneigs))
        previousCliques = currCliques[:]
        k += 1
        sign *= -1
    
    return ans


MOD = 1_000_000
Mod = 10_000
mod = 399

LIM = 50_000

Seq = [0] + [(100003 - 200003*k+300007*k*k*k)%MOD for k in range(1, 55+1)]
for i in range(56, LIM*6+1):
    Seq.append((Seq[i-24]+Seq[i-55])%MOD)
Cubes = [Cube([Seq[6*i-5]%Mod, Seq[6*i-4]%Mod, Seq[6*i-3]%Mod], [1 + Seq[6*i-2]%mod, 1 + Seq[6*i-1]%mod, 1 + Seq[6*i]%mod], type = "length") for i in range(1, LIM+1)]

print("Answer = ", UnionCubesVolume(Cubes))
end = time.time()
print("Time elapsed ", end - start, " seconds")