# Code written on the 2024/01/04
# Note that Shot(50) = 0.04 and Shot(100) << 0.02, so we only need to do binary search there
# The function is decreasing in this part
# DP to fing the probability of hitting 20 shots
# Binary search to find que desired q
# Runs in 0.11953878402 seconds

import time
start = time.time()
from decimal import Decimal, getcontext
from ...CL.CL_Rational import Rational
from math import log
getcontext().prec  = 30


def Shot(q):
    DP = [[Decimal(0) for _ in range(51)] for _ in range(51)]
    DP[0][0] = Decimal(1)
    for i in range(1, 51):
        DP[0][i] = DP[0][i-1]*(Decimal(i)/q)
        for j in range(1, 51):
            DP[j][i] = DP[j][i-1]*(Decimal(i)/q) + DP[j-1][i-1]*(1 - Decimal(i)/q)
    #computes probability of getting exactly 20 pts
    #If each point is a bernoulli with probability 1-x/q
    return DP[20][50]


print(Shot(50), Shot(100))
PREC = Decimal(10)**-15
qmax = Decimal(10)**2
qmin = Decimal(50)
targ = Decimal(0.02)


while(abs(qmax-qmin) > PREC):
    q = (qmax+qmin)/Decimal(2)
    shot = Shot(q)
    if shot > targ:
        qmin = q
    else:
        qmax = q


print("Answer = ", qmin)
end = time.time()
print("Time elapsed ", end - start, " seconds")