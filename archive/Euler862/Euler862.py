import time
start = time.time()
from ...CL.CL_Partitions import Partition_Generate

LIM = 100
binom = [[0 for _ in range(LIM+1)] for _ in range(LIM+1)]
for i in range(LIM+1):
    binom[i][0] = 1
    binom[i][i] = 1
for n in range(1, LIM+1):
    for k in range(1, n):
        binom[n][k] = binom[n-1][k] + binom[n-1][k-1]
#print([[binom[i][j] for j in range(i+1)] for i in range(10)])

factorials = [1 for _ in range(LIM + 1)]
for i in range(1, LIM + 1):
    factorials[i] = factorials[i-1]*i
#print(factorials[:10])

def Mbinom(n, block):
    top = n
    ans = 1
    for b in block:
        ans *= binom[top][b]
        top -= b
    return ans
#print(Mbinom(5, [1, 2, 2]), " vs ", 30)

def Assign(buckets, parts):
    p = parts[:]
    p.sort()
    l = len(p)
    ans = 1
    counter = 1
    top = buckets
    for i in range(1, l):
        if not p[i] == p[i-1]:
            #print(top, counter)
            ans *= binom[top][counter]
            top -= counter
            counter = 1
        else:
            counter += 1
    #print(top, counter, l)
    return ans*binom[top][counter]
#print(Assign(5, [1, 2, 2]), " vs ", 30)

def S(K):
    ans = 0
    parts = Partition_Generate(K)
    for zeroParts in range(K+1):
        for part in parts[K-zeroParts]:
            #Find the size of the cycle generated
            #For instance if we have [1;2,1] this generates 9 numbers: 1120, 1210, 2110, 1102, 1201, 2101, 1012, 1021, 2011
            #This seems to be binom(n; a_0, ..., a_k) - binom(n-1; a_0-1, ..., a_k) (the second term is zero if a_0 = 0)
            #In the case above we have binom(4; 1, 2, 1) - binom(0; 0, 2, 1) = binom(4, 1) binom(3, 2) binom(1, 1) -  binom(3, 0) binom(3, 2) binom(1, 1) = 4*3*1 - 1*3*1 = 9
            cycleSize = Mbinom(K, [zeroParts] + part)
            if zeroParts > 0:
                cycleSize -= Mbinom(K-1, [zeroParts-1] + part)
            #Find the number of integers with this signature, divided by the number of cycles
            #That is, assign for each element of the partition a number
            #Careful that you should not distinguish between assignments of elements with matching sizes
            #For instance, [1;2, 2]  has the similar looking element matches 1 -> 0, 2 -> 1, 2-> 2 and 1 -> 0, 2 -> 2, 2-> 1
            signedNumbers = Assign(9, part)
            #print(" [ ", zeroParts, " ; ", part, " ] - " , signedNumbers, cycleSize, cycleSize*(cycleSize - 1)*signedNumbers//2)
            ans += cycleSize*(cycleSize - 1)*signedNumbers//2
    return ans

print("Answer = ", S(12))
end = time.time()
print("Time elapsed ", end - start, " seconds")