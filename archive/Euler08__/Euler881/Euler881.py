# Code written on the 2024/05/23
# Uses characterization of divisor lattice as a product of intervals
# Assumes that best partition sits inside a 16x8 square, because 8 already seems large enough
# And 16 was shown to be the best because the product of the first 16 primes already satisfies the desired condition
# Runs in 0.2 seconds


import time
start = time.time()
ans = 0

from ...CL.CL_Primes import Primes, PrimeFactorization

primes = Primes(1000)

def n(part):
    """
    
    Assumes partition is already sorted
    """
    ans = 1
    l = len(part)
    for i in range(l):
        ans *= primes[i]**part[l-1-i]
    return ans

def g(part):
    return max(g_vec(part))


def convolution_product(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    ans = [0 for _ in range(len1 + len2 - 1)]
    for i in range(len1):
        for j in range(len2):
            ans[i+j] += l1[i]*l2[j]
    return ans

def g_vec(part):
    if len(part) == 0:
        return [1]
    ans = [1]*(part[0]+1)
    for i in range(1, len(part)):
        ans = convolution_product(ans, [1]*(part[i]+1))
    return  ans


def FindSmalestPart(a, b, LIM):
    if a == 0 or b == 0:
        return [[]]
    ans = [ ]
    partitionList = [[] for _ in range(a*b+1)]
    partitionList[1].append([1])
    partitionList[0].append([])
    for i in range(2, a*b+1):
        for part in partitionList[i-1]:
            if g(part) >= LIM:
                ans.append(n(part))
                continue
            if part[0] < b and (len(part) == 1 or part[1] > part[0]):
                newPart = part[:]
                newPart[0] += 1
                partitionList[i] += [newPart[:]]
            if len(part) < a:
                newPart = part[:]
                newPart = [1] + newPart
                partitionList[i] += [newPart[:]]
    return min(ans)

def GeneratePartitionsInSquare(a, b, LIM):
    if a == 0 or b == 0:
        return [[]]
    partitionList = [[] for _ in range(a*b+1)]
    partitionList[1].append([1])
    partitionList[0].append([])
    for i in range(2, a*b+1):
        for part in partitionList[i-1]:
            if g(part) > LIM:
                #print(n(part))
                continue
            if part[0] < b and (len(part) == 1 or part[1] > part[0]):
                newPart = part[:]
                newPart[0] += 1
                partitionList[i] += [newPart[:]]
            if len(part) < a:
                newPart = part[:]
                newPart = [1] + newPart
                partitionList[i] += [newPart[:]]
    return partitionList

LIM = 10000
nVal = FindSmalestPart(16, 8, LIM)

print("Answer = ", nVal)
print("Answer = ", PrimeFactorization(nVal, primes))
end = time.time()
print("Time elapsed ", end - start, " seconds")