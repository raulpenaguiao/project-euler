#Code made on the 26/10/2023
#For each divisor d we count how many positive itnegers k are there such that d|k, and multiply by re(d).
#If d is integer, this is done directly (add i*(N//i))
#if a, b > 0, then a + ib divides all the multiples of d(a'^2 + b'^2), where d = gcd(a, b), a' = a/d, b' = b/d
#so for all a', b' coprime, we simply sum d a' (N//(d(a'^2 + b'^2)))
#if im(d) < 0, we just copy what happens on the positive side (multiply by 2)
#Runs in 74.51598477363586s

import time
import math
start = time.time()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def f(a):
    ans = 0
    for i in range(1, a+1):
        ans += a - a%i
    return ans

ans = 0
N = 10**8

for i in range(1, N+1):
    ans += i*(N//i)


srN = math.floor(math.sqrt(N))
for i in range(1, srN+1):
    cont = 0
    isq = i*i
    sqtarg = math.floor(math.sqrt(N-isq))
    for j in range(1, sqtarg+1):
        if(gcd(i, j) == 1):
            cont += f(N//(isq + j*j))
    ans += 2*i*cont


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")