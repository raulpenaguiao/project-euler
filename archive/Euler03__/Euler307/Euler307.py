#Code written on the 2024/06/04
#Answer is $1 - \frac{k! \sum_{l = 0}^{k/2} \binom{n}{l} \binom{n-l}{k-2l}2^{-l}}{n^k}$
#Runs in 179.227 seconds, mostly because of the rational structure that is very gcd heavy.


import time
start = time.time()
ans = 0

import sys
from ....CL.CL_Rational import Rational



def binom(n, k):
    if k == 0:
        return 1
    return Rational(n, k)*binom(n-1, k-1)

def fact(k):
    if k == 0:
        return 1
    return fact(k-1)*k

sys.setrecursionlimit(3_000_010)
sys.set_int_max_str_digits(200_000)

def p(k, n):
    sum = Rational()
    bin1 = Rational(1)
    bin2 = binom(n, k)
    pow2 = Rational(1)
    LIM = k//2 + 1
    for l in range(LIM):
        sum += bin1*bin2*pow2
        pow2 *= Rational(1, 2)
        bin1 *= Rational(n-l, l+1)
        bin2 *= Rational((k-2*l)*(k-2*l-1), (n-l)*(n-k+l+1))
    return Rational(1) - Rational(fact(k), n**k)*sum

n = 10**6
k = 20*10**3
print("Answer = ", p(k, n).toFloat())
end = time.time()
print("Time elapsed ", end - start, " seconds")