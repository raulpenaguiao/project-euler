import time
start = time.time()
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
                print(x, y, z)


dist = {}
for x in radii:
    for y in radii:
        dist[(x, y)] = sumDist[x+y]


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")