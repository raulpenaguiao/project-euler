#Code written on the 2024/06/11
# Generates all products of primes below $10^{16}$ in about 30 seconds
# For each product, counts its contribution using inclusion exclusion principles. That is the resulting sum is
#$\sum_{l\geq 4} a_k \sum_{i_1<\cdots <i_l} \# \bigcap_{s=1}^l P_{i_s}$
# The correct coefficient for the inclusion exclusion is $a_k = \sum_{m\geq 4} \binom{k}{m}(-1)^{k-m}$
#This is because these are the coeficients that satisfy that $\sum_k \binom{l}{k}a_k $ is one precisely when $l\geq 4$, and is zero otherwise.
#Runs in 40.23 seconds

import time
start = time.time()
ans = 0

from ....CL.CL_Primes import Primes
from queue import Queue
from ....CL.CL_Binomial import Binom

def GenerateProductsBelow(lst, bound):
    prodList = Queue()
    prodList.put([1, 0])
    ans = Queue()
    ans.put([1, 0])
    for p in lst:
        nProdList = Queue()
        while not prodList.empty():
            f, n = prodList.get()
            newF = f*p
            if newF < bound:
                ans.put([newF, n+1])
                nProdList.put([f, n])
                nProdList.put([newF, n+1])
        prodList = nProdList
    return ans


primes = Primes(100)
N = 10**16
lim = len(primes) + 1
a = [0 for _ in range(lim)]
for k in range(lim):
    for M in range(4, k+1):
        a[k] += Binom(k, M)*(-1)**(k-M)

sfProdList = GenerateProductsBelow(primes, N)

dic_counted = {}
while not sfProdList.empty():
    primeProduct, l = sfProdList.get()
    if l >= 4:
        ans += a[l]*((N-1)//primeProduct)

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")