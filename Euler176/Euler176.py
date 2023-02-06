import time
import math

start_time = time.time()


def gcd(a, b):
    return gcd_ENG(abs(a), abs(b))

def gcd_ENG(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def g(t):
    tot = 0
    lim = math.ceil(math.sqrt(t/2))
    for n in range(1, lim):
        if t%(2*n) == 0:
            m = t//(2*n)
            if not(n%2 == m%2) and gcd(m, n) == 1:
                tot += 1
    return tot


def h(t):
    tot = 0
    for n in range(1, 2*t):
        m = math.floor(math.sqrt(t + n**2))
        if not(m%2 == n%2) and t + n**2 == m**2 and gcd(m, n) == 1:
            tot += 1
    return tot


def f(i):
    return g(i)+h(i)


def F(n):
    tot = 0
    for i in range(1, n+1):
        if n%i == 0:
            tot += f(i)
    return tot


def sigma(n):
    tot = 0
    for i in range(1, n+1):
        if n%i == 0:
            tot += 1
    return tot


def f_F(n):
    if n%2 == 0:
        return (sigma(n**2//4)-1)//2
    return (sigma(n**2)-1)//2



##for i in range(1, 40):
##    print("F(", i, ") = ", F(i))



## 47547 * 2 + 1 = 95095 = 5*7*11*13*19=(1+2*2)*(1+2*3)*(1+2*5)*(1+2*6)*(1+2*9)
## 2*F(t)+1 = sigma((t/2)^2) for t even
##smallest such t has t/2 = 


k = 2*(2**9)*(3**6)*(5**5)*(7**3)*(11**2)
print(k)


print(" --- %s seconds --- "%(time.time() - start_time))
