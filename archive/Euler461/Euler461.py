#Code written on the 2023/12/14
#Computes all possible sums of two terms that are below PI
#Sorting this list of sums, for each term $t$ we find the numbers that are close to $\pi-t$ and check if these improve our current best
#Make sure to use binary search for checking values.
#In total there are $L\times 1.5$ integers to test in the function, and so the list will not have more than $n = 2.25\times L^2$ terms.
#Sorting takes $n \log n = O(L^2 \log L)$ and binary search takes $O(\log n) = $O(\log L)$, so the whole algoritm takes $O(L^2 \log L)$ complexity.
#Runs in 5 minutes




import time
start = time.time()
import math
from decimal import Decimal, getcontext 
getcontext().prec = 30
PI = Decimal("3.14159265358979323846264338327950288419716939937510")
PREC = Decimal("1")


def f(n, k):
    return Decimal(math.exp(Decimal(k/n)))-Decimal(1)


def binary_search(lst, value):
    #Gives the largest index i that has lst[i] <= value
    #if there is no such index (that is all elements are > value) returns -1
    top = len(lst)
    bot = -1
    while(top - bot > 1):
        mid = (top + bot)//2
        if lst[mid] <= value:
            bot = mid
        else:
            top = mid
    return bot

def Score (tpl):
    ans = 0
    for k in tpl:
        ans += k**2
    return ans


N = 10000
kLIM = math.floor(Decimal(10)+Decimal(N*math.log(PI+Decimal(1))))
print("Number of integers tried = ", kLIM)
guess = math.floor(N*math.log(PI+Decimal(1)))
ans = guess**2
PREC = abs(f(N, guess) - PI)
print("Precision taken = ", PREC)
F = [[f(N, i), tuple([i])] for i in range(kLIM)]

listValues = F[:]
for i in range(1, kLIM):
    for j in range(1, i+1):
        nval = F[i][0] + F[j][0]
        if nval > PI + PREC:
            break
        listValues.append([nval, tuple([i, j])])
lenListValues = len(listValues)
end = time.time()
print("List created ", end - start, " seconds")
listValues.sort()
listOnlyValues = [g[0] for g in listValues]

for vl, tpl in listValues:
    if vl*2 > PI + PREC:
        break
    index = binary_search(listOnlyValues, PI-vl)
    if index == -1:
        ab = listOnlyValues[index+1]
        p = abs(PI-vl-ab)
        if p < PREC:
            PREC = p
            ans = Score(tpl) + Score(listValues[index+1][1])
        continue
    bl = listOnlyValues[index]
    p = abs(PI-vl-bl)
    if p < PREC:
        PREC = p
        ans = Score(tpl) + Score(listValues[index][1])
    if index == lenListValues - 1:
        continue
    ab = listOnlyValues[index+1]
    p = abs(PI-vl-ab)
    if p < PREC:
        PREC = p
        ans = Score(tpl) + Score(listValues[index+1][1])

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")
