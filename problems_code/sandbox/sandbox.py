import time
start = time.time()
from math import floor, sqrt

LIM = 10**2
K = 10

ndivs = [1 for _ in range(LIM+1)]
ondivs = [1 for _ in range(LIM+1)]

for i in range(2, LIM+1):
    for j in range(i, LIM+1, i):
        ndivs[j] += 1
ans = 0





print(ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")