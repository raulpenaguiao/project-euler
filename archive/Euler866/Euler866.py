#Code written on the 2024/05/14
#We compute the expected value recursively: the last step joins two processes and contributes with n*(2n-1)
#Runs in 0 ms

import time
start = time.time()
ans = 0

MOD = 987654319
N = 100


lst = [1, 1, 6]

for n in range(3, N+1):
    newVal = 0
    for j in range(n):
        newVal += lst[j]*lst[n-j-1]
        newVal %= MOD
    lst.append((newVal*(2*n-1))%MOD)

print("Answer = ", lst[-1])
end = time.time()
print("Time elapsed ", end - start, " seconds")