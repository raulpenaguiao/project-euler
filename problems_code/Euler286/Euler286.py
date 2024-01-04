import time
start = time.time()
from decimal import Decimal, getcontext
getcontext().prec  = 30

PREC = Decimal(10)**-15
qmax = Decimal(10)**10
qmin = Decimal(50)
targ = 0.02


def Shot(q):
    #computes probability of getting exactly 20 pts
    return 

while(abs(qmax-qmin) > PREC):
    q = (qmax+qmin)/2
    shot = Shot(q)
    if shot > targ:
        qmax = q
    else:
        qmin = q


print("Answer = ", qmin)
end = time.time()
print("Time elapsed ", end - start, " seconds")