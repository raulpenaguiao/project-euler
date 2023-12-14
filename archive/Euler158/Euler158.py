#Code on the 13/11/2023
#Formula for p(n) = (2^n - n - 1)*binom[26][n]
#Runs in 0.0000 seconds

import time
import math
start = time.time()
ans = 0


binom = [[0 for _ in range(30)] for _ in range(30)]
binom[0][0] = 1
for N in range(27):
    binom[N][0] = 1
    binom[N][N] = 1
    for i in range(1, N):
        binom[N][i] = binom[N-1][i] + binom[N-1][i-1]

tbl = [[(2**n-n-1)*binom[26][n], n] for n in range(27)]
tbl.sort()

print("Answer = ", tbl[-1])
end = time.time()
print("Time elapsed ", end - start, " seconds")