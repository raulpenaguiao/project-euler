import time
start = time.time()
ans = 0

from ...CL.CL_Primes import Primes, PrimeFactorization
from math import log

N = 5
M = 5


primes = Primes(N*2+5)[1:]
currBest = [ ]
for i in range(1, N+1):
    pf = {p:exp for p, exp in PrimeFactorization(i, primes)}
    Add(pf, 2, N)
    currBest.append([log(2)*N + log(i), pf.copy()])

maxLog = currBest[-1][0]

for p in primes:
    print(p)



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")