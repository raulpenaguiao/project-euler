# Code written on the 2024/01/04
# First generate all possible decreasing lists of ten integers that sum to 70
# For each such list, we can place them in any of the 20 positions (divide by suitable binomial coef)
# Careful that there may be some copies of the lowest term of this list in the other positions, so take care of that in the combinatorics
# Precompute factorials
# Function "PermutationOfLists" gives the number of different lists that are permutations of a given list
# Function "ExtentionPermutations" computes, for a given list, the number of ways of filling out all 20 positions with this list and weakly lower numbers
# Possible improvements:
# - Precompute binomials
# Code runs in 0.582 seconds



import time
start = time.time()
ans = 0

diceSize = 12
bigNumDices = 10
totNumDices = 20
totSum = 70

factorial = [1 for i in range(25)]
for i in range(1, 25):
    factorial[i] = factorial[i-1]*i

def Binom(n, k):
    return factorial[n]//(factorial[k]*factorial[n-k])


def PermutationsOfList(list):
    if list == []:
        return 1
    a = list[:]
    l = len(a)
    ans = factorial[l]
    noCopies = [a[0]]
    for i in range(1, l):
        if not a[i] == a[i-1]:
            noCopies.append(a[i])
    for c in noCopies:
        countCopies = a.count(c)
        ans //= factorial[countCopies]
    return ans

#Unit testing this function
if not PermutationsOfList([1, 2, 3]) == 6:
    print("AAAH")
if not PermutationsOfList([1, 2, 2]) == 3:
    print("AA")
if not PermutationsOfList([2, 2, 2]) == 1:
    print("AA")
if not PermutationsOfList([12, 8, 7, 7, 6, 6, 6, 6, 6, 6]) == 2520:
    print("AAA")


def ExtentionsPermutation(lst, val):
    ans = 0
    m = min(lst)
    lm = lst.count(m)
    l = len(lst)
    for k in range(val - l+1):
        ans += (m-1)**(val - l - k) * PermutationsOfList(lst + [m]*k + [0]*(val - l - k) )
    return ans

P = [[[[] for _ in range(diceSize + 2)] for _ in range(totSum + 1)] for _ in range(bigNumDices + 1)]
for l in range(1, diceSize + 1):
    for s in range(l, totSum + 1):
        if s > diceSize:
            break
        P[1][s][l] = [[s]]
for n in range(2, bigNumDices + 1):
    for s in range(1, totSum + 1):
        for l in range(1, diceSize + 1):
            for i in range(l, diceSize + 1):
                if i <= s:
                    for part in P[n-1][s-i][i]:
                        P[n][s][l].append(part + [i])

parts = P[bigNumDices][totSum][1]
for p in parts:
    ans += ExtentionsPermutation(p, totNumDices)


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")