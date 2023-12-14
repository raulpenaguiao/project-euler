#Code written in 2023/11/15
#Runs in 10**(n/2) memory and time
#Python seems to be really bat at
#For each 8 dig number, computes the number of matching chars on the left side and saves the result
#For each 8 dig number, computes the number of matching chats on the right and sees it it complements well with some of the saved results
#Runs in 2421 seconds


import time
import math
import queue
start = time.time()


input = """
5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct
"""

dinput = """
90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct
"""

chrs = [str(i) for i in range(10)]
data = []
for wrd in input.splitlines():
    if wrd == "":
        continue
    a, b = wrd.split(';')
    data.append([a.split(" ")[0], int(b.split(" ")[0])])
N = len(data[0][0])
n = 10**(N//2)
m = 10**(N-N//2)

def Str(i, n):
    ans = str(i)
    return "0"*(n - len(ans))+ans


def CountMatches(st1, st2):
    count = 0
    for c1, c2 in zip(st1, st2):
        if c1 == c2:
            count += 1
    return count


def validate(l1, l2):
    flag = True
    for v1, v2 in zip(l1, l2):
        if v1 > v2:
            flag = False
            break
    return flag

dataval = [d[1] for d in data]
data1 = [w[:N//2] for w, d in data]
data2 = [w[N//2:] for w, d in data]
tpls = {}
for i in range(n):
    a = [CountMatches(Str(i, N//2), d) for d in data1]
    if validate(a, dataval):
        tpls[tuple([v2-v1 for v1, v2 in zip(a, dataval)])] = i

for i in range(m):
    t = tuple([CountMatches(Str(i, N-N//2), d) for d in data2])
    if t in tpls:
        print(Str(tpls[t], N//2) + Str(i, N-N//2))

end = time.time()
print("Time elapsed ", end - start, " seconds")