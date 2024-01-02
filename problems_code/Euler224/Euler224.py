#Code written on the 12/12/2023
#Will find divisors up until 25_000_000
#Expected 410208.2777810097 seconds = 5 days
#Started to run at 10h20 on Tuesday 2nd Jan


import time
start = time.time()
import math
from ...CL.CL_Primes import Primes, PrimeFactorization

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
    start = time.time()
    print("Computing primes up to ", math.floor(2.5*L/3)+1)
    primes = Primes(math.floor(2.5*L/3)+1)
    print("Primes computed")
    end = time.time()
    print("Time elapsed ", end - start, " seconds")
    ans = 0
    for a in range(2, L//3 + 1):
        if a%513 == 142:
            print("Finding divisors for a = ", a)
            end = time.time()
            print("Time elapsed ", end - start, " seconds")
        dvs = DivLimited( PrimeFactorization(a*a+1, primes), L-a)
        #print(a, dvs, nextFac, prevFac)
        for d in dvs:
            if (d - (a*a+1)//d)%2 == 0 and d >= a + math.sqrt(2*a*a+1):
                ans += 1
    return ans

def g_naive(L):
    ans = 0
    for c in range(1, L):
        for b in range(1, c+1):
            a = math.floor(math.sqrt(c*c-b*b+1)+.5)
            if a*a == c*c-b*b-1:
                if a+b+c <= L and a <= b and a > 0 and a+b >c:
                    ans += 1
    return ans 

L = 75*10**6
print("Answer = ", g(L))
#print("Answer naive = ", g_naive(L))
end = time.time()
print("Time elapsed ", end - start, " seconds")