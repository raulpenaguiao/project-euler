# Code written on the 27/05/2024
# Recursive formula
# Runs in 150 seconds

import time
start = time.time()
ans = 0

from ...CL.CL_Primes import Primes

def digits(n, base = 10):
    if n < base:
        return[n]
    return digits(n//base, base) + [n%base]


LIM = 10**8
MOD = 1_000_000_007
primes = Primes(LIM)
print("Primes computed")
end = time.time()
print("Time elapsed ", end - start, " seconds")
F = 0
L = [0 for _ in range(10)]
N = 1



divMat = [[False for _ in range(10)] for _ in range(10)]
divList = [[] for _ in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        if i%j == 0:
            divMat[i][j] = True
            divList[i].append(j)
divNumber = [len(divList[i]) for i in range(10)]




for p in primes:
    #print(p)
    dg = digits(p)
    for d in dg:
        #print("Processing ", d)
        if d == 0:
            continue
        F *= divNumber[d]
        F %= MOD
        for e in divList[d]:
            for b in range(e+1, 10):
                F += L[b]
                F %= MOD
        for r in range(1, 10):
            L[r] *= divNumber[d]
            L[r] %= MOD
            if divMat[d][r]:
                L[r] += N
                L[r] %= MOD
        N *= divNumber[d]
        N %= MOD
        #print(N, L, F)





print("Answer = ", F)
end = time.time()
print("Time elapsed ", end - start, " seconds")