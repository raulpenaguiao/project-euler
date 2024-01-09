import math
from .CL_Arithmetics import PowerMod

def Primes(N):
    Nsqrt = math.floor(math.sqrt(N))+2
    primes = [2]
    sieve = [True for _ in range(Nsqrt)]
    for i in range(4, Nsqrt, 2):
        sieve[i] = False
    for p in range(3, Nsqrt, 2):
        if sieve[p]:
            primes.append(p)
            for j in range(p*p, Nsqrt, p):
                sieve[j] = False
    for p in range(Nsqrt-Nsqrt%2+1, N+1):
        flag = True
        i = 0
        q = primes[i]
        while(flag and q*q<= p):
            if p%q == 0:
                flag = False
            i += 1
            q = primes[i]
        if flag:
            primes.append(p)
    return primes

def PrimeFactorization(n, primes):
    m = n
    i = 0
    ans = []
    while(m > 1 and len(primes) > i):
        if m%primes[i] == 0:
            exp = 1
            m //= primes[i]
            while(m%primes[i] == 0):
                m //= primes[i]
                exp += 1
            ans.append([primes[i], exp])
        i += 1
    if m > 1 and len(primes) == i:
        if primes[i-2]**2 > m:
            ans.append([m, 1])
        else:
            raise Exception("Not enough primes computed")
    return ans

#print(PrimeFactorization(4, [2, 3, 5, 7]), " = [[2, 2]]")
#print(PrimeFactorization(12, [2, 3, 5, 7]), " = [[2, 2], [3, 1]]")
#print(PrimeFactorization(30, [2, 3, 5, 7]), " = [[2, 1], [3, 1], [5, 1]]")
#print("Prime factorisation ", PrimeFactorization(22, [2, 3, 5, 7]), " = [[2, 1], [11, 1]]")

def EulerPhi(N):
    phi = [i-1 for i in range(N+1)]
    phi[0] = 0
    phi[1] = 1
    for k in range(2, N):
        for j in range(2*k, N+1, k):
            phi[j] -= phi[k]
    return phi


def Divisors_FC(fc):
    if fc == []:
        return [1]
    p = fc[0][0]
    exp = fc[0][1]
    powList = [1]
    ans = []
    for _ in range(exp):
        powList.append(powList[-1]*p)
    for d in Divisors_FC(fc[1:]):
        for power in powList:
            ans.append(d*power)
    return ans

def Divisors(n, primes):
    fc = PrimeFactorization(n, primes)
    return Divisors_FC(fc)


def MRTest(n, r, verbose = False):
    d = n-1
    e = 0
    while (d%2 == 0):
        d //= 2
        e += 1
    a = PowerMod(r, d, n)
    if (a == 1):
        #if verbose:
        #    print("Power is already one")
        return True
    b = (a*a)%n
    while not(b == 1) and e > 0:
        a = b
        b = (a*a)%n
        e -= 1
    #if verbose:
    #    print("e = ", e, ", a = ", a, ", n = ", n)
    return (e > 0 )and (a+1 == n)


def MillerRabin(n, verbose = False):
    if n == 0 or n == 1:
        return False
    if n < 0:
        return MillerRabin(-n)
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    if n % 7 == 0:
        return n == 7
    if n % 11 == 0:
        return n == 11
    if n % 13 == 0:
        return n == 13
    #if verbose:
    #    print(n, " has survived to the easy divisibility tests.")
    if not MRTest(n, 2, verbose):
        return False
    #if verbose:
    #    print(n, " has survived test 2.")
    if n < 2_047:
        return True
    if not MRTest(n, 3, verbose):
        return False
    #if verbose:
    #    print(n, " has survived test 3.")
    if n < 1_373_653:
        return True
    if not MRTest(n, 5, verbose):
        return False
    if n < 25_326_001:
        return True
    if not MRTest(n, 7, verbose):
        return False
    if n < 3_215_031_751:
        return True
    if not MRTest(n, 11, verbose):
        return False
    if n < 2_152_302_898_747:
        return True
    if not MRTest(n, 13, verbose):
        return False
    if n < 3474749660383:
        return True
    if not MRTest(n, 17, verbose):
        return False
    if n < 341550071728321:
        return True
    if not MRTest(n, 19, verbose) or not MRTest(n, 23, verbose):
        return False
    if n < 3_825_123_056_546_413_051:
        return True
    if not MRTest(n, 29, verbose) or not MRTest(n, 31, verbose) or not MRTest(n, 37, verbose):
        return False
    if n < 18_446_744_073_709_551_616:
        return True
