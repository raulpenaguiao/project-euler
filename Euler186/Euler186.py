import time
import math

start_time = time.time()
found = False
k = 0
PM = 524287
def ro(k):
    t = k
    while not(root[t][0] == t):
        t = root[t][0]
    return t

def s(k):
    return (100003 - 200003*k + 300007*k*k*k)%1000000

S = [s(k) for k in range(56)]
LIM = 5000000
for k in range(56, LIM):
    S += [(S[k-24] + S[k-55])%1000000]
root = [[k, 1] for k in range(1000000)]
k = 1
calls = 0
while not(found):
    #Connect the callers
    #print(" k = ", k, " - Caller ", S[k], " to ", S[k+1])
    c1 = ro(S[k])
    c2 = ro(S[k+1])
    if k%100000 < 6:
        print(k)
        for i in range(1000000):
            root[i][0] = ro(i)
    if not(S[k] == S[k+1]):
        calls += 1
    else:
        print("BUTT DIAL! At k = ", k)
    if not(c1 == c2):
        root[c2][1] = root[c1][1] + root[c2][1]
        root[c1][0] = c2
    PMc = ro(PM)
    root[PM][0] = PMc
    if root[PMc][1] >= 990000:
        found = True
    k += 2
    if k >= LIM-1:
        print("LIMIT EXHAUSTED, size of connected component of PM is ", root[PMc][1])
        found = True
counter = 0
for i in range(1000000):
    if root[i][0] == i:
        counter += 1
        if root[i][1] > 100:
            print("Component of ", i, " has ", root[i][1], " elements")
print(" Calls = ", calls, " and components = ", counter)
print(" --- %s seconds --- "%(time.time() - start_time))
