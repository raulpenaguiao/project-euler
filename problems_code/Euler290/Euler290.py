import time
start = time.time()
from ...CL.CL_Primes import PrimeFactorization, Primes
ans = 0
LIM = 10**6

primes = Primes(1_000_000)

def digsum(k):
    if k < 10:
        return k
    return (k%10) + digsum(k//10)

#We only need to check multiples of nine
for i in range(9, LIM, 9):
    if digsum(i) == digsum(137*i):
        print(PrimeFactorization(i, primes))
        ans += 1


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")