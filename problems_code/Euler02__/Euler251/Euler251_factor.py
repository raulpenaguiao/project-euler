#Code written on the 2024/06/12
#$(a, b, c)$ forms a cardano triple if and only if $(2a - 1)^3 = 27 (b^2 \cdot c - a^2)$
#Runs in more than 200.000 seconds



import time
start = time.time()
ans = 0

from ....CL.CL_Primes import Primes, PrimeFactorization


def NumDivsBetween(primeFact, lb, ub):
    divs = set()
    for k in primeFact:
        powList = [k**i for i in range(1, primeFact[k]+1)]
        for d in divs:
            for powk in powList:
                nd = d * powk
                if nd >= ub:
                    break
                divs.add(nd)
    ans = 0
    for d in divs:
        if d >= lb:
            ans += 1
    return ans
        
    

N = 11*10**4
lm = (N+1)//3
LM = lm*8
primes = Primes(LM)

primeFact = [{} for _ in range(LM+1)]
for p in primes:
    for q in range(p, LM, p):
        primeFact[q][p] = 1
    ppow = p*p
    while(ppow < LM):
        for q in range(ppow, LM, ppow):
            primeFact[q][p] += 1
        ppow *= p


def f(x, y):
    3*x*x*x-2*y*x+M

#a runs from 1 to N-1, is of the form 3a0 -2
#a0 runs from 1 to (N+1)//3 = lm
for a0 in range(1, LM+1):
    primeFactNewNum = {}
    for k in primeFact[a0]:
        primeFactNewNum[k] = primeFact[a0][k]*2
    for k in primeFact[8*a0-3]:
        if k in primeFactNewNum:
            primeFactNewNum[k] += primeFact[8*a0-3][k]
        else:
            primeFactNewNum[k] += primeFact[8*a0-3][k]
    a = 3*a0-1
    M = a0*a0*(8*a0-3)
    if f(2*(N-a)/3, N-a, M) > 0:
        continue

    ans += NumDivsBetween(primeFactNewNum, lb, ub)

print("Answer = ", ans)

end = time.time()
print("Time elapsed ", end - start, " seconds")