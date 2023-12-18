import time
start = time.time()
import math
from ...CL.CL_Primes import Primes, Divisors
LIM = 10**10
primes = Primes(math.floor(math.sqrt(LIM))+10)
mLIM = math.floor(math.sqrt(LIM/2))
for m in range(1, mLIM):
    Divisors(m*(m+1), primes)



ans = 0

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")