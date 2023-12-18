import time
start = time.time()
import math
N = 13
poss = [{tuple([]):1}]
mix = {}

def AddDics(d1, d2):
    ans = {}
    for k in d1:
        if not k in d2:
            ans[k] = d1[k]
        else:
            ans[k] = d1[k] + d2[k]
    for k in d2:
        if not k in d1:
            ans[k] = d2[k]
    return ans
def Rest(tpl):
    return tpl[1:]
def PrependToKeys(dic, v):
    ans = {}
    for k in dic:
        ans[tuple([v] + list(k))] = dic[k]
    return ans
def Mix(a1, a2):#Gives a dictionary of pairs (a, v), where a is a tuple and v is the number of occurrences of this tuple in the mix
    if (a1, a2) in mix:
        return mix[(a1, a2)] 
    if a1 == tuple([]):
        mix[(a1, a2)] = {a2: 1}
        return {a2: 1}
    if a2 == tuple([]):
        mix[(a1, a2)] = {a1: 1}
        return {a1: 1}
    m1 = PrependToKeys(Mix(Rest(a1), a2), a1[0])
    m2 = PrependToKeys(Mix(a1, Rest(a2)), a2[0])
    m = AddDics(m1, m2)
    mix[(a1, a2)] = m
    return m
def AddToDic(dic, key, val):
    if key in dic:
        dic[key] += val
    else:
        dic[key] = val 
def MaxSegments(alpha):
    m = 0
    mx = 0
    for a in alpha:
        m += a
        if m > mx:
            mx = m
    return mx
def Fac(N):
    if N == 0:
        return 1
    return N*Fac(N-1)
for n in range(1, N+1):
    print("n = ", n)
    poss+= [{}]
    for j in range(n):
        k = n-1-j
        for a1 in poss[j]:
            for a2 in poss[k]:
                #print("a1 = ", a1, " and  a2 = ", a2)
                mx = Mix(a1, a2)
                for mxtpl in mx:
                    if j == 0 and k == 0:
                        mxAtpl = tuple(list(mxtpl)+ [1])
                    elif j == 0 or k == 0:
                        mxAtpl = tuple(list(mxtpl)+ [0])
                    else:
                        mxAtpl = tuple(list(mxtpl)+ [-1])
                    AddToDic(poss[n],mxAtpl,mx[mxtpl]*poss[j][a1]*poss[k][a2])
average = 0
for alpha in poss[N]:
    #print("alpha = ", alpha, " with ", poss[N][alpha], " values.")
    average += poss[N][alpha]*MaxSegments(alpha)
print("Answer = ", average/Fac(N))
end = time.time()
print("Time elapsed ", end - start, " seconds")