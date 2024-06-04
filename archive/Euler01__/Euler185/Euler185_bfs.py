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
q = queue.Queue()
q.put(["", [0 for _ in data], 0])
maxsize = 0
while not q.empty():
    w, ls, s = q.get()
    if s > maxsize:
        print(w, ls, s)
        maxsize = s
        end = time.time()
        print("Time elapsed ", end - start, " seconds")
    flag = True
    for n1, n2 in zip(ls, data):
        if n1 > n2[1] or n1 + N - s < n2[1]:
            flag = False
            break
    if flag:
        if s == N:
            print(w)
            q.queue.clear()
            break
        for c in chrs:
            lsa = ls[:]
            for index, nw in enumerate(data):
                if nw[0][s] == c:
                    lsa[index] += 1
            q.put([w+c, lsa, s+1])


end = time.time()
print("Time elapsed ", end - start, " seconds")