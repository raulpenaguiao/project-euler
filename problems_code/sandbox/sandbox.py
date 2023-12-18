import time
start = time.time()
import CL_Arithmetics as CA
import CL_Primes as CP
import math


def Num(s):
    if s == []:
        return 1
    return Num(s[1:])*(s[0][0]**s[0][1])

def psi(n):
    ans = [0 for _ in range(n+1)]
    for a in range(math.floor(math.sqrt(n))+1):
        for b in range(a+1):
            c = a**2+b**2
            if c <= n:
                ans[c] +=1
    return ans
L = 200
primes = CP.Primes(L)
s = [[CP.PrimeFactorization(index, primes), num] for index, num in enumerate(psi(L)) if num > 0]
for a in s:
    print(Num(a[0]), a)
end = time.time()
print("Time elapsed ", end - start, " seconds")