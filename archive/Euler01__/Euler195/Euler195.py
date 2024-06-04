#Code written on 2023/11/21
#Equilateral triangles do not count
#If a is the side opposing to the 60 deg angle, inradius is (b+c-a)/(2sqrt(3))
#Every primitive such triangle has a unique m, n coprime with a, b, c given below, (m, n) = 1 and 2n < m
#Runs in 13.9 seconds


import time
import math
from ...CL.CL_Rational import gcd
start = time.time()
N = 1053779
#N = 400000
#N = 10000
#N = 1000
#N = 100
#N = 10
#ans = math.floor(math.sqrt(3)*N*2) #Start with the number of equilateral triangles with inradius <= n
ans = 0 #turns out these should not be considered anyway
dic = {}

mub =  math.floor(N*2*math.sqrt(3))+2
for m in range(1, mub):
    n = 1
    R = (m-1)
    rub = N * 2 * math.sqrt(3)
    while(R <= rub and 2*n < m):
        if gcd(m, n) == 1:
            r = (n*(m-n)*math.sqrt(3))/2
            if (m+n)%3 == 0:
                r /= 3
            ans += math.floor(N/r)
        n += 1
        R = n*(m-n)

print("n = ", N)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")