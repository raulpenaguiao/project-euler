#Code written on the 7th of May 2024
#Uses the fact that any fair configuration has a piles of GG, b piles of GS, c piles of SG and d piles of SS
#It must satisfy a+b+c+d = 9898 and the fairness condition 4*a+b = c + 4*d
#Runs in 10 seconds

import time
start = time.time()
ans = 0

LIM = 9900
mod = 989898989

binom = [ [0 for _ in range(n//2 + 2)] for n in range(LIM+1)]
for i in range(LIM+1):
    binom[i][0] = 1
binom[1][1] = 1
binom[2][1] = 2
binom[2][2] = 1
for n in range(3, LIM+1):
    for j in range(1, n//2 + 2):
        if 2*j > n:
            binom[n][j] = binom[n][n-j]
        else:
            binom[n][j] = binom[n-1][j] + binom[n-1][j-1]
        binom[n][j] %= mod


def Binomial(n, a):
    if n < 0 or a > n or a < 0:
        return 0
    if 2*a > n:
        return binom[n][n-a]
    return binom[n][a]

def Multinomial(n, a, b, c):
    """Computes \binom{n}{a, b, c, d}
    assumes that a+b+c+d = n
    """
    ans = 1
    m = n
    ans *= Binomial(m, a)
    m -= a
    ans *= Binomial(m, b)
    m -= b
    ans *= Binomial(m, c)
    return ans%mod

def F(n):
    ans = 0
    for b in range(n+1):
        for c in range(b%4, n-b+1, 4):
            y1 = n - b - c
            y2 = (c-b)//4
            if (y1+y2)%2 == 1:
                continue
            a = (y1+y2)//2
            if a < 0 or y1 < y2:
                continue
            ans += Multinomial(n, a, b, c)
            ans %= mod
    return ans


print("Answer = ", F(2))
print("Answer = ", F(4))
print("Answer = ", F(5))
print("Answer = ", F(9898))
end = time.time()
print("Time elapsed ", end - start, " seconds")