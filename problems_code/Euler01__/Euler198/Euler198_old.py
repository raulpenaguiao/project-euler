import time
start = time.time()
from ....CL.CL_Primes import Primes
ans = 0


def T(n):
    return n*(n+1)//2


def F(k, L):
    M = L//k
    return 100*T(M//100 - 1) + (M//100)*(M%100 + 1)

def AmbiguousNumbersApproximatedUntil(lim):
    primes = Primes(lim)
    mu = [1]*(lim+1)
    ans = 0
    for p in primes:
        for q in range(p, lim+1, p):
            mu[q] *= -1
        for q in range(p*p, lim+1, p*p):
            mu[q] = 0

    for k in range(1, lim+1):
        ans += mu[k]*F(k, lim)
    return 2*ans + 1

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")