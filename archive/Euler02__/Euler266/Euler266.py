# Code written on the 2024/01/05
# Generates all primes, splits the set of primes in two and computes all the products of primes in each set (of size 21, so there are about 2M products)
# Sort each set. For each product p of the first prime set, find largest product q of the second prime set that does not exceed an upper bound
# This bound is cooked up so that $p\times q \leq \sqrt{product of primes}$
# This search uses binary search.
# Runs in 14.7169032 seconds




import time
start = time.time()
from ...CL.CL_Primes import Primes
from ...CL.CL_BinarySearch import BinarySearch
from math import sqrt

primes = Primes(190)
tot = 1
for p in primes:
    tot *= p
l = len(primes)
l1 = ((l+1)//2)
l2 = l - l1
part1 = primes[:((l+1)//2)]
part2 = primes[((l+1)//2):]

def PrimeProduct(n, lst, ln):
    m = n
    ans = 1
    for i in range(ln):
        if m%2 == 1:
            ans *= lst[i]
        m//=2
    return ans

prod1 = [PrimeProduct(i, part1, l1) for i in range(2**l1)]
prod1.sort()
prod2 = [PrimeProduct(i, part2, l2) for i in range(2**l2)]
prod2.sort()
Pl2 = len(prod2)

mmax = 1
for p in prod1:
    #Find in prod2 the corresponding product q s.q. p*q*p*q <= tot, that is q <= sqrt(tot/(p*p))
    iq = BinarySearch(prod2, Pl2, sqrt(tot/(p*p)))
    if iq >= 0:
        q = prod2[iq]
        nmax = p*q
        if mmax < nmax:
            mmax = nmax
print("Answer = ", mmax%(10**16))
end = time.time()
print("Time elapsed ", end - start, " seconds")