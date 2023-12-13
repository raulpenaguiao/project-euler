#Code created on the 30/10/2023
#Uses the fact that the angles at X are 120
#Cosine law tells us that a**2 = p**2 + p*q + q**2 and so on
#Solutions to this equation can be generated with the formula in
#   https://www.had2know.org/academics/integer-triangles-120-degree-angle.html
#Generate first all allowed pairs (p, q) that have an integer solution above, there are ~3*10e5
#then run over all p and try to find
#   q and r that are themselves an allowed pair
#Runs in 8.61 seconds

import time
import math
start = time.time()

def isSquare(k):
    return math.floor(math.sqrt(k))**2 == k


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


N = 120000
allowedPairs = {}
paired = [[] for _ in range(N+1)]
vis = [False for _ in range(N+1)]

tot = 0
Nsr = math.floor(math.sqrt(N))
for m in range(1, N//2 + 1):
    lm = min(Nsr + 1, m)
    for n in range(1, lm):
        if gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n + n**2
            if a <= N and b <= N:
                mx = max(a, b)
                for d in range(1, N//mx + 1):
                    paired[d*a] += [d*b]
                    paired[d*b] += [d*a]
                    tot += 1


for a in range(1, N+1):
    paired[a].sort()

for a in range(1, N+1):
    for b in paired[a]:
        for c in paired[a]:
            if a+b+c <= N and (c in paired[b]):
                vis[a+b+c] = True


totans = 0
for i in range(1, N+1):
    if vis[i]:
        totans += i

print("Number of allowed pairs = ", tot)
print("Answer = ", totans)
end = time.time()
print("Time elapsed ", end - start, " seconds")
