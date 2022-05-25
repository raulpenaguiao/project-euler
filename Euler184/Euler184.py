import time
import math
start_time = time.time()

lim = 105 
limsq = lim * lim
pts = []


def gcd(a, b):
    if a == 0:
        return abs(b)
    return gcd(b%a, a)


for i in range(1, lim):
    pts += [(i, 0), (0, i)]


for i in range(1, lim):
    for j in range(1, lim):
        if i*i + j*j < limsq:
            pts += [(i, j)]
            pts += [(-i, j)]
l = len(pts)
tot = l*(l-1)*(l-2)//3

#for pt in pts:
#    print(pt[0], ", ", pt[1])
##How about colinear points? Theory is wrong!


for pt in pts:
    if gcd(pt[0], pt[1]) == 1:
        pts_on_line = pt[0]*pt[0] + pt[1] * pt[1]
        pts_on_line = math.ceil(limsq / pts_on_line) - 1
        pts_on_line = math.floor(math.sqrt(pts_on_line))
        tot -= (l-pts_on_line)*pts_on_line*(pts_on_line - 1)
        #These account for all triangles with two points on the line
        tot -= pts_on_line*(pts_on_line - 1)*(pts_on_line - 2) // 3
        #These account for all triangles with all three points on the line
print(tot)

print("--- %s seconds ----"%(time.time() - start_time))
