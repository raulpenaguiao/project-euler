#Code written on the 2024/01/11
#This function finds all the numbers $n$ that have $\phi(n)$
#Uses the fact that if $\phi(n) = N$, then $\prod_i \phi(p_i^{a_i}) = N$ is a factorisation of $N$
#So we generate all factorisations of $N$ and for each factor we find all the ways of writting it as $\phi(p_i^{a_i})$ for some prime $p_i$ (called Euler decs).
#An optimization implemented is that we only generate factorisations using factors that do accept some called Euler dec.
#Do not forget that $1$ can also be a factor in the factorisation. We only need to include this factor once because there is only one Euler dec that interests us.
#Function DCPPrime
#   Computes how many ways we can write a number $k$ as phi of a prime number. That is $k = p^a - p^{a-1}$
#   The case $p = 2$ has to be dealt separately
#   For each possible exponent $a$ we know $p$ is close and larger than $\sqrt[a]{k}$. We hope it's precisely the ceiling
#   We use Miller Rabin for primality test
#Function Product Partitions
#   Computes all factorisations, different ways of writting a number $N$ as a product of different numbers
#   It accepts a dictionary, and we will ignore all factors that are keys in this dictionary
#Function AllAreDistinct, DeleteCopies, CartesianProduct manipulate lists
#Function FromPrimeFactToNum converts a prime factorisation into the number it represents
#   Example [[2, 3], [3, 1]] -> 24
#Function ListNumPhiIsN is the meat of the code. For an input $N$ creates all numbers $n$ such that $\phi(n) = N$.
#   For each possible factorisation where each factor can be written
#Runs in 12.88 seconds


import time
start = time.time()
from ...CL.CL_Primes import MillerRabin, Divisors, Primes
import math


def DCPPrime(k, verbose = False):
    a = 1
    p = k+1
    lk = math.log(k)
    ans = []
    while(p > 2):
        p = math.ceil(p)
        if (p**(a-1)*(p-1)) == k and MillerRabin(p):
            ans.append([p, a])
        a += 1
        p = math.exp( lk/a)
    #Check if two works. That is, is k a power of 2?
    x = k
    a = 1
    while x%2 == 0:
        x//= 2
        a += 1
    if x == 1:
        ans.append([2, a])
    return ans
def ProductPartitions(N, primes, toIgnore = {}):
    divs = Divisors(N, primes)
    divs.sort()
    partits = {d: [] for d in divs}
    partits[1] = [[], [1]]
    #print(partits)
    numdivs = len(divs)
    for i in range(1, numdivs):
        di = divs[i]
        if not di in toIgnore:
            partits[di].append([di])
        for j in range(i):
            dj = divs[j]
            #print(di, dj)
            if di%dj == 0:
                nfac = di//dj
                #print("new factors added", nfac, partits[dj])
                if not nfac in toIgnore:
                    for p in partits[dj]:
                        if p == [] or nfac >= max(p):
                            partits[di].append([nfac] + p)
                #print("new factors added", nfac, partits[di])
        #print(di, " __", partits[di])
    return partits[divs[-1]]
def AllAreDistinct(lst):
    lst.sort()
    l = len(lst)
    for i in range(1, l):
        if lst[i] == lst[i-1]:
            return False
    return True
def DeleteCopies(lst):
    if lst == []:
        return []
    ls = lst[:]
    ls.sort()
    l = len(ls)
    ans = [ls[0]]
    for i in range(1, l):
        if not ls[i] == ls[i-1]:
            ans.append(ls[i])
    return ans
def CartesianProduct(mat):
    if mat == []:
        return [[]]
    ans = []
    for ind in mat[0]:
        for pind in CartesianProduct(mat[1:]):
            ans.append([ind] + pind)
    return ans
def FromPrimeFactToNum(pf):
    if pf == []:
        return 1
    return FromPrimeFactToNum(pf[1:]) * (pf[0][0] ** pf[0][1])
def ListNumPhiIsN(N, primes):
    divs = Divisors(N, primes)
    listDCPP = {}
    toIgnore = {}
    for d in divs:
        listDCPP[d] = DCPPrime(d)
        if listDCPP[d] == []:
            toIgnore[d] = True
    pp = ProductPartitions(N, primes, toIgnore)
    lNumPhiIsN = []
    for par in pp:
        for i in CartesianProduct([listDCPP[p] for p in par]):
            prms = [p for p, a in i]
            prms.sort()
            if prms == []:
                print(i)
            if AllAreDistinct(prms):
                lNumPhiIsN.append(FromPrimeFactToNum(i))
    lNumPhiIsN.sort()
    return lNumPhiIsN

primes = Primes(100)
L = 1
for i in range(1, 1+13):
    L *= i

ls = ListNumPhiIsN(L, primes)
ls = DeleteCopies(ls)
print("Answer 150000th = ", ls[150_000-1])
end = time.time()
print("Time elapsed ", end - start, " seconds")