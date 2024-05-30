# Code written on the 2024/05/30
# Brute force is not good enough

import time
start = time.time()
ans = 0

from queue import Queue

def Mid(i, j, N, verbose = False):
    xi = i%N
    yi = i//N
    xj = j%N
    yj = j//N
    ans = []
    for k in range(N*N):
        if j == k or i == k:
            continue
        xk = k%N
        yk = k//N
        if abs(xk-xi) > abs(xj-xi):
            continue
        if abs(yk-yi) > abs(yj-yi):
            continue
        if (xk-xi)*(xj-xi) < 0:
            continue
        if (yk-yi)*(yj-yi) < 0:
            continue
        if (xk-xi)*(yj-yi) == (xj-xi)*(yk-yi):
            ans += [k]
    return ans


def Syms(i, N):
    xi = i%N
    yi = i//N
    f1 = (xi == yi)
    f2 = (2*yi == N - 1)
    if f1 or f2:
        if f1 and f2:
            return 1
        return 4
    return 8



N = 3
edges = [[] for _ in range(N*N)]

for i in range(N*N):
    for j in range(N*N):
        if i == j:
            continue
        mid = Mid(i, j, N)
        edges[i].append([j, mid])

counter = 0
for i in range(N*N):
    for j, mid in edges[i]:
        for m in mid:
            #print(i, j, m)
            counter += 1
print("There are ", counter, " different restrictions in the arrangement.")

q = Queue()
for i in range(N*N):
    xi = i%N
    yi = i//N
    if 2*yi < N and xi <= yi:
        q.put([i])

currlen = 1
while(not q.empty()):
    pth = q.get()
    ans += Syms(pth[0], N)
    if len(pth) > currlen:
        currlen = len(pth)
        print(currlen, " with approximately ", q.qsize(),  " elements in queue. Number of passwords found so far: ", ans)
        end = time.time()
        print("Time elapsed ", end - start, " seconds")
    for endpt, md in edges[pth[-1]]:
        if endpt in pth:
            continue
        flag = True
        for m in md:
            if not(m in pth):
                flag = False
                break
        if flag:
            q.put(pth + [endpt])

#Remove passwords of length 1
ans -= N*N

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")