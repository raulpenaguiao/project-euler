#Code created on 30/10/2023
#There are three types of points, the hardest ones are in the circle that are dealt with a sweeping algorithm.
#Cdoe runs in 14.14 seconds


import time
import math
start = time.time()
ans = 0

N = 1_000_000_000

lLim = math.ceil(N*(1 - math.sqrt(2))/8)

for i in range(lLim, 0):
    ans += -1+2*math.ceil(math.sqrt(2*(N//8)**2 - (i - N//8)**2))
ans *= 4
ans += (N//4 + 1)**2 - (N//4 + 1) - 2
ans += (N//2)*(2*N)
ans += (N//4)*(2*N)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")