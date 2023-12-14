import time
import math

start_time = time.time()


def power_mod(a, p, m):
    if p < 2:
        if p == 0:
            return 1
        if p == 1:
            return a%m
    if a == 1:
        return 1
    if p%2 == 0:
        return power_mod((a*a)%m, p//2, m)
    return (a*power_mod((a*a)%m, p//2, m))%m


mat = [[0 for i in range(35)] for j in range(13)] 
## We only need to consider the sum up to 33, above that index the numbers are too small to affect decimal values in the interval at hand
## We study four more digits to make sure we dont have some carry from unstudied digits
for i in range(1, 35):
    L = 10**16-3**i
    t = 3**i
    for j in range(13):
        if L > 0:
            F = power_mod(10, L+j-1, t)
            mat[j][i] = (F*10)//t
l =  [sum(mat[j]) for j in range(13)]
t = sum([l[i]*10**(13-i) for i in range(13)])
print((t//10000)%10**10) 
## We only want to see 10 digits, and we should want to trim the last four. 
print(" --- %s seconds --- "%(time.time() - start_time))
