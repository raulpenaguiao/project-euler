
#It is not possible for three spheres to mutually touch, so we can simply reduce the problem to the plane
#   Fit the 21 circles in between lines 100mm apart
#   This corresponds to a minimal Hamiltonian cycle with 22 vertices (21 corresponding to the different circles and 1 corresponding to the endpoints)
#vertices: {0, 30, 31, 32, ..., 49, 50} and edges have the following distance
#dist(a, b) = 10 sqrt(2(a+b) - 100) is a, b> 0
#dist(a, 0) = a if a>0


import time
start = time.time()
from itertools import combinations
ans = 0

from math import sqrt

radii = [30 + i for i in range(21)]
sumDist = {}
for s in range(60, 101):
    sumDist[s] = sqrt(2*s-100)*10


#Check if it is possible for three spheres to mutually touch
EPS = 0.01
for x in radii:
    for y in radii:
        l1 = sumDist[x+y]
        for z in radii:
            l2 = sumDist[y+z]
            if x+z > l1 + l2 - EPS:
                print("It is possible for spheres with radii ", x, y, z, " to touch each other.")


dist = {}
for x in radii:
    for y in radii:
        dist[(x, y)] = sumDist[x+y]



f = set()
for i in range(30, 51):
    #if not( i == a or i == b or i == c):
    f.add(i)
for l in combinations(range(30, 51), 10):
    t = f.copy()
    for m in l:
        t.discard(m)
    pass

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")