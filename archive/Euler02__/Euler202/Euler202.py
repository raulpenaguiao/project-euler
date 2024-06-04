import time
import math

start_time = time.time()

## computes a couple of small examples so we can get used to the guesses
## PHI2 computes the number of a in 1, ..., M st (a, M) = 1 and a = 2 mod 3
## if M == 1 mod 3 then this should be the answer to teh problem of bounding N rays and M = (N+3)/2 


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def phi(M):
    count = 0
    for a in range(1, M):
        if gcd(M, a) == 1:
            count += 1
    return count

def PHI2(M):
    count = 0
    for a in range(2, M//2, 3):
        if gcd(M, a) == 1:
            count += 1
    return count*2

for N in range(10004,10100, 3):
    ph = phi(N)
    ph2= PHI2(N)
    print(N, " - phi = ", ph, " and phi2 = " , ph2, " and the guess is ", ph//3 , " or ", ph//3 - 1)

count = 0
N = 12017639147

print(N)

M = (N + 3)//2
LIM = M//2
for a in range(2, LIM, 3):
    if gcd(M, a) == 1:
        count += 1
print(count*2)




print(" --- %s seconds --- "%(time.time() - start_time))
