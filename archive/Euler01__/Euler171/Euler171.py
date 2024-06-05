#Code written on the 30/10/2023
#Dinamic programing. These numbers satisfy an easy recursive relation
#First compute how many numbers with at most N digits have f(k) = M
#Use this to compute the sum of the numbers with this property
#Runs in 0.145 seconds


import time
import math
start = time.time()
ans = 0

N = 20
lim = 9*9*N
ans = 0
MOD = 1000000000

T = [[0 for _ in range(lim+1)]for _ in range(N+1)]
L = [[0 for _ in range(lim+1)]for _ in range(N+1)]
T[0][0] = 1
for i in range(1, N+1):
    for b in range(lim + 1):
        for m in range(10):
            dsum = b - m**2
            if dsum >= 0:
                T[i][b] += T[i-1][dsum]

for i in range(1, N+1):
    for b in range(lim + 1):
        for m in range(10):
            dsum = b - m**2
            if dsum >= 0:
                L[i][b] += L[i-1][dsum]
                L[i][b] += T[i-1][dsum]*m*(10**(i-1))
                L[i][b] %= MOD



for m in range(math.floor(math.sqrt(lim))):
    ans += L[N][m**2]
    ans %= MOD


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")