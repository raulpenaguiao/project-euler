#Code written on the 12/12/2023
#For each possible length a computes all the possible sides b, c
#These satisfy (b+c)*(c-b) = a*a - 1
#This means that b+c is a divisor of a*a-1, that satisfies some bounds, so for all a*a-1 cound such divisors and add everything up
#Make sure to precompute the factorization of all integers < 25*10**6/3 to factor (a-1)(a+1)
#Code runs in 6.6 minutes


import time
start = time.time()
import math
from ...CL.CL_Primes import Primes


def DivLimited(fc, LIM):
    if fc == []:
        return [1]
    p = fc[0][0]
    exp = fc[0][1]
    powList = [1]
    ans = []
    for _ in range(exp):
        oas = powList[-1]*p
        if oas > LIM:
            break
        powList.append(oas)
    for d in DivLimited(fc[1:], LIM):
        if d > LIM:
            break
        for power in powList:
            s = d*power
            if s > LIM:
                break
            ans.append(d*power)
    return ans

def g(L):
    primes = Primes(math.floor(math.floor(2.5*L/3)+1)+10)
    ans = (L-1)//2
    primeFact = [[] for a in range(L//3 + 2)]
    for p in primes:
        for i in range(p, L//3 + 2, p):
            primeFact[i].append([p, 1])
        powp = p*p
        while(powp <= L//3 + 1):
            for i in range(powp, L//3 + 2, powp):
                primeFact[i][-1][1] += 1
            powp *= p

    for a in range(2, L//3 + 1):
        toFact = {x:y for x, y in primeFact[a+1]}
        for x, y in primeFact[a-1]:
            if x in toFact:
                toFact[x] += y
            else:
                toFact[x] = y
        dvs = DivLimited([[k, toFact[k]] for k in toFact], L-a)
        for d in dvs:
            if (d - (a*a-1)//d)%2 == 0 and d >= a + math.sqrt(2*a*a-1):
                ans += 1
    return ans


def g_naive(L):
    ans = 0
    for c in range(1, L):
        for b in range(1, c):
            a = math.floor(math.sqrt(c*c-b*b+1)+.5)
            if a*a == c*c-b*b+1:
                if a+b+c <= L and a <= b and a > 0 and a+b >c:
                    ans += 1
                    #print(a, b, c)
        if 2*c+1 <= L:
            ans += 1
            #print(1, c, c)
    return ans 

L = 25*10**6
print("Answer = ", g(L))
#print("Answer naive = ", g_naive(L))
end = time.time()
print("Time elapsed ", end - start, " seconds")