#Code done on the 23/10/2023
#First assumption that there are infinitely many licence plates and all of them exist infinitely many times
#This problem can be modeled with a markov chain, on 1+500*2 states, and we want to compute the exit time from the 500*2 transient component.
#This component happens to be upper triangular, so invertion is specially easy an ddoes not need Gaussian elimination.
# Runs in 2.21 ms

import time
import math
import numpy as np
from decimal import *

start = time.time()

#Let's assume there are infinitely many license plates of each number
"""
LICENSESdiv2 = 10
mat = [[0 for _ in range(LICENSESdiv2*2)] for _ in range(LICENSESdiv2*2)]#transition matrix of transient states
for i in range(LICENSESdiv2):
    mat[i][i] = (i+1)/(LICENSESdiv2*2)
    mat[i][i+LICENSESdiv2] = 1/(LICENSESdiv2*2)
    mat[i+LICENSESdiv2][i+LICENSESdiv2] = (i+1)/(LICENSESdiv2*2)
    if(i < LICENSESdiv2 - 1):
        mat[i+LICENSESdiv2][i+LICENSESdiv2+1] = (LICENSESdiv2 - i-1)/LICENSESdiv2
        mat[i][i+1] += (2*LICENSESdiv2 - 2*i - 2)/(LICENSESdiv2*2)
n = [[0 for _ in range(LICENSESdiv2*2)] for _ in range(LICENSESdiv2*2)]#fundamental matrix
for i in range(LICENSESdiv2*2):
    for j in range(LICENSESdiv2*2):
        if (i == j):
            n[i][j] = 1-mat[i][j]
        else:
            n[i][j] = -mat[i][j]
t = [0 for _ in range(LICENSESdiv2*2)]
t[0] = 1

ans = np.linalg.solve(np.array(n), np.array(t)).sum()"""


EET = [[Decimal(0) for _ in range(500)] for _ in range(2)]

EET[1][499] = Decimal(2)
EET[0][499] = (1+2*Decimal(1/1000))/Decimal(1 - Decimal(499/1000))
for i in range(498, -1, -1):
    EET[1][i] = (1 + EET[1][i+1] * Decimal(1000 - 2*i - 2)/1000)/Decimal(1 - (i+1)/1000)
    EET[0][i] = (1 + EET[0][i+1] * Decimal(1000 - 2*i - 2)/1000 + EET[1][i] * Decimal(1/1000))/Decimal(1 - Decimal(i+1)/1000)


print("Answer = ", EET[0][0])
end = time.time()
print("Time elapsed ", end - start, " seconds")