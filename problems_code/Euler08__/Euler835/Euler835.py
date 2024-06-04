import time
start = time.time()
ans = 0

from math import log10

def f(k):
    return 2*(k+1)*(2*k+1)


def T(n):
    return n*(n+1)//2


def Q(n):
    return n*(n+1)*(2*n+1)//6


def maxP(lgN):
    lbd = 1
    ubd = 2
    while log10(f(ubd)) <= lgN:
        ubd *= 2
    while ubd - lbd > 1:
        mbd = (ubd+lbd)//2
        if log10(f(mbd)) <= lgN:
            lbd = mbd
        else:
            ubd = mbd
    return lbd


def F(x, y):
    return (x+y)*(x+2*y)*2

MOD = 1234567891
lgN = (10**4)
P = maxP(lgN)
ans = 4*Q(P) + 6*T(P) + 2*P
ans %= MOD

x = [1, 3]
y = [1, 2]
p = log10(F(x[-1], y[-1]))
while(p <= lgN):
    ans += p
    ans %= MOD
    x0 = x[0]*x[-1] + y[0]*y[-1]*2
    y0 = x[0]*y[-1] + y[0]*x[-1]
    x.append(x0)
    y.append(y0)
    p = F(x0, y0)




print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")