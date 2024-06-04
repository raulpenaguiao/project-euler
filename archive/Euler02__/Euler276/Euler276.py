#Code written on the 2023/11/28
#F(n) - F(n-1) = sum_{d|n} mu(n//d) G(d) according to OEIS A051493
#Runs in 19.13 seconds


import time
start = time.time()
from ...CL.CL_Primes import Primes


def G(n):#round(n^2/12) - floor(n/4)*floor((n+2)/4) 
    #return math.floor(n*n/12 + 0.5) - math.floor(n/4)*math.floor((n+2)/4)
    a = n%12
    if a < 6:
        if a < 3:
            if a < 1:
                #a == 0
                return n*n//12 - (n//4)*((n+2)//4)
            else:
                if a < 2:
                    #a == 1
                    return (n*n-1)//12 - (n//4)*((n+2)//4)
                else:
                    #a == 2
                    return (n*n-4)//12 - (n//4)*((n+2)//4)
        else:
            if a < 4:
                #a == 3
                return (n*n+3)//12 - (n//4)*((n+2)//4)
            else:
                if a < 5:
                    #a == 4
                    return (n*n-4)//12 - (n//4)*((n+2)//4)
                else:
                    #a == 5
                    return (n*n - 1)//12 - (n//4)*((n+2)//4)
    else:
        if a < 9:
            if a < 7:
                #a == 6
                return n*n//12 - (n//4)*((n+2)//4)
            else:
                if a < 8:
                    #a == 7
                    return (n*n - 1)//12 - (n//4)*((n+2)//4)
                else:
                    #a == 8
                    return (n*n - 4)//12 - (n//4)*((n+2)//4)
        else:
            if a < 10:
                #a == 9
                return (n*n + 3)//12 - (n//4)*((n+2)//4)
            else:
                if a < 11:
                    #a == 10
                    return (n*n - 4)//12 - (n//4)*((n+2)//4)
                else:
                    #a == 11
                    return (n*n - 1)//12 - (n//4)*((n+2)//4)


def F_eff(n):
    ans = 0
    for d in range(1, n+1):
        ans += G(d) * Cmu[n//d]
    return ans


N = 10**7
primes = Primes(N)
mu = [1 for _ in range(N+1)]
mu[1] = 1
mu[0] = 0
for p in primes:
    if p > N:
        break
    for i in range(p, N+1, p):
        mu[i] *= -1
    for i in range(p*p, N+1, p*p):
        mu[i] *= 0


Cmu = [1 for _ in range(N+1)]
Cmu[0] = 0
for i in range(1, N+1):
    Cmu[i] = Cmu[i-1] + mu[i]



print("Answer = ", F_eff(N))
end = time.time()
print("Time elapsed ", end - start, " seconds")

"""

def F_eff(N):
    primes = CP.Primes(N)
    mu = [1 for _ in range (N+1)]
    for p in primes:
        for i in range(p, N+1, p):
            mu[i] *= -1
        for i in range(p*p, N+1, p*p):
            mu[i] *= 0
    #Cumulative moebious
    Cmu = [0 for _ in range (N+1)]
    for i in range(1, N+1):
        Cmu[i] = Cmu[i-1] + mu[i]
    ans = 0
    for d in range(1, N+1):
        ans += (d+1)*(d+2)*Cmu[N//d]//2
    Phi = 0
    for d in range(1, N+1):
        g = N//d
        Phi += mu[d]*g*(g+1)//2
    return (3*Phi + ans+2)//6
"""

"""
#OEIS formula for the differences
def f(n):
    ans = 0
    primes = CP.Primes(n)
    mu = [1 for _ in range (N+1)]
    for p in primes:
        for i in range(p, N+1, p):
            mu[i] *= -1
        for i in range(p*p, N+1, p*p):
            mu[i] *= 0
    for d in CP.Divisors(n, primes):
        ans +=mu[n//d]*(d+1)*(d+2)//2
    return ans

print([f(n) for n in range(4, 15)])
print([F_eff(n) for n in range(4, 15)])"""

"""
#Naive function
def F(N):
    ans = 0
    for c in range(N+1):
        for b in range(N-c+1):
            d = CA.gcd(c, b)
            for a in range(N-c-b+1):
                if CA.gcd(a, d)==1:
                    ans += 1
    return ans
print("Naive answer = ", F(N))"""
