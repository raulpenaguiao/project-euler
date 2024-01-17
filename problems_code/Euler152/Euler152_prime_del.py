import time
import math
start = time.time()
from decimal import Decimal, getcontext 
from ...CL.CL_Primes import MillerRabin
from ...CL.CL_Rational import Rational
from math import sqrt, floor
getcontext().prec = 16



def bin_search(trg, ls, ln):
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
        cum_sum_lst[i] = cum_sum_lst[i+1] + max(lst[i+1])
    for item_lst, cum_sum in zip(lst, cum_sum_lst):
        #print(item_lst, cum_sum, len(ans), lBd - cum_sum, cum_sum)
        newans = []
        lans = len(ans)
        for item in item_lst:
            lbBd = bin_search(lBd - cum_sum - item, ans, lans)
            hbBd = bin_search(uBd - item, ans, lans)
            newans += [ a + item for a in ans[lbBd+1:hbBd+1]]
        ans = newans[:]
        ans.sort()
        #print(ans)
    return ans


def Sums(lst):
    ans = [Decimal(0)]
    for l in lst:
        ans += [a + l for a in ans]
    return ans

LIM = 80
lol = 0
TARG = Decimal(1)/Decimal(2)
PREC = Decimal(10)**(-3)

bigPrimes = []
possibleSums = []
for i in range(floor(sqrt(LIM)), LIM//2+1):
    if MillerRabin(i):
        bigPrimes.append(i)
        lol+= 1
        possibleSums.append(SumsWithListPrime([Rational(1, k*k) for k in range(i, LIM+1, i)], i))
for i in range(2, LIM//2+1):
    flag = True
    for p in bigPrimes:
        if i%p == 0:
            flag = False
    if flag:
        lol += 1
        possibleSums.append([0, Decimal(1)/Decimal(i*i)])


par = [l for l in possibleSums if len(l) > 1]
#print(len(par))
ls = Sums([p[1] for p in par])
#print(len(ls))
ls = [k for k in ls if TARG - PREC < k and TARG + PREC > k]
ls.sort()
#f = open("demofile2.txt", "a")
#for k in ls:
#    f.write(str(k))
#    f.write("\n")
#f.close()
#print(len(ls))
#ls.sort()
#vl = bin_search(TARG, ls, len(ls))
#print(vl)
#print(ls[vl])
#ONEFORUTH = Decimal(1)/Decimal(4)
#print(SumsInBound([[0, ONEFORUTH], [0, ONEFORUTH], [0, ONEFORUTH]], TARG-PREC, TARG+PREC))
sib = SumsInBound(possibleSums, TARG - PREC, TARG + PREC)
print("Answer = ", len(sib))
end = time.time()
print("Time elapsed ", end - start, " seconds")