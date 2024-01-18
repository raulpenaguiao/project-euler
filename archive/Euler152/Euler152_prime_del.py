import time
import math
start = time.time()
from decimal import Decimal, getcontext 
from ...CL.CL_Primes import MillerRabin
from ...CL.CL_Rational import Rational
from math import sqrt, floor
getcontext().prec = 16



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


def bin_searchD(trg, ls, ln):
    top = ln
    bot = -1
    while(top - bot > 1):
        mid = (top+bot)//2
        if ls[mid][0] > trg:
            top = mid
        else:
            bot = mid
    return bot

def SumsWithListPrime(lst, p):
    #We are given a list of rationals
    #Returns a list with all the sums of terms in lst where p does not divide the denominator
    ans = [[Rational(0), []]]
    for r in lst:
        #for a in ans:
        #    print(a)
        ans += [[a + r, b+[r]] for a, b in ans]
    #print("Ans = ", ans)
    for a, b in ans:
        a.reduce()
    #print("Ans = ", ans)
    #for a, b in ans:
    #    print(a, b)
    return [[a.toDecimal(), b] for a, b in ans if a.denominator%p > 0]


def SumsInBound(lst, lBd, uBd):
    ans = [[Decimal(0), []]]
    l = len(lst)
    cum_sum_lst = [Decimal(0) for _ in range(l)]
    for i in range(l-2, -1, -1):
        cum_sum_lst[i] = cum_sum_lst[i+1] + max([l[0] for l in lst[i+1]])
    #print(cum_sum_lst)
    for item_lst, cum_sum in zip(lst, cum_sum_lst):
        #print(item_lst, cum_sum, len(ans), lBd - cum_sum, cum_sum)
        newans = []
        lans = len(ans)
        for item, currTerms in item_lst:
            lbBd = bin_searchD(lBd - cum_sum - item, ans, lans)
            hbBd = bin_searchD(uBd - item, ans, lans)
            newans += [ [a + item, b + [item]] for a, b in ans[lbBd+1:hbBd+1]]
        ans = newans[:]
        ans.sort()
        #print("+++++++++++++++++++++", len(ans), "++++++++++++++++++++++")
        #print("values to be considered = ", [MaybeRound(1/sqrt(it[0])) for it in item_lst if it[0] > 0])
        #presSums(ans)
        #print(ans)
    return ans

def MaybeRound(k):
    l = round(k)
    if abs(l-k < PREC):
        return l
    return k

def presSums(ls):
    ansToPrint = [[MaybeRound(1/sqrt(r)) for r in l if r > 0] for a, l in ls]
    ansToPrint.sort()
    for a in ansToPrint:
        print(a, " - ", sum([Decimal(1)/Decimal(k*k) for k in a]))
    return


def Sums(lst):
    #print(lst)
    #for l in lst:
    #    print("li = ", l)
    ans = [[Decimal(0), []]]
    for l, v in lst:
        #print(ans)
        ans += [[a + l, b + [l]] for a, b in ans]
    return ans

LIM = 45
lol = 0
TARG = Decimal(1)/Decimal(2)
PREC = Decimal(10)**(-10)

bigPrimes = []
possibleSums = []
for i in range(floor(sqrt(LIM))+1, LIM//2+1):
    if MillerRabin(i):
        bigPrimes.append(i)
        lol+= 1
        sumsToAppend = SumsWithListPrime([Rational(1, k*k) for k in range(i, LIM+1, i)], i)
        if len(sumsToAppend) > 1:
            possibleSums.append(sumsToAppend)
            print(i, possibleSums[-1])
for i in range(2, LIM+1):
    flag = True
    for p in bigPrimes:
        if i%p == 0:
            flag = False
    if flag:
        lol += 1
        possibleSums.append([[0, []], [Decimal(1)/Decimal(i*i), [Decimal(1)/Decimal(i*i)]]])
        print(i, possibleSums[-1])
#for p in possibleSums:
#    print(p)
#par = [l for l in possibleSums if len(l) > 1]
#ls = Sums([p[1] for p in par])
#print(ls)
#ls = [k for k in ls if TARG - PREC < k[0] and TARG + PREC > k[0]]
#ls.sort()

sib = SumsInBound(possibleSums, TARG - PREC, TARG + PREC)
#print(sib)
print("Answer = ", len(sib))
end = time.time()
print("Time elapsed ", end - start, " seconds")