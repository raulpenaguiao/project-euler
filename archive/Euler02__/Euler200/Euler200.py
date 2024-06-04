#Code written in 2023/12/06
#Fix arbitrary upper bound, 10**12 works
#Uses Miller Rabin to check primality (helped me find a bug!)
#Uses sieve up to square root (upper bound/8), dont do square root (upper bound)/8.
#Prime-proof and contaning contiguous substring is naive algorithm
#make sure to generate squbes by using only primes with the right size, created two lists for the effect. Break when you are already above cuts 75% of time
#Runs in 0.302422 seconds


import time
start = time.time()
import math
from ...CL.CL_Primes import MillerRabin, Primes
ans = 0



def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base)+[n%base]


def ToInteger(lst):
    if lst == []:
        return 0
    return int("".join([str(a) for a in lst]))

#print(ToInteger([2, 4, 3]))#243
#print(ToInteger([0]))#0
#print(ToInteger([2, 3]))#23


def IsPrimeProof(dgs):
    l = len(dgs)
    for i in range(l):
        for d in range(10):
            if (not d == dgs[i]) and (i > 0 or d > 0):
                a = dgs[i]
                dgs[i] = d
                if MillerRabin(ToInteger(dgs)):
                    return False
                dgs[i] = a
    return True


#print(IsPrimeProof(digits(200)))#True
#print(IsPrimeProof(digits(1992008)))#True
#print(IsPrimeProof(digits(1999)))#False maybe

def ContainsSubstring(lst, sbs):
    l = len(lst)
    m = len(sbs)
    for i in range(l-m+1):
        j = 0
        while(j < m and lst[i+j] == sbs[j]):
            j += 1
        if j == m:
            return True
    return False

#print(ContainsSubstring([1, 4, 2, 3, 5, 3, 4, 2, 0, 0, 2, 3, 1, 4], [2, 0, 0]))#True
#print(ContainsSubstring([1, 4, 2, 3, 5, 3, 4, 2, 0, 2, 3, 1, 4], [2, 0, 0]))#False
#print(ContainsSubstring([1, 4, 2, 3, 5, 3, 4, 2, 0, 0], [2, 0, 0]))#True


def IsPrimeProofAndContains200(n):
    d = digits(n)
    return ContainsSubstring(d, [2, 0, 0]) and IsPrimeProof(d)

LIM = 10**12
LIMP = math.floor(math.sqrt(LIM+2))
primes = Primes(math.floor(LIMP/math.sqrt(8)))
primesC = [p for p in primes if p*p*p*4 <= LIM]
primesS = [p for p in primes if p*p*8 <= LIM]
end = time.time()
print("Primes computed. Time elapsed ", end - start, " seconds")
squbes = []
for p in primesC:
    b = p*p*p
    for q in primesS:
        if not p == q:
            a = b*q*q
            if a <= LIM:
                squbes.append(a)
            else:
                break

end = time.time()
print("Squbes computed, there are ", len(squbes), " squbes. Time elapsed ", end - start, " seconds")
squbes.sort()
counter = 0
found = False
ppsw200 = []
for s in squbes:
    if IsPrimeProofAndContains200(s):
        counter += 1
        ppsw200.append(s)
        if counter == 200:
            print("Answer = ", s)
            found = True
            break
if not found:
    print("Only ", counter, " prime-proof squbes containing 200 found.")
#print("All squbes found: ", ppsw200)
end = time.time()
print("Time elapsed ", end - start, " seconds")