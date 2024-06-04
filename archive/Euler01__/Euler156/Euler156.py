#code written on the 2023/11/03
#Use a divide and conquer approach. if we know f(n*10^s-1, d) we can compute f((n*10+t)*10^(s-1) - 1, d) very easily
#Only divide when there is any chance there is a solution in the interval. This is enough
#runs in 0.023s


import time
import math
start = time.time()


def digs(n, base = 10):
    if n < base:
        return [n]
    return digs(n//base, base) + [n%base]

def s(d):
    ans = 0
    #Let's take care of all the solutions < 1000 first
    cumul = 0
    for i in range(1000):
        for t in digs(i):
            if t == d:
                cumul += 1
        if cumul == i:
            ans += i
    #Now we take care of all the solutions that are between 10^t and 10^(t+1) - 1 inclusive
    #we know such solution only exists for t < 100
    t = 3
    for t in range(3, 100): #Lets find some solutions now
        ans += RecSolFinder(d, t, [10**t-1, t*(10**(t-1))], [10**(t+1)-1, (t+1)*(10**t)], 0, True)    
    return ans

def RecSolFinder(d, t, lB, uB, stemDigs, flag = False):
    #d is the digit that we are counting
    #t is the number of digits that uB and lB do not match
    if lB[0] > uB[1] or uB[0] < lB[1]:
        return 0
    if t == 0:
        currCount = lB[1]
        ans = 0
        for i in range(10):
            currCount += stemDigs
            if(d == i):
                currCount += 1
            if lB[0]+i+1 == currCount:
                ans += lB[0]+i+1
        return ans
    ans = 0
    pow10 = 10**(t-1)
    if t == 0:
        pow10 = 0
    Pow10 = 10**t
    offsetL = 0
    offsetU = Pow10
    fl = lB[1]
    fu = lB[1]
    lLim = 0
    if flag:
        lLim = 1
    for i in range(lLim, 10):
        fl = fu
        if i == d:
            pStemdig = 1
            fu += (stemDigs+1)*Pow10 + pow10*t
        else:
            pStemdig = 0
            fu += stemDigs*Pow10 + pow10*t
        ans += RecSolFinder(d, t-1, [lB[0]+offsetL, fl], [lB[0]+offsetU, fu], stemDigs+pStemdig)
        offsetL = offsetU
        offsetU += Pow10
    return ans

ans = 0
for i in range(1, 10):
    ans += s(i)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")