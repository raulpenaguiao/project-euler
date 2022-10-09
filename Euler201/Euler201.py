import time
import math

start_time = time.time()

#Defines the sum of squares up to n
def sumSq(n):
    if n < 0:
        return 0
    return (n*(n+1)*(2*n+1))//6

LIM = 100
SIZE = LIM//2
sumLIM = sumSq(LIM) - sumSq(LIM-SIZE)


S = [t*t for t in range(1, LIM+1)]

#Ssum[s] is the maximal sum of SIZE squares up to s
Ssum = [sumSq(t)-sumSq(t-SIZE) for t in range(1, LIM+1)]


# v[s][k][t] = number of subsets of {a_1, ..., a_s} with k elements and with sum == t
v = [[[0 for t in range(sumLIM+1)] for k in range(LIM+1)] for s in range(3)]
#print("memory created")
#print(" --- %s seconds --- "%(time.time() - start_time))
for s in range(LIM+1):
    v[s%2][0][0] = 1


#This takes advantage of the recursion v[s][k][t] = v[s-1][k][t] + v[s-1]k-1][t-S[s-1]]
for s in range(1, LIM+1):
    m = min(s, SIZE)
    #m = s
    for k in range(m+1):
        for t in range(Ssum[s-1]+1):
            v[s%2][k][t] = v[(s-1)%2][k][t]
            if k > 0 and t >= S[s-1]:
                v[s%2][k][t] += v[(s-1)%2][k-1][t - S[s-1]]

#Only thing left to do is count how many entries are there with a unique sum
tot = 0
for t in range(Ssum[s-1]+1):
    if v[LIM%2][SIZE][t] == 1:
        tot += t


print("Answer = ", tot)
print(" --- %s seconds --- "%(time.time() - start_time))
