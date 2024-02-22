import time
start = time.time()
from ...CL.CL_Primes import MillerRabin
from ...CL.CL_Arithmetics import PowerMod

def PrimesUpTo(LIM):
    primes = [2, 3]
    l = 1
    i = 3
    while l < LIM:
        i += 2
        if MillerRabin(i):
            primes.append(i)
            l += 1
    return primes

#PRIMES = PrimesUpTo(10**7+500)
PRIMES = PrimesUpTo(10**4)
def S(k):
    return PowerMod(PRIMES[k], k, 10007)

def S2(k):
    return S(k) + S(1+k//10000)

print((S2(100) + S2(1000))/2)

print(sorted([S2(i) for i in range(11)]))


end = time.time()
print("Time elapsed ", end - start, " seconds")