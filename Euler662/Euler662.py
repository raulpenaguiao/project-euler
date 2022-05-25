import time
import math

start_time = time.time()

fibbs = [1, 2]
lim = 10000 + 1


while fibbs[-1] < lim:
    fibbs += [fibbs[-1] + fibbs[-2]]
fibs_sq = [a*a for a in fibbs]

def is_fibs(x, y):
    return (x * x + y * y) in fibs_sq

steps = []
for x in range(1, lim):
    for y in range(1, lim):
        if is_fibs(x, y):
            steps += [(x, y)]
#print(len(steps))
#print(len(fibbs))


paths = [[0 for i in range(lim)] for j in range(lim)]
prime = 10 ** 9 + 7

paths[0][0] = 1

for j in range(lim):
    for i in fibbs:
        if i <= j:
            paths[j][0] += paths[j-i][0]
            paths[j][0] %= prime
            paths[0][j] += paths[0][j-i]
            paths[0][j] %= prime


for i in range(1, lim):
    for j in range(1, lim):
        for f in fibbs:
            if f <= i:
                paths[i][j] += paths[i-f][j]
                paths[i][j] %= prime
            if f <= j:
                paths[i][j] += paths[i][j-f]
                paths[i][j] %= prime
        for step in steps:
            if step[0] <= i and step[1] <= j:
                paths[i][j] += paths[i-step[0]][j-step[1]]
                paths[i][j] %= prime
print(paths[-1][-1])


print(" --- %s seconds --- "%(time.time() - start_time))
