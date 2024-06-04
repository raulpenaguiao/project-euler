import time
import math

start_time = time.time()


##We are going to use the best algorithm that is present on the internet

d = 2_000_000
#d = 14
LIM = 2*d
mod = 50515093
s = [290797]*LIM
MAX = 3*mod**2

for i in range(LIM-1):
    s[i+1]=(s[i]**2)%mod
points = [[s[2*i], s[2*i+1]] for i in range(d)]
points.sort()
#n_copy = [points[0]]
#for i in range(d-1):
#    if not points[i] == points[i+1]:
#        n_copy.append(points[i+1])

#print(points)

def d_s(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


def flip(P):
    return [P[1], P[0]]


def is_close(P, m, d):
    return abs(P[0] - m) < d

def smallest_distance(a, b):
    ##Gives the smallest distance for the collection of points
    ##[points[a], ..., points[b-1]]
    if b - a < 3:
        if b - a < 2:
            return MAX
        if b - a == 2:
            return d_s(points[a], points[b-1])
    mid = (b+a)//2
    d = min(smallest_distance(a, mid), smallest_distance(mid, b))
    m = points[mid][0]
    mid_points = [flip(points[i]) for i in range(a, b) if is_close(points[i], m,d)]
    mid_points.sort()
    rg = len(mid_points)
    for i, P in enumerate(mid_points):
        for j in range(i-3, i+4):
            if j >= 0 and j < rg and not j == i:
                if P == mid_points[j]:
                    print(" P = ", P, " | i = ", i, "| j = ", j, " a = ", a, " | b = ", b)
                    print(mid_points)
                d = min(d, d_s(P, mid_points[j]))
    return d

ans = math.sqrt(smallest_distance(0, d))
print("The shortest distance in the cloud of points is d = ", ans)

print(" --- %s seconds --- "%(time.time() - start_time))
