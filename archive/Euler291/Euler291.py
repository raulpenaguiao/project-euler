#Code written on the 2024/01/16
# the panaitopol primes are precisely the ones of the form n**2 + (n+1)**2
# I dont even know why, just found that fact on the internet
#We search for n until ~50M, and use Miller Rabin
#Runs in 592.36 seconds


import time
start = time.time()
from ...CL.CL_Primes import MillerRabin
import math
ans = 0
LIM = 5*10**15
lim = math.floor(math.sqrt(LIM))
for i in range(1, lim + 1):
    p = i**2 + (i+1)**2
    if p > LIM:
        break
    if MillerRabin(p):
        ans += 1



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")