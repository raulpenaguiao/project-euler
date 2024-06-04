import time
import math
start = time.time()
ans = 0

LIM = 1*(10**7)
sqrtLIM = math.floor(math.sqrt(LIM))
a1 = [False for _ in range(LIM+1)]
a2 = [False for _ in range(LIM+1)]
a3 = [False for _ in range(LIM+1)]
a4 = [False for _ in range(LIM+1)]
print("List created")
end = time.time()
print("Time elapsed ", end - start, " seconds")
for s1 in range(1, sqrtLIM):
    if s1%51 == 13:
        print(s1)
    for s2 in range(1, sqrtLIM):
        v = s1*s1+s2*s2
        if v <= LIM:
            a1[v] = True
        else:
            continue
        v += s2*s2
        if v <= LIM:
            a2[v] = True
        else:
            continue
        v += s2*s2
        if v <= LIM:
            a3[v] = True
        else:
            continue
        v += 4*s2*s2
        if v <= LIM:
            a4[v] = True


for a in range(1, LIM+1):
    if a1[a] and a2[a] and a3[a] and a4[a]:
        ans += 1
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")