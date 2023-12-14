import time
import math

start_time = time.time()




LIM = 10 ** 8

sieve = [0 for _ in range(LIM+1)]

k = 2
while k*k <= LIM:
    if sieve[k] == 0:
        j = k*k
        while j <= LIM:
            sieve[j] = 1
            j += k
    k += 1

#for i in range(2, LIM+1):
    #print("sieve [ ", i, "] = ", sieve[i])

ans = 2
PRIME = 10 ** 9 + 7

for p in range(2, LIM+1):
    if sieve[p] == 0:
        ## find largest power of p smaller than LIM
        power = p
        while power <= LIM:
            power *= p
        power //= p
        ans *= power
        ans %= PRIME

print("ans = ", ans)
print(" --- %s seconds --- "%(time.time() - start_time))
