#Code written on the 2024/06/18
#It is not possible for three spheres to mutually touch, so we can simply reduce the problem to the plane
#   Fit the 21 circles in between lines 100mm apart
#   This corresponds to a minimal Hamiltonian cycle with 22 vertices (21 corresponding to the different circles and 1 corresponding to the endpoints)
#vertices: {0, 30, 31, 32, ..., 49, 50} and edges have the following distance
#dist(a, b) = 10 sqrt(2(a+b) - 100) is a, b> 0
#dist(a, 0) = a if a>0
#Distance function is concave so it is better to balls of similar size together
#Let's try smaller cases and find a pattern, we do it with 9 balls
#The pattern is the largest balls on the ends and smallest in the middle.
#Runs in 0s

import time
start = time.time()

from itertools import permutations
from math import floor, sqrt

radii = [30 + i for i in range(21)]
sumDist = {}
for s in range(60, 101):
    sumDist[s] = sqrt(2*s-100)*10

def Check2Dassumption():
    #Check if it is possible for three spheres to mutually touch
    EPS = 0.01
    for x in radii:
        for y in radii:
            l1 = sumDist[x+y]
            for z in radii:
                l2 = sumDist[y+z]
                if x+z > l1 + l2 - EPS:
                    print("It is possible for spheres with radii ", x, y, z, " to touch each other inside the cylinder.")
                    return False
    return True
#print(Check2Dassumption()) 
#> True

dist = {}
for x in radii:
    dist[(0, x)] = x
    dist[(x, 0)] = x
    for y in radii:
        dist[(x, y)] = sumDist[x+y]

def LenCycle(lst):
    ans = dist[(lst[0], lst[-1])]
    for i in range(len(lst)-1):
        ans += dist[(lst[i], lst[i+1])]
    return ans

#Find best by looping among all hamiltonian paths
#The answer arises for n = 21
def FindBestHamiltonian(n):
    verts = [0] + [i for i in range(50-n, 51)]
    bestCycle = verts[:]
    bestCycleLen = LenCycle(verts)
    for perm in permutations(verts):
        newLen = LenCycle(perm)
        if newLen < bestCycleLen:
            bestCycleLen = newLen
            bestCycle = perm
    return bestCycle

#print(FindBestHamiltonian(9))
#>(0, 49, 47, 45, 43, 41, 42, 44, 46, 48, 50)
#Runs in 43s

#With a pattern in mind, compute the distance
ans = LenCycle([0] + [i for i in range(50, 29, -2)] + [i for i in range(31, 50, 2)])
print("Answer = ", floor(1000*ans+0.5))
end = time.time()
print("Time elapsed ", end - start, " seconds")