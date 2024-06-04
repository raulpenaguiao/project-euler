#This is to compare the algorithm found in "the use of bit and byte manipulation in computing summation sequences" with the one I came up with

import time
start = time.time()
import queue


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
