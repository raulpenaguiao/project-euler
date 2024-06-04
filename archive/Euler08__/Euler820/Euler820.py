import time
import math

start_time = time.time()

def power_mod(a, m, p):
    if a%p == 1 or m == 0:
        return 1
    if m == 1:
        return a%p
    x = power_mod((a*a)%p, m//2, p)
    if m%2 == 1:
        x *= a
        x %= p
    return x

LIM = 10**7
tot = 0
for i in range(1, LIM+1):
    a = power_mod(10, LIM-1,i) 
    tot += (10*a)//i
print("tot = ", tot)
print(" --- %s seconds --- "%(time.time() - start_time))
