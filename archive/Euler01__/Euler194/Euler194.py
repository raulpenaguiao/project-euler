#Code written on 2023/12/05
#Recursive formula with the linear structure of the problem
#code runs in  16.19 ms

import time
start = time.time()
from ...CL.CL_Graphs import Graph
MOD = 10**8

def F(a, b, c):
    p = Graph(vertices = [0, 1, 2, 3, 4, 5, 6], edges = [[0, 1], [0, 2], [0, 5], [1, 2], [1, 6], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6]]).chromatic_polynomial().eval(c)
    p //= c*(c-1)
    p %= MOD
    q = Graph(vertices = [0, 1, 2, 3, 4, 5, 6], edges = [[0, 1], [0, 2], [0, 5], [1, 2], [1, 6], [2, 3], [3, 4], [4, 5], [4, 6]]).chromatic_polynomial().eval(c)
    q //= c*(c-1)
    q %= MOD
    tbl = [ [0 for _ in range(a+1)] for _ in range(b+1)]
    tbl[0][0] = c*(c-1)
    tbl[0][0] %= MOD
    for i in range(1, b+1):
        tbl[i][0] = q * tbl[i-1][0]
        tbl[i][0] %= MOD
    for j in range(1, a+1):
        tbl[0][j] = p * tbl[0][j-1]
        tbl[0][j] %= MOD
    for i in range(1, b+1):
        for j in range(1, a+1):
            tbl[i][j] = tbl[i][j-1]*p + tbl[i-1][j]*q
            tbl[i][j] %= MOD
    return tbl[b][a]


print("Answer = ", F(25, 75, 1984))
end = time.time()
print("Time elapsed ", end - start, " seconds")