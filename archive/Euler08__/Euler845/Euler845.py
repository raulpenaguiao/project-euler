## Code done on 10/10/2023
## contains a function F(M, a) that counts the positive integers n < M with digit sum = a
## This code is very efficient, using the inclusion-exclusion trick for powers of 10, plus iteration over all digits
## Highly dependent on the bigInt structure of python
##Errors commited - did not use // for integer division, making numbers be skiped because they were not in the required precision
## Runs in <.5s for 10**16 > 45009328011709400
## Runs in   1s for 10**24 > 4992807761953432073250229
## Runs in   2s for 10**30 > 5590371034358585932162729926235

import time
import math
start = time.time()

def pdsBelow(n, verbose = False):
    ans = 0
    nDigs = len(digits(n))
    for i in range(9*nDigs + 10):
        if (primeQ[i]):
            t = F(n, i, verbose)
            ans += t
            if(verbose):
                print("ans updated by ", t, " on prime ", i)
    return ans


def digits(n, base = 10):
    if(n < base):
        return [n]
    return digits(n//10) + [n%10]


def F(M, a, verbose = False):
    digs = digits(M)
    if(verbose):
        print(digs)
    ans = 0
    currsum = 0
    printer = []
    l = len(digs)
    for i in range(l):
        for j in range(digs[i]):
            t = G(l - i - 1, a - currsum)
            ans += t
            if(verbose):
                printer += [[t, j]]
            currsum += 1
    if(verbose):
        print(printer)
    return ans


def G(N, k):
    if(k <= 0 or N <= 0):
        if(k ==0 and N >= 0):
            return 1
        return 0
    ans = 0
    for i in range(N+1):
        ans += sign(i) * Binom(N, i) * Binom(N+k-10*i-1, N-1)
    return ans

def Binom(a, b):
    if(a < 0 or a < b):
        return 0
    return binom[a][b]


def sign(n):
    if(n%2 == 0):
        return 1
    return -1

limbin = 1000
binom = [[1 for _ in range(i+1)] for i in range(limbin)]
for i in range(limbin):
    binom[i][0] = 1
for i in range(1, limbin):
    binom[i][i]
for i in range(2, limbin):
    for j in range(1, i):
        binom[i][j] = binom[i-1][j] + binom[i-1][j-1]

LIM = 100000
sqrtLIM = math.ceil(math.sqrt(LIM))
primeQ = [False for _ in range(LIM)]
for i in range(3, LIM, 2):
    primeQ[i] = True
primeQ[2] = True
for i in range(3, sqrtLIM, 2):
    if(primeQ[i]):
        for j in range(i*i, LIM, i):
            primeQ[j] = False

target = 10**30
lbound = target
ubound = target*2
while(pdsBelow(ubound) < target):
    ubound *= 2
while(ubound - lbound > 1):
    mbound = (ubound + lbound)//2
    #print(ubound, " - ", mbound, " - ", lbound, " ::: ", pdsBelow(mbound))
    if(pdsBelow(mbound) < target):
        lbound = mbound
    else:
        ubound = mbound
if(pdsBelow(ubound) < target):
    lbound = ubound
print("Answer = ", lbound)

end = time.time()
print("Time elapsed ", end - start, " seconds")