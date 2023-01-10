import time
import math

start_time = time.time()


def ord(a, p):
    k = 1
    po = a%p
    while po > 1:
        po *= a
        po %= p
        k += 1
    return k
def power_mod(a, m, p):
    if m == 0:
        return 1
    k = power_mod((a*a)%p, m//2, p)
    if m%2 == 1:
        return (a*k)%p
    return k

LIM = 10_000_000
sieve = [1]*(LIM + 10)
sqLIM = math.floor(math.sqrt(LIM))
for i in range(2, sqLIM+1):
    if sieve[i] == 1:
        k = i**2
        while k <= LIM:
            sieve[k] = 0
            k += i
primes = []
for i in range(3, LIM+1):
    if sieve[i] == 1:
        primes += [i]
print("Primes computed")
print(" --- %s seconds --- "%(time.time() - start_time))


#def g_inef(p):
#    k = 2**(2**p)//p
#    k %= 2**p
#    return k%p


def g_2(p):
    k1 = power_mod(2, p, p-1)
    k1 = power_mod(2, k1, p)
    j1 = power_mod(p, 2**(p-1)-1, 2**p)
    a = 2**p - (k1*j1)%2**p
    return a%p

def g(n):
    f = power_mod(2, p-2, p)
    k1 = power_mod(2, p, p-1)
    k1 = power_mod(2, k1, p)
    f *= k1
    f %= p
    h = power_mod(2, p, p*p)
    h *= f
    h %= p*p
    return h//p

ans = 0
for p in primes:
    ans += g(p)

print(ans)
print(" --- %s seconds --- "%(time.time() - start_time))
