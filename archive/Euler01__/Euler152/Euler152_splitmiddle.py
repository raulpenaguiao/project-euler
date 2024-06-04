import time
start = time.time()
from decimal import Decimal, getcontext 
getcontext().prec = 16
from ...CL.CL_Rational import Rational

LIM = 35
TARG = Rational(1, 2)
ls1 = [Rational(1, i**i) for i in range(2, LIM//2)]
ls2 = [Rational(1, i**i) for i in range(LIM//2, LIM+1)]

def Sums(ls):
    if ls == []:
        return [Rational(0)]
    oS = Sums(ls[1:])
    return oS + [k+ls[0] for k in oS]

ls1 = [Rational(i) for i in range(10)]
ls2 = [Rational(i) for i in range(10)]
TARG = Rational(5)

sum1 = Sums(ls1)
sum1.sort()
sum2 = Sums(ls2)
sum2.sort()
l = len(sum2)
print(sum1)
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

ans = 0
for s in sum1:
    ind = bin_search(TARG - s, sum2, l)
    if ind >= 0 and s + sum2[ind] == TARG:
        ans += 1

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")