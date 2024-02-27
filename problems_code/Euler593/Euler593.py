import time
start = time.time()
from ...CL.CL_Primes import MillerRabin
from ...CL.CL_Arithmetics import PowerMod


class MinHeap:
    def __init__(self, list):
        pass


class MaxHeap:
    def __init__(self, list):
        self.elements = list[:]
        self.elements.sort(reversed = True)#sorting a list is the easiest way to put it in a heap position.
        self.nelements = len(list)
        self.hash = {}
        if self.nelements == 0:
            self.empty = True
            self.elements = []
            self.hash = {}
            return
        self.empty = False
        for i in range(self.nelements):
            AddToDic(self.hash, self.elements[i], i)


    
    def insert(self, ele):
        index = self.nelements - 1
        self.nelements += 1
        self.elements += [ele]
        AddToDic(self.hash, ele, index)
        while index > 0:
            pindex = parent(index)
            if self.elements[pindex] > ele:
                return
            self.elements[index] = self.elements[pindex]
            self.elements[pindex] = ele
            ReplaceInDic(self.hash, self.elements[index], pindex, index)
            ReplaceInDic(self.hash, ele, index, pindex)
            index = pindex
    
    def remove(self, ele):
        index1 = self.hash[ele][0]
        index2 = self.nelements - 1
        p1 = parent(index1)
        p2 = parent(index2)
        while not index1 == index2:
            if index1 < index2:
                if self.elements[child(p2)] < self.elements[child(p2)+1]:


        self.nelements -= 1

def parent(i):
    return (i+1)//2

def child(i):
    return 2*i+1

def AddToDic(dic, ele, index):
    if ele in dic:
        dic[ele] += [index]
    else:
        dic[ele] = [index]

def ReplaceInDic(dic, ele, indexFrom, indexTo):
    if ele in dic:
        i = dic[ele].index(indexFrom)
        dic[ele][i] = indexTo


def RemFromDic(dic, ele, index):
    if ele in dic:
        dic[ele].remove(index)



N = 10**7
K = 10**5

def PrimesUpTo(LIM):
    primes = [2, 3]
    l = 1
    i = 3
    while l < LIM:
        i += 2
        if MillerRabin(i):
            primes.append(i)
            l += 1
    return primes

PRIMES = PrimesUpTo(N+500)
print("Primes computed, there are ", len(PRIMES), " primes")
end = time.time()
print("Time elapsed ", end - start, " seconds")

def S(k):
    return PowerMod(PRIMES[k-1], k, 10007)

def S2(k):
    return S(k) + S(1+k//10000)

def Median(ls):
    l = len(ls)
    lst = ls[:]
    lst.sort()
    if l == 0:
        raise Exception("empty list has no median")
    return (lst[l//2] + lst[(l-1)//2])/2


def F(n, k):
    print("Computing F for ", n, k)
    s2list = [S2(i) for i in range(n+1)]
    lst1st = s2list[:k]
    lst1st.sort()
    minheap = MaxHeap(lst1st[:k//2])
    maxheap = MinHeap(lst1st[k//2:])
    ans = 0
    for i in range(1, n-k+2):
        if i%k == 4141%k:
            print(i)
        ans += Median(s2list[i:i+k])
    return ans


print("Answer = ", F(N, K))
end = time.time()
print("Time elapsed ", end - start, " seconds")