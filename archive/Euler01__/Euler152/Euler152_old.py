import time
import math
start = time.time()
from decimal import Decimal, getcontext 
getcontext().prec = 16



def bin_search(trg, ls, ln):
    top = ln
    bot = -1
    while(top - bot > 1):
        mid = (top+bot)//2
        if ls[mid] > trg:
            top = mid
        else:
            bot = mid
    return bot


tot = 0
L = 55
head = [0]
for i in range(1, L+1):
    tot += 1/Decimal(i**2)
    head += [tot]
tail = [tot - h for h in head]

PREC = Decimal(0.00000000001)
ans = 0
queue = [Decimal(0)]
for i in range(2, L+1):
    n_q = []
    iinvs = 1/Decimal(i**2)
    ln = len(queue)
    print(i, " -- ", ln)
    i1 = bin_search(Decimal(0.5) + PREC - iinvs, queue, ln)
    i2 = bin_search(Decimal(0.5) - PREC - iinvs, queue, ln)
    i3 = bin_search(Decimal(0.5) - PREC - tail[i], queue, ln)
    print(i1, i2, i3)
    ans += i1 - i2
    n_q = [v+iinvs for v in queue[:i1+1]] + queue[i3+1:]
    queue = [v for v in n_q]
    queue.sort()

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")