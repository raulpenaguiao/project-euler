import time
start = time.time()
ans = 0

#Sequence A008443

lim = 17526
T = [0]
vis = [0 for _ in range(lim+1)]

while T[-1] <= lim:
    T += [T[-1] + len(T)]

for a in T:
    for b in T:
        for c in T:
            if a+b+c <= lim:
                vis[a+b+c] += 1

print(vis[:30])
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")