#Code written in 2023/12/07
#For each power of prime that superdivides the module, we compute the remainder
#This is done by computing the period of fibbs over each prime power, because there are no prime powers larger than 630_803, the period is of the order of milions
#Primes generated by MillerRabin
#Code runs in 11.77 seconds


import time
start = time.time()
from ...CL.CL_Arithmetics import ChineseRemainder
from ... CL.CL_Primes import MillerRabin

def SumFibPrimes(nums, mod):
    fibbs = [0, 1, 1]
    print("mod = ", mod)
    while not( fibbs[-1]%mod == 1) or not( fibbs[-2]%mod == 0 ):
        fibbs.append((fibbs[-1]+fibbs[-2])%mod)
    Q = len(fibbs)-2
    print("Has period ", Q)
    return sum([fibbs[n%Q] for n in nums])%mod

def GeneratePrimes(lB, size):
    lst = []
    sz = 0
    a = lB + 1
    while(sz < size):
        if MillerRabin(a):
            lst.append(a)
            sz += 1
        a += 1
    return lst



quest = [[3, 1], [7, 1], [13, 1], [67, 1], [107, 1], [630803, 1]]
lB = 10**14
nPrimes = 10**5
lPrimes = GeneratePrimes(lB, nPrimes)



ans = ChineseRemainder([[SumFibPrimes(lPrimes, p**e), p**e] for p, e in quest])

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")