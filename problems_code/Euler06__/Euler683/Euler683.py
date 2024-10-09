import time
start = time.time()

import numpy as np
import math

ans = 5

def HittingTime(q, s):
    It = np.identity(s)
    Q = np.array(q)
    Nmat = np.linalg.inv(It - Q)
    t = np.array( [[sum(Nmat[i][:])] for i in range(s)] )
    tsq = np.array( [[t[i][0]**2] for i in range(s)] )
    return t, np.matmul(2*Nmat - It, t) - tsq



print(HittingTime([[.5, .5, 0], [0, .5, .5], [.5, 0, 0]], 3))

def F(N):
    q = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, N):
        for j in range(-2, 3):
            q[i][(i+j+N)%N] = (3 - abs(j))/9
    #r = [[row[0]] for row in q]
    q = [row[1:] for row in q[1:]]
    evec, varvec = HittingTime(q, N-1)
    return (sum(varvec)[0] + (N-1)*(sum(evec)[0]/(N-1))**2)/N


def G(N):
    print([F(i) for i in range(2, N+1)])
    return sum([F(i) for i in range(2, N+1)])

print("Answer = ", G(ans))
end = time.time()
print("Time elapsed ", end - start, " seconds")