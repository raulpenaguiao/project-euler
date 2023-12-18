#Code written on the 07/12/2023

#Expected to run in 7 days

import time
start = time.time()
import queue
ans = 0


seqs = []
seqs.append([2, 5, 32, 10**11, 126])
seqs.append([2, 7, 26, 10**11, 126])
seqs.append([2, 9, 444, 10**11, 1778])
seqs.append([2, 11, 1628, 10**11, 6510])
seqs.append([2, 13, 5906, 10**11 ,23622])
seqs.append([2, 15, 80, 10**11, 510])
seqs.append([2, 17, 126960, 10**11, 507842])
seqs.append([2, 19, 380882, 10**11, 1523526])
seqs.append([2, 21, 2097152, 10**11, 8388606])

def UlamSeq(a, b, lm):
    dic = {a:1, b:1}
    ans = [a, b]
    q = queue.PriorityQueue()
    q.put(a+b)
    dic[a+b] = True
    count = 2
    while not q.empty():
        s = q.get()
        if dic[s]:
            count += 1
            if count == lm:
                return s
            if count%9839 == 3132:
                print(a, b, lm, count, s)
            for i in ans:
                nv = i+s
                if nv in dic:
                    dic[nv] = False
                else:
                    dic[nv] = True
                    q.put(nv)
            ans.append(s)
        del dic[s]


for a, v, N, k, D in seqs:
    print("v = ", v, " and we are computing a Ulam sequence of size ", k%N+N)
    ulEl = UlamSeq(a, v, k%N+N)
    ans += ulEl + D*(k//N - 1)
    end = time.time()
    print("Time elapsed ", end - start, " seconds,  - ans = ", ans)

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")