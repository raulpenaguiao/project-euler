#Runs in 67s
#Uses very high precision
#Done on the 10/10/2023


import time
import math
from decimal import *
start = time.time()

getcontext().prec = 40

def sum_b(N, K):
    ans = 0
    for i in range(2, N+1):
        ans += math.ceil(K - ll(i))
    return ans

def tiro(N, M):
    uBound = Decimal(N)
    lBound = Decimal(N)
    PREC = Decimal(.1**6)
    while(sum_b(N, uBound) < M):
        uBound *= 2
    while(sum_b(N, lBound) > M):
        lBound /= 2
    while(uBound - lBound > PREC):
        mPoint = (uBound + lBound)/2
        aim = sum_b(N, mPoint)
        print(lBound, " / " , mPoint, " / " , uBound, " :::: ", aim)
        if(aim < M):
            lBound = mPoint
        else:
            uBound = mPoint
    return lBound


def PowerMod(a, n, p):
    #print("a = ", a, " | n = ", n, " | p = ", p)
    if n < 2:
        if n == 1:
            return a%p
        if n == 0:
            return 1
    ans = PowerMod((a*a)%p, n//2, p)
    if(n%2 == 1):
        ans *= a
        ans %= p
    return ans

def squareNTimes(a, k, mod):
    return pow(a, pow(2, k, mod-1), mod)

"""
def squareNTimes(a, pow, mod):
    ans = a
    for i in range(pow):
        ans *= ans
        ans %= mod
    return ans"""

def ll(n):
    return Decimal(n).ln().ln()/Decimal(2).ln()

N = 10**4
M = 10**16
x = tiro(N, M)
print("x = ", x)
F = sum_b(N, x)
sum = 0
MOD = 1234567891
for i in range(2, N+1):
    expon = squareNTimes(i, math.ceil(x - ll(i)), MOD)
    sum += expon

min = Decimal(x+1)
for i in range(2, N+1):
    n = math.ceil(x - ll(i)) 
    print(i, " was exponentiated ", n, " times.")
    if(min > n + ll(i)):
        min = math.ceil(x - ll(i)) + ll(i)
        argmin = i

print("Argmin = ", argmin, " with min = ", min)
smallest_power = squareNTimes(argmin, math.ceil(x - ll(argmin)), MOD)
sum += (M - F + MOD)*((smallest_power*smallest_power)%MOD - smallest_power + MOD)

print("smallest power = ", smallest_power, " with M - F = ", M - F)

sum %= MOD

print("Answer = ", sum)
end = time.time()
print("Time elapsed ", end - start, " seconds")