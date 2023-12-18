## Code completed on the 18th Oct 2023
## One uses two auxiliary functions that compute data recursively
# m function counts {0 < n < 10**M | s(n) = k}
# g function counts sum(0 < n < 10**M)


import time
from decimal import *
start = time.time()


pow10 = [10**i for i in range(50)]


def sign(n):
    if(n%2 == 0):
        return 1
    return -1


def Binom(a, b):
    if(a < 0 or a < b):
        return 0
    return binom[a][b]



def digits(n, base = 10):
    if(n < base):
        return [n]
    return digits(n//10) + [n%10]


def toNumber(lis, base = 10):
    if(len(lis) == 0):
        return 0
    return toNumber(lis[:-1], base)*base + lis[-1]


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


def Maux(N, k):
    if(k <= 0 or N <= 0):
        if(k == 0 and N >= 0):
            return 1
        return 0
    ans = 0
    for i in range(N+1):
        ans += sign(i) * Binom(N, i) * Binom(N+k-10*i-1, N-1)
    return ans


def M(N, k):
    if ( k <= 0 or N <= 0):
        if k == 0:
            return 1
        return 0
    return m[N][k]


def G(N, k):
    if(N < 0 or k <= 0):
        return 0
    return g[N][k]

def D(N, k):
    ans = 0
    currsum = k
    digs = digits(N)
    digs.reverse()
    l = len(digs)
    a = 0
    t = 0
    #print("Computing for N = ", N, " and k = ", k)
    #print(" l = ", l, " - ", digs)
    while(l > 0):
        if(digs[l-1] == a):
            l -= 1
            #print(" l = ", l)
            a = 0
        else:
            #print(l-1, " / ", currsum)
            gCont = G(l-1, currsum)
            mCont = M(l-1, currsum)
            #print("Number of numbers in the interval = ", mCont)
            #print("Sum of numbers in the interval = ", gCont)
            newSum = gCont + mCont*t
            ans += newSum
            #print(newSum,  " - ", l, " - ", a, " - ", currsum)
            #print(ans, " sum of such numbers between ", t, " and ", t + pow10[l-1])
            t += pow10[l-1]
            a += 1
            currsum -= 1
    return ans

limbin = 1000
binom = [[1 for _ in range(i+1)] for i in range(limbin)]
for i in range(limbin):
    binom[i][0] = 1
for i in range(1, limbin):
    binom[i][i]
for i in range(2, limbin):
    for j in range(1, i):
        binom[i][j] = binom[i-1][j] + binom[i-1][j-1]

m = [[Maux(N, k) for k in range(450)] for N in range(50)]
g = [[0 for _ in range(455)] for _ in range(50)]

m[0][0] = 1
for N in range(1, 50):
    for k in range(450):
        for i in range(min(10, k+1)):
            g[N][k] += g[N-1][k-i] + pow10[N-1]*i*M(N-1, k-i)

n = 10# -> 19
n = 123# -> 1.1877646 * 10e3
n = 12345# -> 4.855801996238 * 10e6
n = 1234567890123456789# -> answer



n+=1 
nDigs = len(digits(n))
ans = Decimal(0)
#print(" n = ", n)
for i in range(1, 9*nDigs+1):
    d = D(n, i)
    #print("sum of numbers below ", n, " with digit sum == ", i, " -- > ", d)
    ans += Decimal(d)/Decimal(i)


print("Answer = ", ans)

end = time.time()
print("Time elapsed ", end - start, " seconds")