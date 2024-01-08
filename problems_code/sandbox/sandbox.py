import time
start = time.time()
from ...CL.CL_Primes import Primes, MillerRabin

s = 10**7
SIEVE = [False for _ in range(s+1)]
PRIMES = Primes(s)
for p in PRIMES:
    SIEVE[p] = True
for i in range(s+1):
    if not SIEVE[i] == MillerRabin(i):
        print("MR = ", MillerRabin(i, True))
        print("SIEVE = ", SIEVE[i])
        print(i)


end = time.time()
print("Time elapsed ", end - start, " seconds")