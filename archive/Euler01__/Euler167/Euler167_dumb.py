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
seqs.append([2, 13, 5906, 10**11, 23622])
seqs.append([2, 15, 80, 10**11, 510])
#seqs.append([2, 17, 126960, 10**11, 507842])
#seqs.append([2, 19, 380882, 10**11, 1523526])
#seqs.append([2, 21, 2097152, 10**11, 8388606])

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

def UlamSeqAllTerms(a, b, lm):
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
                return ans
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
us = UlamSeqAllTerms(2, 5, 300)
print(us)
usDiff = [us[i+1] - us[i] for i in range(len(us)-1)]
print(usDiff)

def ListUlamSeq(a, b, UB):
    dic = {a:1, b:1}
    ans = [a, b]
    q = queue.PriorityQueue()
    q.put(a+b)
    dic[a+b] = True
    while not q.empty():
        s = q.get()
        if s > UB:
            return ans
        if dic[s]:
            for i in ans:
                nv = i+s
                if nv in dic:
                    dic[nv] = False
                else:
                    dic[nv] = True
                    q.put(nv)
            ans.append(s)
        del dic[s]


def LimUlamSeq(x, y, lm):
    V = [0]*(lm)
    W = [1]*(lm)
    V[x-1] = V[y-1] = 1
    W[x-1] = W[y-1] = 0
    k = 2
    while 2*k < lm:
        V[k:2*k-1] = [((not a) and b and c) or (a and (not b) and (not c)) or (a and (not b) and c) for a, b, c in zip(V[k:2*k-1], V[0:k-1], W[k:2*k-1])]
        W[k:2*k-1] = [(not a) and b for a, b in zip(V[0:k-1], W[k:2*k-1])]
        #print(V)
        L = [j for j in range(k+1, lm) if V[j-1] == 1] 
        if L == []:
            break
        else:
            k = min(L)
    return [i+1 for i, v in enumerate(V) if v == 1]

LimUlamSeq(2, 5, 40000)
end = time.time()
print("Time elapsed ", end - start, " seconds")

ListUlamSeq(2, 5, 40000)
end = time.time()
print("Time elapsed ", end - start, " seconds")

def DiffList(ls):
    l = len(ls)
    return [ls[i]-ls[i-1] for i in range(1, l)]

#print(DiffList(ListUlamSeq(2, 21, 1021)))
print(UlamSeq(2, 5, 3), UlamSeq(2, 5, 35))



for a, v, N, k, D in seqs:
    print("v = ", v, " and we are computing a Ulam sequence of size ", k%N+N)
    ulEl = UlamSeq(a, v, k%N+N)
    ans += ulEl + D*(k//N - 1)
    end = time.time()
    print("Time elapsed ", end - start, " seconds,  - ans = ", ans)

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")