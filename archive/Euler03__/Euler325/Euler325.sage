#Coded on the 2023/11/08
#The set of losing positions are the integet points (x, y) such that x\neq y that are inside the cone x/phi < y < x*phi
#The desired sum can be extended to counting the number of integer points inside a 3 dimentional polytope
#We compute this polytope here, runs in very few time. Afterwards we need to use sage to compute the #of integer pts
#Runs in 5.084355 seconds

import time
import math
import numpy as np
start = time.time()
ans = 0
N = 10**16
MOD = 7**10
fibbs = [0, 1]
while(fibbs[-1] <= 2* N):
    fibbs += [fibbs[-1] + fibbs[-2]]
vert = []
M = N
while(M > 0):
    n = 1
    while(fibbs[2*n] <= M):
        n+=1
    #print(n, M, fibbs[2*(n-1)])
    M -= fibbs[2*(n-1)]
    #print([fibbs[2*n-1], fibbs[2*n]])
    vert.append(n-1)
vtop = [0, 0, 0]
vbot = [0, 0, 0]
vertices = [np.array([0, 0, 0]), np.array([N, N, 0]), np.array([N, N, N])]
for n in vert:
    nvectop = [fibbs[2*n-1], fibbs[2*n], fibbs[2*n-1]]
    nvecbot = [fibbs[2*n], fibbs[2*n-1], fibbs[2*n]]
    vtop = [a+b for a, b in zip(vtop, nvectop)]
    vbot = [a+b for a, b in zip(vbot, nvecbot)]
    lvtop = [vtop[0], vtop[1], 0]
    lvbot = [vbot[0], vbot[1], 0]
    vertices.append(np.array(vtop))
    vertices.append(np.array(vbot))
    vertices.append(np.array(lvtop))
    vertices.append(np.array(lvbot))
P = Polyhedron(vertices = vertices)
Q = Polyhedron(vertices = [v[:2] for v in vertices])
Pnpts = P.integral_points_count()
Qnpts = Q.integral_points_count()
ans = (Pnpts-Qnpts-N*(N+1)//2)%MOD
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")