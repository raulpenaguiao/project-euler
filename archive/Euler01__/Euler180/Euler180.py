#Code written on the 2023/11/23
#Expression reduces to (x+y+z)(x^n + y^n - z^n)
#allowed rationals are a/b between 0 and 1 such that b <= K
#Finds all rationals of order 35 (there are 383 such rationals)
#for two rationals, compute the four possible z and sees if they are
# - between 0 and 1
# - of the given order
#Runs in 1.18 seconds


import time
import math
from ...CL.CL_Rational import Rational, gcd
start = time.time()
K = 35
count = 0
num = 0
ans = []


def AddNewValue(ans, x, y, z):
    newR = Rational()
    newR.add(x)
    newR.add(y)
    newR.add(z)
    newR.reduce()
    #print("New member ===> ", newR)
    ans.append([newR.numerator, newR.denominator])


def DeleteCopies(st):
    if st == []:
        return []
    t = sorted(st)
    #print(sorted([RC.Rational(r[0], r[1]) for r in t]))
    finalList = [t[0]]
    for i in range(1, len(t)):
        if not(t[i] == t[i-1]):
            finalList += [t[i]]
    #print(sorted([RC.Rational(r[0], r[1]) for r in finalList]))
    return finalList


def isORDER(r, K):
    if r <= Rational() or Rational(1) <= r:
        return False
    return r.denominator <= K


rationalsOfOrder = []
for a in range(1, K+1):
    for b in range(1, K+1):
        r = Rational(a, b)
        if gcd(a, b) == 1 and isORDER(r, K):
            rationalsOfOrder.append(r)
lenRationals = len(rationalsOfOrder)
num = lenRationals*(lenRationals+1)*2
print("For order ", K)
print("There are ", len(rationalsOfOrder),  " rationals with the given order.")
PREC = 10**(-6)

for i in range(lenRationals):
    x = rationalsOfOrder[i]
    for j in range(i+1):
        y = rationalsOfOrder[j]
        z = Rational.Plus(x, y)
        if isORDER(z, K):
            AddNewValue(ans, x, y, z)
        z = Rational.Plus(x.Reverse(), y.Reverse()).Reverse()
        if isORDER(z, K):
            AddNewValue(ans, x, y, z)
        z = Rational.Plus(Rational.Times(x, x), Rational.Times(y, y))
        flag = z.SquareRoot()
        if flag and isORDER(z, K):
            AddNewValue(ans, x, y, z)
        z = Rational.Plus(Rational.Times(x, x).Reverse(), Rational.Times(y, y).Reverse()).Reverse()
        flag = z.SquareRoot()
        if flag and isORDER(z, K):
            AddNewValue(ans, x, y, z)

count = len(ans)
ans = DeleteCopies(ans)
tot = Rational()
for n, d in ans:
    tot.add(Rational(n, d))
print("There are ", num, " possible values.")
print("There are ", count, " solutions.")
print("There are ", len(ans), " distinct solutions.")
print("Answer = ", tot.numerator+tot.denominator)
print("Total ", tot)

end = time.time()
print("Time elapsed ", end - start, " seconds")