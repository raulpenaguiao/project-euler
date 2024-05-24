# Code written on the 2024/05/24
# Generates all numbers of up to 18 digits using digits from 0 to 9 in a sorted manner
# These are just partitions of lenght at most 18 with parts <= 9, and there are about $\binom{18+9}{18} \sim 5 \cdot 10^6$
# For each such number $d$, count how many numbers of at most 18 digits will be mapped to $d$ after reordering
# This is a simple factorial product
# Runs in 28.26 seconds


import time
start = time.time()
ans = 0
n = 18



fact = [1 for _ in range(n+1)]
for i in range(1, n+1):
    fact[i] = fact[i-1]*i

def DeleteCopies(lst):
    if lst == []:
        return []
    ans = [lst[0]]
    for i in range(1, len(lst)):
        if not(lst[i] == lst[i-1]):
            ans.append(lst[i])
    return ans


def Count(item, lst):
    ans = 0
    for i in lst:
        if i == item:
            ans += 1
    return ans

def CountOccurrences(lst):
    dclst = DeleteCopies(lst)
    return [Count(item, lst) for item in dclst]


def GeneratePartitionsInSquare(a, b):
    if a == 0 or b == 0:
        return []
    partitionList = [[] for _ in range(a*b+1)]
    partitionList[1].append([1])
    partitionList[0].append([])
    for i in range(2, a*b+1):
        for part in partitionList[i-1]:
            if part[0] < b and (len(part) == 1 or part[1] > part[0]):
                newPart = part[:]
                newPart[0] += 1
                partitionList[i] += [newPart[:]]
            if len(part) < a:
                newPart = part[:]
                newPart = [1] + newPart
                partitionList[i] += [newPart[:]]
    return partitionList


def Prod(lst):
    ans = 1
    for item in lst:
        ans *= item
    return ans


def NumbersToPart(part, size):
    zeroes = size - len(part)
    if zeroes < 0:
        return 0
    occs = CountOccurrences(part) + [zeroes]
    return fact[n]//Prod([fact[i] for i in occs])


def ToInt(lst):
    if lst == []:
        return 0
    return 10*ToInt(lst[:-1]) + lst[-1]

MOD = 1123455689
parts = GeneratePartitionsInSquare(n, 9)[1:]
for parts_indexed in parts:
    for part in parts_indexed:
        ans += NumbersToPart(part, n)*ToInt(part)
        ans %= MOD

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")