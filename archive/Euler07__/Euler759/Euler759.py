#Code written on the 2024/06/10
#Induction proves that $f(i) = i\times d(i)$, where $d(i)$ is the number of one digits in the binary expansion of $i$
#The sum $S(n) = \sum_d d^2 \sum_{i: d(i) = d, i\leq n} i^2$ can be split into distinct blocks according to the binary expansion of $n+1$
#Crutial step is computing the following function
#$M_i(k, d) = \sum_{0 \leq l_1 < \cdots < l_d < k} (2^{l_1} + \cdots 2^{l_k})^i$
#We use it for $i = 0, 1, 2$
#Runs in 2 ms



import time
start = time.time()
ans = 0

def digits(n, base = 2):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]

limD = 100
binom = [[0 for _ in range(limD+1)] for _ in range(limD)]
#binom[k][j] = number of <=k-digit integers base 2 that has digit sum j
for k in range(limD):
    binom[k][0] = 1
    for j in range(1, k+1):
        binom[k][j] = binom[k-1][j] + binom[k-1][j-1]


def Binom(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return binom[n][k]

def FromDigits(ls, base = 2):
    if ls == []:
        return 0
    return ls[-1] + base * FromDigits(ls[:-1], base)

def M2(k, d):
    return Binom(k-2, d-2)*(2**k - 1)**2 + (4**k - 1)*(Binom(k - 1, d - 1) - Binom(k - 2, d - 2))//3

def SquareFSum(N, mod):
    digs = digits(N+1)
    ans = 0
    l = len(digs)
    sumDigs = sum(digs)
    pow2 = 1
    for index, d in enumerate(digs[::-1]):
        if d == 1:
            bottom = (FromDigits(digs[:l - index]) - 1)*pow2
            sumDigs -= 1
            for f in range(index+1):
                a = (f+sumDigs)**2
                b = M2(index, f)
                b += Binom(index - 1, f - 1) * (2**index - 1) * bottom * 2
                b += Binom(index, f) * bottom**2
                ans += a*b
                ans %= mod
        pow2 *= 2
    return ans


print("Answer = ", SquareFSum(10**16, 1_000_000_007))
end = time.time()
print("Time elapsed ", end - start, " seconds")