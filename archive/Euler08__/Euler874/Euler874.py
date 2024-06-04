#Code written on the 2024/05/21
#Uses the Knapsack algorithm on the list [6999 - ai ,i from 1 to n]
#This allows us to search for the list with sum k by adding the best list with sum k-j with a term [j]
#Assumes that $n>k$
#Runs in 1.084 seconds

import time
start = time.time()
ans = 0

from ...CL.CL_Primes import Primes
from math import ceil

primes = Primes(7000*13)

def Knapsack(bagSize, listItems):
    """classic knapsack algorithm 
    with infinitely many items of each kind
    you have to fill the bag up completely
    allows for negative values
    assumes listItems are sorted with increasing item volume
    
    Input:
     - bagSize: an integer
     - listItems: a collection of items
        Each item is a pair of integers [vol, val], where vol is the volume and val is the value of the item
    
    Output:
     - ans: the maximal value of the items that fit in the bag
    """
    INF = sum([ceil(abs(item_val*bagSize/item_vol)) for item_vol, item_val in listItems])
    bestKnapSackScore = [[-INF, []] for _ in range(bagSize+1)]
    bestKnapSackScore[0] = [0, []]
    for i in range(1, 1+bagSize):
        for item_vol, item_val in listItems:
            if item_vol <= i:
                score = bestKnapSackScore[i-item_vol][0] + item_val
                if bestKnapSackScore[i][0] < score:
                    bestKnapSackScore[i][0] = score
                    bestKnapSackScore[i][1] = bestKnapSackScore[i-item_vol][1] + [[item_vol, item_val]]
            else:
                break
    return bestKnapSackScore[bagSize]

def M(k, n):
    """
    This function assumes that n > k, or at least n > toDistribute
    """
    toDistribute = (n*(k-1))%k
    kp = Knapsack(toDistribute, [[i, primes[k-1-i] - primes[k-1]] for i in range(1, 1+k)])
    return n*(primes[k-1]) + kp[0]

L = 7000
ans = M(L, primes[L])
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")