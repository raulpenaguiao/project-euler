#Code written in 2024/01/18
#This was really a tough nut to crack. I believe the hardest problem in PE that I have solved. For sure the one that took the most time from me.
#I tried a bunch of strategies, like meet in the middle and creating sum sets that sum in a bounded target
#I came across a really nice fact when searching for this problem on the net (kudos to  [Setphan Brumme](https://euler.stephan-brumme.com/152/) for pointing it out).
#I don't usually search for ideas on the internet and if I do it is often on [Project Euler chat](projecteuler.chat)
#The idea presented there is that for you to clear primes from the denominator, you have to use denominators with this prime.
#This clears all primes that occur once, and the ones that occur more than once can be tested individually to find all the sums that clear the denominators
#To be careful that some numbers are multiples of different large primes (ex 35=5*7) so make sure you test it on only one prime
#To be careful as well on the meet in the middle strategy that when we find a hit, there may be another term just behind the hit that should be counted. This makes a huge difference!
#The roller coaster of this problem proved to be extremely interesting but frustrating...
#Code runs in  2.509976 seconds


import time
start = time.time()
from decimal import Decimal, getcontext 
from ...CL.CL_Primes import MillerRabin
from ...CL.CL_Rational import Rational
from math import sqrt, floor
getcontext().prec = 55



def bin_search(trg, ls, ln):
    #
    top = ln
    bot = -1
    while(top - bot > 1):
        mid = (top+bot)//2
        if ls[mid] > trg:
            top = mid
        else:
            bot = mid
    return bot


def SumsWithListPrime(lst, p):
    #We are given a list of rationals
    #Returns a list with all the sums of terms in lst where p does not divide the denominator
    ans = [Rational(0)]
    for r in lst:
        ans += [a + r for a in ans]
    for a in ans:
        a.reduce()
    return [a.toDecimal() for a in ans if a.denominator%p > 0]


def SumsInBound(lst, lBd, uBd):
    ans = [Decimal(0)]
    l = len(lst)
    cum_sum_lst = [Decimal(0) for _ in range(l)]
    for i in range(l-2, -1, -1):
        cum_sum_lst[i] = cum_sum_lst[i+1] + max( lst[i+1])
    for item_lst, cum_sum in zip(lst, cum_sum_lst):
        newans = []
        lans = len(ans)
        for item in item_lst:
            lbBd = bin_search(lBd - cum_sum - item, ans, lans)
            hbBd = bin_search(uBd - item, ans, lans)
            newans += [ a + item for a in ans[lbBd+1:hbBd+1]]
        ans = newans[:]
        ans.sort()
    return ans

def Sums(lst):
    ans = [Decimal(0)]
    for l, v in lst:
        ans += [a + l for a in ans]
    return ans

def MegaSums(lst):
    ans = [Decimal(0)]
    for termsInList in lst:
        newans = []
        for term in termsInList:
            newans += [a + term for a in ans]
        ans = newans[:]
    return ans
#print(MegaSums([[0, 1, 2], [0, 2, 4], [0, 3, 6]]))
#[Decimal('0'), Decimal('1'), Decimal('2'), Decimal('2'), Decimal('3'), ...

LIM = 80
lol = 0
TARG = Decimal(1)/Decimal(2)
PREC = Decimal(10)**(-36)

bigPrimes = []
possibleSums = []
for i in range(floor(sqrt(LIM))+1, LIM+1):
    if MillerRabin(i):
        bigPrimes.append(i)
        sumsToAppend = SumsWithListPrime([Rational(1, k*k) for k in range(i, LIM+1, i)], i)
        if len(sumsToAppend) > 1:
            possibleSums.append(sumsToAppend)
for i in range(2, LIM+1):
    flag = True
    for p in bigPrimes:
        if i%p == 0:
            flag = False
    if flag:
        lol += 1
        possibleSums.append([Decimal(0), Decimal(1)/Decimal(i*i)])


totalIters = 1
for p in possibleSums:
    totalIters *= len(p)
mdl = 0
totalIters1 = 1
for p in possibleSums:
    mdl += 1
    totalIters1 *= len(p)
    if totalIters1*totalIters1 > totalIters:
        break
possibleSums1 = possibleSums[:mdl]
possibleSums2 = possibleSums[mdl:]


ms1 = MegaSums(possibleSums1)
ms2 = MegaSums(possibleSums2)
ms1.sort()
ms2.sort()

l = len(ms1)
lol = 0
for item in ms2:
    v = bin_search(TARG + PREC - item, ms1, l)
    if TARG - PREC < item + ms1[v] < TARG + PREC:
        lol += 1
        #count how many other items satisfy this prop
        v -= 1
        while TARG - PREC < item + ms1[v] < TARG + PREC:
            v -= 1
            lol += 1




#sib = SumsInBound(possibleSums, TARG - PREC, TARG + PREC)
#print(sib)
print("Answer = ", lol)
end = time.time()
print("Time elapsed ", end - start, " seconds")