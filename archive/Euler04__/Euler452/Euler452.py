# Code written on the 2024/10/02
# Let $f(i, n)$ be the number of $n$-tuples whose product is exactly $i$, then $F(m, n) = \sum_{i \leq m} f(i, n)$
# Then $f(i, n)$ is multiplicative, and for powers of primes it is simply a binomial coefficient.
# Runs in 1092 seconds

import time
start = time.time()
import math
from ....CL.CL_Arithmetics import PowerMod
from ....CL.CL_Primes import Primes
from ....CL.CL_Primes import MillerRabin
ans = 0

power = 9
N = 10**power
M = 10**power
mod = 1234567891#I know this is a prime
print("Is ", mod, " prime? ", MillerRabin(mod))
maxExp = 5 + math.floor(math.log(M)/math.log(2))


s_div = [1]
for a in range(1, maxExp+1):
    newValue = (N - 1 + a)
    newValue %= mod
    newValue *= PowerMod(a, mod-2, mod)
    newValue %= mod
    s_div.append(newValue)
end = time.time()
print("Exponents computed up to ", maxExp, " time elapsed ", end - start, " seconds")


primes = Primes(M)
f = [1 for _ in range(M+1)]
f[0] = 0
end = time.time()
print("Memory created, time elapsed ", end - start, " seconds")

for p in primes:
    q = p
    exp = 1
    while q <= M:
        for x in range(q, M+1, q):
            f[x] *= s_div[exp]
            f[x] %= mod
        q *= p
        exp += 1

print("Answer = ", sum(f)%mod)
end = time.time()
print("Time elapsed ", end - start, " seconds")