import time
start = time.time()
from decimal import Decimal, getcontext
getcontext().prec = 40

LIM = 85

ans = Decimal(0)
for i in range(2, LIM + 1):
    ans += Decimal(1)/Decimal(i*i)

print(ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")