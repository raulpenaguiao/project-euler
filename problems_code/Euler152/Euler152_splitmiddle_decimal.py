import time
start = time.time()
from decimal import Decimal, getcontext 
getcontext().prec = 40

PREC = Decimal(10)**-30

def bin_search(trg, ls, ln):
    #Returns the largest inxed i such that ls[i] < trg
    top = ln
    bot = -1
    while(top - bot > 1):
        mid = (top+bot)//2
        if ls[mid] > trg:
            top = mid
        else:
            bot = mid
    return bot

#print(sum([Decimal(1)/Decimal(i*i) for i in range(2, 50)]))
#print(sum([Decimal(1)/Decimal(i*i) for i in range(50, 81)]))




lsSol1 = [2, 3, 4, 5, 7, 12, 15, 20, 28, 35]
lsSol2 = [2, 3, 4, 6, 7, 9, 10, 20, 28, 35, 36, 45]
lsSol3 = [2, 3, 4, 6, 7, 9, 12, 15, 28, 30, 35, 36, 45]
lsSold1 = [Decimal(1)/Decimal(i*i) for i in lsSol1]
lsSold2 = [Decimal(1)/Decimal(i*i) for i in lsSol1]
lsSold3 = [Decimal(1)/Decimal(i*i) for i in lsSol1]
#ans = Decimal(0)
#for k in lsSol1:
#    ans += Decimal(1)/Decimal(k*k)
#    print(ans)
#print(ans)
ans = Decimal(0)

def BsumsSums(lst, lBd, uBd):
    l = len(lst)
    cum_sum_lst = [0 for _ in range(l)]
    for i in range(l-2, -1, -1):
        cum_sum_lst[i] = cum_sum_lst[i+1] + lst[i+1]
    ans = [0]
    testValue = Decimal(0)
    for index, item in enumerate(lst):
        if item in lsSold1:
            testValue += item
            #print(item, 1/item)
            #print(":::::: TV = ", testValue)
        l = len(ans)
        lTers = bin_search(uBd-item, ans, l)
        hTers = bin_search(lBd-cum_sum_lst[index], ans, l)
        #print("value parameters = ", item, cum_sum_lst[index], index+2)
        #print("len answer = ", len(ans), " new item = ",  item)
        #print("lower bound info = ", hTers, lBd-cum_sum_lst[index]+PREC)
        #print("upper bound info = ", lTers, uBd-item+PREC)
        #print(ans[hTers+1:], [a + item for a in ans[:lTers+1]])
        ans = ans[hTers+1:] + [a + item for a in ans[:lTers+1]]
        ans.sort()
        #if not ans == []:
        #    print(ans[0],  " ::: ", ans[-1], " with ", len(ans), " elements")
        #else:
        #    print("ans = []")
        #tv = bin_search(testValue + Decimal(10)**-7, ans, len(ans))
        #if(tv >= 0 and tv < len(ans) and abs(ans[tv] - testValue) > Decimal(10)**-5):
        #    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ADSD++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", ans[tv],  testValue)
        #print("testvalues are in ", ans[tv-2:tv+2], tv-2, tv+2, " tv = ", tv,  " and value is ", testValue)
    #print(ans[-1] + Decimal(1)/Decimal(28*28) + Decimal(1)/Decimal(35*35))
    return ans
#print(BsumsSums([1, 3, 5, 6], 3, 12))
#print(BsumsSums([Decimal(1)/Decimal(i*i) for i in range(2, 10)], Decimal(1)/Decimal(3), Decimal(1)/Decimal(2)))

def Sums(ls):
    if ls == []:
        return [Decimal(0)]
    oS = Sums(ls[1:])
    return oS + [k+ls[0] for k in oS]

"""
ls1 = [Decimal(i) for i in range(10)]
ls2 = [Decimal(i) for i in range(10)]
TARG = Decimal(5)
"""

LIM = 55
spl = 35
TARG = Decimal(1)/Decimal(2)
ls1 = [Decimal(1)/Decimal(i*i) for i in range(2, spl)]
ls2 = [Decimal(1)/Decimal(i*i) for i in range(spl, LIM+1)]


sum1 = BsumsSums(ls1, TARG - sum(ls2)-PREC, TARG+PREC)
sum2 = Sums(ls2)
sum2.sort()

print(len(sum1))
print(len(sum2))

l = len(sum1)

ans = 0
for s in sum2:
    ind = bin_search(TARG - s + PREC, sum1, l) #This + PREC is necessary because if it is not there some of the solutions are not caught
    if ind >= 0 and abs(s + sum1[ind] - TARG) < PREC:
        ans += 1

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")