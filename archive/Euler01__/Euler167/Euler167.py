#Code written on the 18/06/2024
#Ulam sequences were studied already, and here is what we know for sequences starting with 2:
#   the differences are eventually periodic
#   there are only two even terms in the sequence
#   any other term is the sum of an even term and an odd term in the sequence
#   the periods were studied for all the given sizes and can be found here: S. Finch. Patterns in 1-additive Sequences. Experimental Mathematics, 1(1):57–63, 1992
#Expected to run in 7.805 seconds

import time
start = time.time()
import queue
ans = 0


seqs = []
seqs.append([5, 32, 10**11])
seqs.append([7, 26, 10**11])
seqs.append([9, 444, 10**11])
seqs.append([11, 1628, 10**11])
seqs.append([13, 5906, 10**11])
seqs.append([15, 80, 10**11])
seqs.append([17, 126960, 10**11])
seqs.append([19, 380882, 10**11])
seqs.append([21, 2097152, 10**11])

def AddToDic(val, dic):
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1

def UlamSeq2(v, per):
    EVEN = 2*v+2
    vis = {}
    mantissa = [0, 2] + [i for i in range(v, EVEN, 2)] + [EVEN]
    period = [0 for _ in range(per+1)]
    q = queue.PriorityQueue()
    for k in range(v, EVEN, 2):
        vis[k+2*v+2] = 1
        q.put(k+2*v+2)
    vis[2*v+3] = 1
    q.put(2*v+3)
    counter = 0
    while not q.empty():
        s = q.get()
        if vis[s] > 1:
            continue
        period[counter] = s
        counter += 1
        if counter == per+1:
            return mantissa, period[:-1], period[-1]-period[0]
        AddToDic(s+2, vis)
        q.put(s+2)
        AddToDic(s+EVEN, vis)
        q.put(s+EVEN)


for v, per, k in seqs:
    mant, period, D = UlamSeq2(v, per)
    x = (k-len(mant))//per
    c = (k-len(mant))%per
    if k > len(mant):
        ulEl = period[c]
        ans += ulEl + D*x
    else:
        ans += mant[k]

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")