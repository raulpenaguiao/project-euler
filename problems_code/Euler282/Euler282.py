import time
start = time.time()
from ...CL.CL_Primes import Primes, PrimeFactorization, gcd

def ord(a, mod):
    if gcd(a, mod) > 1:
        raise Exception("NO ORDER")
    x = a%mod
    n = 1
    while(x > 1):
        x = (x*a)%mod
        n += 1
    return n

ans = 0
MOD = 7**8

print(ord(2, MOD))



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")