### 2023_01_06
### Author: Raul Penaguiao
### Project Euler problem 813

### represents polynomials in F2 as lists of 0's and 1's
import math
import time
t_begin = time.time()


##Adds polynomials
def add(l1, l2):
    if len(l1) < len(l2):
        return add(l2, l1)
    ans = [l1[i] for i in range(len(l1))]
    for j in range(len(l2)):
        ans[j] += l2[j]
        ans[j] %= 2
    j = len(l1) - 1
    while j >= 0 and ans[j] == 0:
        j-= 1
    return ans[0:j+1]


## Multiplies polynomials by x
def sh(l):
    return [0] + l

## p -> (p - p(0))/x
def unsh(l):
    return l[1:]

## polynomial product
def pr(l1, l2):
    ans = []
    for i in range(len(l1)):
        if l1[i] == 1:
            ans = add(ans, [0]*i + l2)
    return ans

## power of polynomials
def power(l, n):
    if n == 1:
        return l
    l_carry = power(pr(l, l), n//2)
    if n%2 == 1:
        l_carry = pr(l, l_carry)
    return l_carry

## evaluates polynomial p at value base, computations modulo
## evaluation in Z
def comp(lis, base, mod):
    po = 1
    ans = 0
    for i in range(len(lis)):
        if lis[i] == 1:
            ans += po
            ans %= mod
        po *= base
        po %= mod
    return ans


def power_mod(a, m, p):
    if m == 0:
        return 1
    ans = power_mod((a*a)%p, m//2, p)
    if m%2 == 1:
        ans *= a
        ans %= p
    return ans


#compute 2**2**52 module 
MOD = 1_000_000_007
t = power_mod(2, 2**52, MOD)
eleven = [1, 1, 0, 1]
num = power(eleven, 3**8)

print(comp(num, t, MOD))
print(comp(power(eleven, 2), 2, MOD))
print(comp(eleven, power_mod(2, 2, MOD), MOD))
print("Duration: ", math.floor((time.time() - t_begin)*10_000_000)/10000, " ms")
