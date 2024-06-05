#Code written on the 15/11/2023
#Dynamic programming allows us to compute the number of colourings of a triangle of size n by knowing colourings of size n-1
#We have to know the number of colourings that have a specific colouring on the bottom row
#Runs in 19.98s
#For N = 9 runs in 185s and gives 104224568112581443584

import time
import math
import queue
start = time.time()
ans = 0

N = 8

def GenerateTuples(n):
    if n == 0:
        return [tuple([])]
    ans = []
    for t in GenerateTuples(n-1):
        l = list(t)
        ans.append(tuple([1]+l))
        ans.append(tuple([2]+l))
        ans.append(tuple([3]+l))
    return ans



def f(a, b, c):
    if a == b:
        if b == c:
            return 2
        return 1
    if a == c or b == c:
        return 1
    return 0


colouringWays = [{} for _ in range(N+1)]
colouringWays[1] = {tuple([1]):1, tuple([2]):1, tuple([3]):1}
for i in range(2, N+1):
    colouringWays[i] = {t:0 for t in GenerateTuples(i)}
    for t in colouringWays[i]:
        for w in colouringWays[i-1]:
            new_ways = 1
            for n in range(i-1):
                new_ways *= f(t[n], t[n+1], w[n])
                #print(t, w, n, f(t[n], t[n+1], w[n]), new_ways)
            colouringWays[i][t] += new_ways*colouringWays[i-1][w]
        #print(i, t, colouringWays[i][t])
ans = 0
for c in colouringWays[N]:
    ans += colouringWays[N][c]
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")