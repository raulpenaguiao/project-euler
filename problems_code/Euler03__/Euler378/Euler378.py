import time
start = time.time()
ans = 0
from ....CL.CL_Primes import PrimeFactorization, Primes
import math

lim = 6*10**6

facts = [[] for _ in range(lim+2)]
primes = Primes(math.floor(math.sqrt(lim+1)+0.1))
for i in range(2, lim+2):
    for p in primes:
        if i%p == 0:
            k = i//p
            e = 1
            while k%p == 0:
                k//= p
                e += 1
            facts[i] = [[p, e]] + facts[k]
            break
        if p*p > i:
            facts[i] = [[p, 1]]

dT = [0 for _ in range(lim+1)]
for i in range(1, lim+1):
    fac = {}
    for k, ex in facts[i]:
        fac[k] = ex
    for k, ex in facts[i+1]:
        fac[k] = ex
    fac[2] -= 1
    d = 1
    for k in fac:
        d *= fac[k] + 1
    dT[i] = d

#We are left with counting the number of 321 patterns in dT

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")