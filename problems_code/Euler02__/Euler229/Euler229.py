import time
import math
start = time.time()
ans = 0

LIM = 200*(10**1)
sqrtLIM = math.floor(math.sqrt(LIM + 1))
a1 = {}
a2 = {}
a3 = {}
a4 = {}
squares = [i*i for i in range(sqrtLIM)]
for s1 in range(1, sqrtLIM):
    if s1%514 == 13:
        print(s1)
    for s2 in range(1, sqrtLIM):
        v = squares[s1]+squares[s2]
        if v <= LIM:
            a1[v] = True
        else:
            continue
        v += squares[s2]
        if v <= LIM:
            a2[v] = True
        else:
            continue
        v += squares[s2]
        if v <= LIM:
            a3[v] = True
        else:
            continue
        v += 4*squares[s2]
        if v <= LIM:
            a4[v] = True

print("Dics created")
end = time.time()
print("Time elapsed ", end - start, " seconds")

for a in a4:
    if a in a1 and a in a2 and a in a3:
        ans += 1
        print(a)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")