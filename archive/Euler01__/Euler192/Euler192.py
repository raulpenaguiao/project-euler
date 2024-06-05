#Code written on the 2023/11/23
#Computes the continued fraction of all the square roots up to 100.000, this is the part that takes time
#Then generates all the convergents and semiconvergents (with last entry at least half of the same entry of sqrt(n))
#I think there is a theorem that tells us exactly which of the convergents are the ones that we want
#But I just select all of them, sort and pick the closest one
#Expected to run for 22 hours, exactly 78910 seconds 

import time
import math
from ...CL.CL_ContinuedFractions import toRational, ContinuedFractionsqrt
from ...CL.CL_Rational import Rational
start = time.time()
ans = 0


def FindOrderAprox(cf, ord, n):
    newa = Rational(cf[0])
    aprox = [newa]
    currlist = [cf[0]]
    i = 0
    MOD = len(cf[1])
    while(newa.denominator <= ord):
        newv = cf[1][i%MOD]
        aprox.append(newa)
        for j in range((newv+1)//2, newv):
            aprox.append(toRational(currlist + [j]))
        currlist += [newv]
        i += 1
        newa = toRational(currlist)
    aprox = [r for r in aprox if r.denominator <= ord]
    aprox.sort()
    ub = sorted([r for r in aprox if Rational.Times(r, r) > Rational(n)])[0]
    lb = sorted([r for r in aprox if Rational.Times(r, r) < Rational(n)])[-1]
    mb = Rational.Plus(lb, ub)
    mb = Rational.Times(mb, mb)
    if mb > Rational.Times(Rational(n), Rational(4)):
        return lb
    return ub

LIM = 100000
o = 10**12

for i in range(1, LIM+1):
    l = ContinuedFractionsqrt(i)
    if len(l) > 1:
        r = FindOrderAprox(l, o, i)
        if(i%829 == 21):
            print(i, r)
            end = time.time()
            ex =  (end - start)*(LIM/i)**2
            print("Time elapsed ", end - start, " seconds, expected time is ", ex, " seconds")
        ans += r.denominator


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")