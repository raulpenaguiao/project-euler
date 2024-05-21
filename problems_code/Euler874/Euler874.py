#Code written on the 2024/05/21
#Uses the Knapsack algorithm on the list [6999 - ai ,i from 1 to n]
#This allows us to search for the list with sum k by adding the best list with sum k-j with a term [j]
#Assumes that $n>k$
#Runs in 

import time
start = time.time()
ans = 0

from ...CL.CL_Primes import Primes

primes = Primes(7000*13)

def Score(indexList, max):
    ans = 0
    for i in indexList:
        ans += primes[max] - primes[max - i]
    #print("Computing the score of ", indexList,  " gives ", ans)
    return ans

def M(k, n):
    """
    
    This function assumes that n > k, or at least n > toDistribute
    """
    tot = n*(k-1)
    toDistribute = k - 1 - (tot - 1)%k
    knapsack = [[[], 0]]
    for i in range(1, toDistribute+1):
        bestChoice = [1] + knapsack[-1][0][:]
        score = Score(bestChoice, k-1)
        bestScore = score
        for j in range(2, i+1):
            currentChoice = [j] + knapsack[-j][0][:]
            score = primes[k-1] - primes[k-1 - j] + knapsack[-j][1]
            if score < bestScore:
                currentChoice.sort()
                bestChoice = currentChoice[:]
                bestScore = score
        bestChoice.sort()
        knapsack += [[bestChoice[:], score]]
    print(knapsack[-1])
    return sum([primes[k-1-i] for i in knapsack[-1][0]]) + primes[k-1] * (n - len(knapsack[-1][0]))


L = 7000
ans = M(L, primes[L])
print([primes[L-659] - primes[L-i-659] for i in range(10)])
#ans = M(7000, primes[7000])
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")