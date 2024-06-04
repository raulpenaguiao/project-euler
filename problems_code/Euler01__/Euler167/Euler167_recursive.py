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

def UlamBetaVec(a, b, per, mod, k):
    dic = {a:1, b:1}
    ans = [a, b]
    UB = 100
    beta = [0 for _ in range(1, UB+1, 2)]
    if a%2 == 1:
        beta[a//2] = 1
    if b%2 == 1:
        beta[b//2] = 1
    q = queue.PriorityQueue()
    q.put(a+b)
    dic[a+b] = True
    while not q.empty():
        s = q.get()
        if s > UB:
            break
        if dic[s]:
            for i in ans:
                nv = i+s
                if nv%2 == 1 and nv <= UB:
                    print(nv)
                    beta[nv//2] += 1
                if nv in dic:
                    dic[nv] = False
                else:
                    dic[nv] = True
                    q.put(nv)
            ans.append(s)
        del dic[s]
    return beta


print(UlamBetaVec(2, 5, 32, 100, 100))


end = time.time()
print("Time elapsed ", end - start, " seconds")