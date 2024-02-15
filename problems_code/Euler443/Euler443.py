#Code written on the 15/02/2025
#Compactifies the runs of consecutive numbers of the sequence using the fact that
#These runs depend on the primes dividing $g(n-1) - n$.
#Specifically, for each prime $p$, this run can only go on for $p - 1 - (n - 1)%p$ terms
#Looping over all primes, we can find the size of this run
#Runs in 427 seconds, much of which is generating all primes up to $10^8$

import time
start = time.time()
from ...CL.CL_Arithmetics import gcd
from ...CL.CL_Primes import PrimeFactorization, Primes
ans = 0

primes = Primes(10**8)
print("==== Primes computed ====")
LIM = 10**15
g = 13
Nums = [[g, 4]]
n = 5
while(n <= LIM):
    pf = PrimeFactorization(g-n, primes)
    step = min([p - 1 - (n - 1)%p for p, a in pf])
    d = gcd(g+step, n+step)
    n += step + 1
    g += d + step
    Nums += [[g, n - 1]]
if n > LIM:
    ans = Nums[-2][0] + (LIM - Nums[-2][1])
else:
    ans = g
#print(Nums)

"""
g = 13
count = 0
nums = [g]
for i in range(5, LIM+1):
    d = gcd(i, g)
    if d > 1:
        count = 0
    else: 
        count += 1
    g += d
    nums += [g]
print(nums)
print("Ans = ", g)"""
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")