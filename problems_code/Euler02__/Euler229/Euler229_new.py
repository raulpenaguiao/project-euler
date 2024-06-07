import time
start = time.time()
ans = 0
import math
from ....CL.CL_Primes import Primes


def CheckPrime(p):
    if p%24 == 1:
        mod7 = p%7
        return mod7 == 1 or mod7 == 2 or mod7 ==4
    return p == 2


LIM = 200*(10**9)
primes = Primes(LIM)
primes_to_check = [p for p in primes if not CheckPrime(p)]#we will never need to consider 2 as a criteria

isRepr = [True for _ in range(LIM+1)]
for p in primes_to_check:
    dic = {q:1 for q in range(p, LIM+1, p)}
    powp = p*p
    while powp <= LIM:
        for q in range(powp, LIM+1, powp):
            dic[q] += 1
        powp *= p
    for q in dic:
        if dic[q]%2 == 1:
            isRepr[q] = False

ans = 0
for i in range(1, LIM+1):
    if isRepr[i]:
        ans += 1
        print(i)

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")