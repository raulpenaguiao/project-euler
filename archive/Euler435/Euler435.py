#Code written in 2023/12/07
#We compute each F_n(x) mod p**e separately for each power divisor of 15!
#Note that each power divisor of 15! will not be larger than 2.5k, so the fibonacci period will not be larger than (2.5k)**2
#We use the fact that fibbs is periodic as well as the powers are periodic to compress the sum as much as possible, will be the size at most (2.5k)**2
#Runs in 0.1493 seconds



import time
start = time.time()
from ...CL.CL_Arithmetics import PowerMod, InverseMod, ChineseRemainder, gcd
ans = 0


def SumPowerMod(tr, n, mod):#We are using the fact that mod is a power of a prime, so either a-1 and mod are coprime or a and mod are coprime
    a = tr%mod
    if gcd(a+mod-1, mod) == 1:
        return ((PowerMod(a, n, mod) - 1)*(InverseMod(a-1, mod)))%mod
    powa = a
    totsum = 1
    period = 1
    while(powa > 1):
        powa *= a
        powa %= mod
        period += 1
    rs = n%period
    if rs == 0 :
        return 0
    powa = a%mod
    totsum = 1
    for _ in range(1, rs):
        totsum += powa
        powa *= a
        powa %= mod
    return totsum%mod


def FPoly(N, n, mod, phi):
    fibbs = [0, 1, 1]
    while not( fibbs[-1]%mod == 1) or not( fibbs[-2]%mod == 0 ):
        fibbs.append(fibbs[-1]+fibbs[-2])
    Q = len(fibbs)-2
    P = Q*phi//(gcd(Q, phi))
    ans = 0
    for x in range(N+1):
        powx = [1]
        for i in range(1, P):
            powx.append((x*powx[-1])%mod)
        gpx = 0
        res = n%P
        for i in range(P):
            gpx += fibbs[i%Q]*powx[i]
            gpx %= mod
            if i == res:
                gpres = gpx
        toAdd = gpx*SumPowerMod(PowerMod(x, P, mod), n//P, mod)+PowerMod(x, n-res, mod)*gpres
        toAdd %= mod
        ans += toAdd
        ans %= mod
    return ans
        


quest = [[2, 11], [3, 6], [5, 3], [7, 2], [11, 1], [13, 1]]
N = 100
n = 10**15
remList = [[FPoly(N, n, p**e, (p-1)*p**(e-1)), p**e] for p, e in quest]
print("Answer = ", ChineseRemainder(remList))
end = time.time()
print("Time elapsed ", end - start, " seconds")


"""
"""