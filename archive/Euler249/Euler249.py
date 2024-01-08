#Code written in 2024/01/08
# generates a list sprimes, such that sprimes[i] = number of subsets with sum i
# this generation is fast because we only record the number of such sums, which allows this to have size |sprimes|*maxsum ~ 1000 * 1M
# We add all the values of this list for prime indices
#Code runs in 48.72416 seconds


import time
start = time.time()
from ...CL.CL_Primes import Primes, MillerRabin
primes = Primes(5000)

def SumList(lst, sz):
    totSum = [0 for _ in range(sz+1)]
    totSum[0] = 1
    for l in lst:
        for i in range(sz, l-1, -1):
            totSum[i] += totSum[i-l]
    return totSum

s = sum(primes)
SIEVE = [False for _ in range(s+1)]
PRIMES = Primes(s)
for p in PRIMES:
    SIEVE[p] = True
sprimes = SumList(primes, s)
ans = 0
for index, nprs in enumerate(sprimes):
    if SIEVE[index]:
        ans += nprs
        

print("Answer = ", ans%(10**16))
end = time.time()
print("Time elapsed ", end - start, " seconds")