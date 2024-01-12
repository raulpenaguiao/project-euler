import time
start = time.time()
from ...CL.CL_Arithmetics import gcd
ans = 0


n = [5248, 1312, 2624, 5760, 3936]
m = [640, 1888, 3776, 3776, 5664]

mmax = max(m)
nmax = max(n)

rat = {}
coPrimePairs = []
for a in range(1, mmax+1):
    if a%41 == 13:
        print(a)
    for b in range(1, nmax+1):
        if gcd(a, b) == 1:
            te = tuple([a, b])
            coPrimePairs.append(te)

print("A")

for a, b in coPrimePairs:
    mn = min(a//mmax, b//nmax)
    rat[te] = [tuple(a*i, b*i)  for i in range(1, 1+nmax)]


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")