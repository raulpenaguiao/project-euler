# Code written on the 2024/09/24
# dynamic programming in stages corresponding to the three different operations (concatenation, product, sum)
# Runs in two days
# After an optimization of putting numbers in different buckets according to the value in the product, 
#and just analyzing thoes sums that have bounded sum, we are able to bring it down to 152.14 seconds.


#The code runs in three steps.
#First we compute the number of matchsticks required for creating a number.
#This part takes O(N)
#Then we compute the number of matchsticks required for creating a number using products
#This part takes O(N + N*log(N)/2)
#Then we compute the number of matchsticks required for creating a number using products and sums
#This part takes too long... O(N^2) We need to improve this.

import time
start = time.time()
N = 10**6#maxvalue

def countMatches(str):
    return sum([numberMatchsticks[c] for c in str])

#Loop over all strings of a given size.
matchsticks = "0123456789"
numberMatchsticks = {"0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}
bestValuesNumber = [countMatches(str(i)) for i in range(N+1)]

#product phase
bestValuesNumberProduct = [bestValuesNumber[i] for i in range(N+1)]
for a in range(1, N+1):
    for b in range(1, min(N//a, a)+1):
        bestValuesNumberProduct[a*b] = min(bestValuesNumberProduct[a*b], bestValuesNumberProduct[a] + bestValuesNumberProduct[b] + 2)

#sum phase
bestValuesNumberProductSum = [bestValuesNumberProduct[i] for i in range(N+1)]
maxValue = max(bestValuesNumberProduct)
vis = {}

for i in range(1, N+1):
    if bestValuesNumberProduct[i] in vis:
        vis[bestValuesNumberProduct[i]] += [i]
    else:
        vis[bestValuesNumberProduct[i]] = [i]

visKeys = [i for i in vis]
visKeys.sort()
l = len(visKeys)

for isum in range(l):
    for i1 in range(isum):
        k1 = visKeys[i1]
        i2 = isum - i1
        k2 = visKeys[i2]
        #print(k1, k2, len(vis[k1]) * len(vis[k2]))
        if k1+k2 + 2 >= maxValue:
            continue
        for a in vis[k1]:
            for b in vis[k2]:
                if a+b > N:
                    break
                #print(a, b, N, a+b, N, a+b <= N, len(bestValuesNumberProductSum))
                nBV = bestValuesNumberProductSum[a] + bestValuesNumberProductSum[b] + 2
                if nBV < bestValuesNumberProductSum[a + b]:
                    bestValuesNumberProductSum[a + b] = nBV
                #bestValuesNumberProductSum[a + b] = min(bestValuesNumberProductSum[a + b], bestValuesNumberProductSum[a] + bestValuesNumberProductSum[b] + 2)

print("Answer = ", sum(bestValuesNumberProductSum[1:]))
end = time.time()
print("Time elapsed ", end - start, " seconds")