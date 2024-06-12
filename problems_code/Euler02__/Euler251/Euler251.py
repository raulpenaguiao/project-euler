#Code written on the 2024/06/12
#$(a, b, c)$ forms a cardano triple if and only if $(2a - 1)^3 = 27 (a^2 - b^2 \cdot c)$
#Runs in more than 200.000 seconds



import time
start = time.time()
ans = 0

from ....CL.CL_Primes import Primes, Divisors

N = 11*10**7
primes = Primes(8*(N//3))
print()
end = time.time()
print("Time elapsed ", end - start, " seconds  :: Primes computed up to ", 8*(N//3))
LM = 1+(1+N)//3
for a0 in range(1, LM):
    if a0%5152 == 23:
        end = time.time()
        print("Time elapsed ", end - start, " seconds :: ", a0, " vs ", LM)
    sqrval = a0*(8*a0 - 3)
    val = a0*sqrval
    a = 3*a0-1
    for b in Divisors(sqrval, primes):
        if b <= N - a - 1:
            bs =b*b
            if val % bs == 0:
                c = val//bs
                if c <= N - a - b:
                    ans += 1

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")