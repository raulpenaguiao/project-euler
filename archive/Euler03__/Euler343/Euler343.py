#Code written on the 2024/06/21
#From the factorization $k^3+1 = (k+1)(k^2-k+1)$ we only need to find prime numbers up to $\sqrt{k^2-k+1} = k$.
#Runs in 5996.64 seconds


import time
start = time.time()
ans = 0
from ....CL.CL_Primes import Primes

def f(k, primes):    
    m = k
    for p in primes:
        if m%p == 0:
            while(m%p == 0):
                m //= p
            if m == 1:
                return p
    if m > 1:
        return m


lim = 2*10**6
primes = Primes(lim+2)


ans += 1#f(1) = 1
for k in range(2, lim+1):
    ans += f(k**3+1, primes) - 1



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")