import time
import math

start_time = time.time()



m = [[0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]


def mat_prod(A, B, m, n, r, mod):
    return [ [ sum([A[i][k] * B[k][j] for k in range(n)])%mod for j in range(r)] for i in range(m)]

def Kdelta(a, b):
    if a == b:
        return 1
    return 0

def ident(k):
    return [ [ Kdelta(i, j) for i in range(k)] for i in range(k)] 

def power_mod(mat, p, mod):
    l = len(mat)
    if p <= 1:
        if p == 0:
            return ident(l)
        return mat
    new_mat = power_mod(mat_prod(mat, mat, l, l, l, mod), p//2, mod)
    if p%2 == 1:
        new_mat = mat_prod(new_mat, mat, l, l, l, mod)
    return new_mat

def paths(n):
    MOD = 10**8
    path_mat = power_mod(m, n, MOD)
    ans = path_mat[2][2] + path_mat[2][4]
    return ans%MOD

g = 12
N = 10**g

print(paths(N-1))

print(" --- %s seconds --- "%(time.time() - start_time))
