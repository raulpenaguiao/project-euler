import time
start = time.time()
ans = 0

import math

def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]


def ExtractPeriod(arrayVals):
    if arrayVals == []:
        return [], []
    pointEndPeriod = len(arrayVals) - 1
    pointBegPeriod = len(arrayVals) - 2
    while pointBegPeriod >= 0 and not(arrayVals[pointBegPeriod] == arrayVals[pointEndPeriod]):
        pointBegPeriod -= 1
    if pointBegPeriod == -1:
        return arrayVals, []
    while pointBegPeriod > 0 and arrayVals[pointBegPeriod-1] == arrayVals[pointEndPeriod-1]:
        pointBegPeriod -= 1
        pointEndPeriod -= 1
    return arrayVals[:pointBegPeriod], arrayVals[pointBegPeriod:pointEndPeriod]

def PeriodSums_ineff(period, N):
    periodLen = len(period)
    periodSum = sum(period)
    p = [0 for _ in range(periodSum)]
    p[0] = 1
    for i in range(periodLen):
        currSum = 0
        for j in range(periodLen - 1):
            currSum += period[(i+j)%periodLen]
            if 0 < currSum < periodSum and p[currSum] == 0:
                p[currSum] = i + 1
    ans = 0
    for i in range(1, N+1):
        ans += p[i%periodSum]
    print("Answer is ", ans)
    print(sum(p[:N%periodSum+1]))
    print(sum(p))
    print( p[0])
    return sum(p)*(N//periodSum) + sum(p[1:N%periodSum+1])


def PeriodSums(period, N):
    print(not(period[-1] == 0))
    periodSum = sum(period)
    periodLen = len(period)

    p = set()
    totSum = 0
    partSum = 0
    lim = N%periodSum

    for i in range(periodLen):
        if period[(i-1)%periodLen] == 0:
            continue
        currSum = 0
        for j in range(periodLen-1):
            currSum += period[(j+i)%periodLen]
            if not currSum in p and 0 < currSum < periodSum:
                p.add(currSum)
                totSum += i + 1
                if 0 < currSum <= lim:
                    partSum += i + 1
        k = len(p)
        #print("Until index ", i, " the total number of impossible sums is ", periodSum - k - 1,  " in ", periodSum , " - current sum of p is ", totSum, " and partial sum is ", partSum)
        if k == periodSum - 1:
            print("All indices are found")
            break
    return (totSum + 1)*(N//periodSum) + partSum


s = [14025256]
pow2 = 2**1
while not s[-1] in s[:-1]:
    for _ in range(pow2):
        s.append((s[-1]**2)%20300713)
    pow2 *= 2

mantissaS, periodS = ExtractPeriod(s)
mantissa = []
period = []
for m in mantissaS:
    mantissa += digits(m)
for p in periodS:
    period += digits(p)
#print(sum(mantissa) == 0) #Assume there is no mantissa
#print(period[-1] == 0)#assume that the last term is non-zero
smallArray = [5 + math.floor(math.sin(i)*5) for i in range(103)]
print(PeriodSums(smallArray, 10**3))
print(PeriodSums_ineff(smallArray, 10**3))


#print("Answer = ", PeriodSums(period, 10**15))
end = time.time()
print("Time elapsed ", end - start, " seconds")