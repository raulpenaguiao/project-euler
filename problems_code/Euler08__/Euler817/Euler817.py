import math

def digits(n, base = 10):
    if(n < base):
        return [n]
    return digits(n//base, base) + [n%base]


def factors(n):
    k = n
    ans = []
    if (k%2 == 0):
        k = n//2
        count = 1
        while(k%2 == 0):
            count += 1
            k //= 2
        ans += [[count, 2]]
    iterPrime = 3
    while(iterPrime**2 <= k):
        if(primeQ[iterPrime]):
            if(k%iterPrime == 0):
                count = 1
                k //= iterPrime
                while(k%iterPrime == 0):
                    k //= iterPrime
                    count += 1
                ans += [[count, iterPrime]]
        iterPrime += 2
    if (k > 1):
        ans += [[1, k]]
    return ans

def sign(n):
    if (n%2 == 1):
        return -1
    return 1

def LegSymbol(d, p):#We require p to be prime!
    if(d > p):
        return LegSymbol(d%p, p)
    if(p == 2):
        return d
    if (d%p == 0):
        return 0
    ans = 1
    for a, b in factors(d):
        if a%2 == 1:
            if b > 2:
                ans *= LegSymbol(p, b)* sign((p-1)*(b-1)//4)
            else:
                ans *= sign((p*p-1)//8)
    return ans


def sqrtMod(d, n):###TODOTODO
    return d

def M(n, d):#We assume that n is prime and d < n
    ls = LegSymbol(d, n)
    if (ls == 1):
        return sqrtMod(d, n)
    a = (d)*n
    b = (d+1)*n
    while(True):
        if(math.sqrt(a) < math.floor(math.sqrt(b))):
            #We found the interval!
            i = math.ceil(math.sqrt(a))
            # I need to find some i that is above this guy whose square has d
            while(((i*i)%n)//n%n != d):
                i += 1
            return i
        a += n*n
        b += n*n
        

LIM = 100000
primeQ = [False, True]*(LIM//2)
primeQ[2] = True
primeQ[1] = False
for i in range(3, LIM, 2):
    if(primeQ[i]):
        for j in range(i*i, LIM, i):
            primeQ[j] = False

for i in range(1, 20):
    print(i, " - " , LegSymbol(i, 11))
"""
p = 10009
D = 1000
for i in range(p-D, p):
    t = M(p, i)
    if (t > 3*p):
        print("i = ", i, " M(p, i) = ", t)"""