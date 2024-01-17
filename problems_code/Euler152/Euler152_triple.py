import time
import math
start = time.time()
from decimal import Decimal, getcontext 
from ...CL.CL_Arithmetics import InverseMod
from ...CL.CL_Primes import MillerRabin
from ...CL.CL_Rational import Rational

#I dont know what to do with a triple stack but maybe it helps


getcontext().prec = 40
PREC = Decimal(10)**-14

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



def Sums(lst, zero):
    ans = [zero]
    for l in lst:
        ans += [a + l for a in ans]
    return ans

def SumsInBound(lst, zero, lBd, uBd):
    ans = [zero]
    l = len(lst)
    cum_sum_lst = [zero for _ in range(l)]
    for i in range(l-2, -1, -1):
        cum_sum_lst[i] = cum_sum_lst[i+1] + lst[i+1]
    for item, cum_sum in zip(lst, cum_sum_lst):
        lans = len(ans)
        lABd = bin_search(lBd - cum_sum, ans, lans)
        hBBd = bin_search(uBd - item, ans, lans)
        #print(item, cum_sum)
        #print(lans, lABd, hBBd, ans)
        ans = ans[lABd+1:] + [ a + item for a in ans[:hBBd+1]]
        ans.sort()
        #print(ans)
    return ans


print(SumsInBound([1, 3, 5, 9], 0, 10, 13))
class DoubleRational:
    def __init__(self, rat, p):
        self.real = Decimal(rat.numerator) / Decimal(rat.denominator)
        self.mod = (rat.numerator)* InverseMod(rat.denominator, p)
        self.p = p
    
    def __add__(self, other):
        ans = DoubleRational(Rational(0), self.p)
        ans.real = self.real + other.real
        ans.mod = (self.mod + other.mod)%self.p
        ans.p = self.p
        return ans
    
    def __sub__(self, other):
        ans = DoubleRational(Rational(0), self.p)
        ans.real = self.real - other.real
        ans.mod = (self.mod - other.mod)%self.p
        ans.p = self.p
        return ans

    def __repr__(self):
        return "[ " + str(self.real)  + ", " + str(self.mod) + " ]"

    def __lt__(self, obj):
        return self.real < obj.real

    def __gt__(self, obj):
        return self.real > obj.real

    def __le__(self, obj):
        return self.real <= obj.real

    def __ge__(self, obj):
        return self.real >= obj.real

    def __eq__(self, obj):
        return abs(self.real - obj.real) < PREC and self.mod == obj.mod

#Find prime > 100_000_000
prime = 100_000_001
while not MillerRabin(prime):
    prime += 2
print("Prime found = ", prime)


LIM = 80
TARG = DoubleRational(Rational(1, 2), prime)

spl1 = (LIM + 1)//2
spl2 = 3*(LIM + 1)//4
spl1 = 30
spl2 = 55
ls1 = [DoubleRational(Rational(1, i*i), prime) for i in range(2, spl1)]
ls2 = [DoubleRational(Rational(1, i*i), prime) for i in range(spl1, spl2)]
ls3 = [DoubleRational(Rational(1, i*i), prime) for i in range(spl2, LIM+1)]
bord = DoubleRational(Rational(0), prime)
for k in ls2:
    bord += k
for k in ls3:
    bord += k

print("bord = ", bord)
print(len(ls1))
print(len(ls2))
print(len(ls3))


s1 = SumsInBound(ls1, DoubleRational(Rational(0), prime), TARG - bord, TARG)
s2 = Sums(ls2, DoubleRational(Rational(0), prime))
s2.sort()
s3 = Sums(ls3, DoubleRational(Rational(0), prime))
s3.sort()

ans = 0
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")