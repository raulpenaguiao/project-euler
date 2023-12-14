import time
import math

t_begin = time.time()

LIM = 1_000_000
sqLIM = math.floor(math.sqrt(LIM))
sieve = [1]*(LIM + 2)

for i in range(2, sqLIM+1):
    if sieve[i] == 1:
        k = i*i
        while k <= LIM:
            sieve[k] = 0
            k += i
primes = []
for i in range(2, LIM+1):
    if sieve[i] == 1:
        primes += [i]


f = 0
prod = 1
for p in primes:
    f += prod/(p*(p-1)*(p-1))
    prod *= (p-1)/(p)

print(f)
print("Time elapsed:", (math.floor((time.time() - t_begin)*10_000_000)/10000), "ms")
