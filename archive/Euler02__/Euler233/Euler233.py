#code completed on 2023/11/01
#How many numbers have a given factorization below a certain threshold
#Use the fact that f(N) = 4 + 4prod(1+2*ai) where ai are exponends of primes =1mod4
#Runs in 9.68 seconds

import time
import math
from ...CL.CL_Partitions import Partition_Generate
start = time.time()

MAX = 10**11
MAXsr = math.floor(math.sqrt(MAX))
maxsieve = MAXsr*45 #I dont know why this works but we need to compute all the primes up to this mark

#Sieve primes
primeQ = [True for _ in range(maxsieve+1)]
primeQ[0] = False
primeQ[1] = False
for i in range(4, maxsieve+1, 2):
    primeQ[i] = False
for i in range(3, maxsieve+1, 2):
    if primeQ[i]:
        for j in range(i*i, maxsieve+1, i):
            primeQ[j] = False

primesPit = []
for i in range(5, maxsieve+1, 4):
    if primeQ[i]:
        primesPit.append(i)

def PrimeQ(p):
    if p <= maxsieve:
        return primeQ[p]
    if p%2 == 0:
        return p == 2
    if p > MAX:
        raise Exception("Sieve more stuff to compute primeQ of ", p)
    for i in range(3, math.floor(math.sqrt(p)), 2):
        if primeQ[i]:
            if p%i == 0:
                return p == i
    return True

def PitPrimeProd(part):#The smallest number N with the given factorization
    prd = 1
    l = len(part)
    spart = sorted(part)
    for ind, i in enumerate(spart):
        prd *= primesPit[l-ind-1]**i
    return prd


largest_part = math.floor(math.log(MAX)/math.log(5))
parts = Partition_Generate(largest_part)
partitions = []
for part_list in parts:
    for part in part_list:
        if PitPrimeProd(part) <= MAX:
            partitions.append(part[:])
# partitions contains all the partitions of interest. There are 181 such partitions
#For each partition it corresponds a value of f, so we have to find the ones that correspond to 420
#We need some numerology to figure out this value

psi = {}
def f(perm):
    ans = 1
    for i in perm:
        ans *= 1+2*i
    return 4+4*(ans - 1)

imp_partitions = []
for p in partitions:
    if f(p) == 420:
        imp_partitions.append(p)
#imp_partitions holds all the important partitions

maxNonPitPrime = 0
for p in imp_partitions:
    maxNonPitPrime = max(MAX//PitPrimeProd(p), maxNonPitPrime)

#if(maxNonPitPrime > maxsieve):
#    print("We are not considering non-pitagoras primes above ", maxsieve, " which may also contribute for the computations.")
#Its not so simple and I dont know exactly
isNonPitFactorized = [True for _ in range(maxNonPitPrime+1)]
for p in primesPit:
    for i in range(p, maxNonPitPrime+1, p):
        isNonPitFactorized[i] = False

cumulNonPitFactorized = [0 for _ in range(maxNonPitPrime+1)]
for i in range(1, maxNonPitPrime+1):
    cumulNonPitFactorized[i] = cumulNonPitFactorized[i-1]
    if isNonPitFactorized[i]:
        cumulNonPitFactorized[i] += 1

#This gives us, for and index i the number of all integers N<=i that are not divided by a prime = 1 mod 4

cumulSumNonPitFactorized = [0 for _ in range(maxNonPitPrime+1)]
for i in range(1, maxNonPitPrime+1):
    cumulSumNonPitFactorized[i] = cumulSumNonPitFactorized[i-1]
    if isNonPitFactorized[i]:
        cumulSumNonPitFactorized[i] += i

#This gives us, for and index i the sum of all integers N<=i that are not divided by a prime = 1 mod4

def factors(part, M, minPrimeIndex = -1):
    #Gives the list of all numbers N <= M with factors in primesPit following list p
    if( M == 0 ):
        return []
    if( part == [] ):
        return [1]
    list_ans = []
    for index, pexp in enumerate(part):
        npart = part[:index] + part[index+1:]
        for primeIndex in range(minPrimeIndex+1, len(primesPit)):
            p = primesPit[primeIndex]**pexp
            if p > M:
                break
            list_ans +=[N*p for N in factors(npart, M//p, primeIndex)]
    list_ans.sort()
    return list_ans

#For each partition, find all numbers N<= MAX that factor into pitagoras primes with this partition
#for each of these numbers, contribute to ans with N*cumulSumNonPitFactorized[MAX//N]
ans = 0
for p in imp_partitions:
    for N in factors(p, MAX):
        ans += N*cumulSumNonPitFactorized[MAX//N]

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")