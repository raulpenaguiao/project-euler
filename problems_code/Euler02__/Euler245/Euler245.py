#Code written on the 2024/01/09
# this code only solves the problem for n = pq, for p, q primes
# even for this case is extremely slow for the goal target, expected to run to up to one hour
# It uses the fact that if n - phi | n - 1, then p + q - 1 | p*p - p + 1
# assume p < q, then we have that p < LIM**(2/3), so we can check all the divisors of p*p-p+1 and see if they satisfy p*q <= LIM and q > p
# do not forget to sort the divisors set!
# A really natural way of improving the time is by reducing the primes we need to compute

import time
start = time.time()
from ...CL.CL_Primes import Primes, Divisors, MillerRabin, EulerPhi
from ...CL.CL_BinarySearch import BinarySearch
import math
ans = 0



LIM = 2*(10**11)
LIM = 1793689
lim = math.floor(LIM**(2/3))+math.floor(LIM**(1/2))*2
primes = Primes(lim)
phi = EulerPhi(LIM)
ln = len(primes)
for p in primes:
    if 2*p > min(p*p-p+1, LIM//p + p - 1):
        continue
    div = Divisors(p**2-p+1, primes)
    div.sort()
    lnd = len(div)
    bot = BinarySearch(div, lnd, 2*p)
    top = BinarySearch(div, lnd, min(p*p-p+1, LIM//p + p -1))
    for ind in range(bot + 1, top + 1):
        Q = div[ind]
        q = Q - p + 1
        if MillerRabin(q):
            ans += p*q
            print(p, q, (p*q - 1)//(p*q - phi[p*q]))
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")