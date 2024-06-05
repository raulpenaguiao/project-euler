#Code written on 2023/11/07
#Uses the fact that n+m has to be a divisor of n*(n-1)/2
#precomputes all the prime factorizations of numbers below 1234567
#Runs in 40 secs



import time
import math
start = time.time()


def Divs(dicPrimeFact):
    ans = [1]
    for p in dicPrimeFact:
        newans = []
        for a in ans:
            for e in range(dicPrimeFact[p]+1):
                newans.append(a*(p**e))
        ans = newans[:]
    return ans


def T(N):
    a = 0
    dl1 = Divs(factors[N])
    dl2 = Divs(factors[N-1])
    for d1 in dl1:
        for d2 in dl2:
            pr = d1*d2
            if pr > n:
                m = pr - n
                if (n*(m+1) + m*(m+1)//2)%pr == 0:
                    a += m
    return a

LIM = 1234567
LIMsr = math.floor(math.sqrt(LIM+1))
sieve = [True for _ in range(LIMsr+1)]
sieve[0] = False
sieve[1] = False
for i in range(4, LIMsr+1, 2):
    sieve[i] = False
for i in range(3, math.floor(math.sqrt(LIMsr+1)), 2):
    if sieve[i]:
        for j in range(i*i, LIMsr, i):
            sieve[j] = False

primes = {2:True}
nPrimes = 1
for i in range(3, LIM+1):
    j = 2
    while(j*j <= i and i%j > 0):
        j += 1
    if j*j > i:
        primes[i] = True
        nPrimes += 1

factors = [{} for _ in range(LIM+1)]

for N in range(2, LIM+1):
    for p in primes:
        if ( p*p > N):
            factors[N] = {N:1}
            break
        if N%p == 0:
            f = factors[N//p]
            fc = {k:f[k] for k in f}
            if p in fc:
                fc[p] += 1
            else:
                fc[p] = 1
            factors[N] = fc
            break
        
ans = 0
for n in range(3, LIM+1):
    a = T(n)
    ans += a

#divisors = [Divs(fac) for fac in factors]

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")