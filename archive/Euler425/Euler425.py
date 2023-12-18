#Code written in 2023/12/07
#BFS on the graph constructed in the problem, where the BFS is done with a priority queue
#We want to visit the lowest neighbour that we havent visited yet
#We check all the neighbours that we have not visited, add them to queue
#Remember how high is the number where you came from (largest in the whole path)
#Runs in 59.75 seconds


import time
start = time.time()
import CL_Primes as CP
import CL_Digits as CD
import queue

LIM = 10**7
primes = CP.Primes(LIM)
primeQ = {i:False for i in range(LIM+1)}
for p in primes:
    primeQ[p] = True


neigp = {p:[] for p in primes}
for p in primes:
    dgs = CD.Digits(p)
    for i in range(len(dgs)):
        for d in range(10):
            if not(i == 0 and d == 0) and not(dgs[i] == d):
                a = dgs[i]
                dgs[i] = d
                q = CD.ToInteger(dgs)
                dgs[i] = a
                if q <= LIM and primeQ[q]:
                    neigp[p].append(q)
    if len(dgs) > 1 and not(dgs[1] == 0):
        q = CD.ToInteger(dgs[1:])
        if q <= LIM and primeQ[q]:
            neigp[q].append(p)
            neigp[p].append(q)

#BFS according to a priority queue
q = queue.PriorityQueue()
q.put(2)
larg = {p:LIM+1 for p in primes}
larg[2] = 2
ans = 0

while not q.empty():
    p = q.get()
    if larg[p] > p:
        ans += p
    top = max(p, larg[p])
    for r in neigp[p]:
        if larg[r] == LIM + 1:
            larg[r] = top
            q.put(r)

for p in primes:
    if larg[p] == LIM+1:
        ans += p

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")