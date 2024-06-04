# Code written on the 2024/05/31
# The order in which the operations are performed is irrelevant, as long as we always topple beans to the right when the left pile is higher
# Divide and conquer method: we perform the toppling process on each half of the array independently
# Then we perform a last avalanche from the left half to the right half
# For that, we do a binary search to figure out what is the height in the middle after the avalanche
# We can see if this height is enough or not in linear time, so complexity of job is $n \log n$
# Runs in 165.09 seconds



import time
start = time.time()

N = 5#0
N = 6#14263289
N = 100#3284417556
N = 10**7

MOD = 50515093
S = [ 290797 ]
for _ in range(N-1):
    S.append((S[-1]**2)%MOD)



def TestStir(l1, l2):    
    l1cum = [0 for _ in l1]
    l2cum = [0 for _ in l2]
    l1cum[0] = l1[0]
    for i in range(len(l1) - 1):
        l1cum[i+1] = l1cum[i] + l1[i+1]
    l2cum[0] = l2[0]
    for i in range(len(l2) - 1):
        l2cum[i+1] = l2cum[i] + l2[i+1]
    if not(l1cum[len(l1)-1] == l2cum[len(l2)-1]):
        print(l1, l2, "Sums dont match")
    for i in range(len(l2) - 1):
        if l2[i] > l2[i+1]:
            print(l1, l2, "Decreasing sequence")
        elif l2cum[i] > l1cum[i]:
            print(l1, l2, i, "Cumulative sum criteria not met")
        elif l2[i] < l2[i+1] - 1 and l2cum[i] < l1cum[i]:
            print(l1, l2, i, "Minimality criteria not met")



def BinarySearch(lst, trg, lb, ub):
    #Returns largest index i st lst[i] <= trg
    #print("Binary search for (lst, trg, lb, ub) = ", lst, trg, lb, ub)
    while(ub-lb > 1):
        mb = (ub+lb)//2
        if lst[mb] > trg:
            ub = mb
        else:
            lb = mb
    #print("Binary search answer ", lb)
    return lb


def AvalancheDiff(l1, l2, val):
    #print("Avalanche difference for (lst1, lst2, val) = ", l1, l2, val)
    ans = 0
    for l in reversed(l1):
        if l > val:
            ans += l-val
        else:
            break
    for l in l2:
        if l < val:
            ans -= val-l
        else:
            break
    #print("Avalanche difference answer ", ans)
    return ans


def AvalancheMerge(l1, l2):
    #Find level of avalange via binary search
    #print("Avalanche Merge for (l1, l2) = ", l1, l2)
    ub = l1[-1]+1
    lb = l2[0]
    cum = 0
    while(ub-lb > 1):
        mb = (ub+lb)//2
        cum = AvalancheDiff(l1, l2, mb)
        if cum >= 0:
            lb = mb
        else:
            ub = mb
    lc1 = l1[:]
    for index, item in enumerate(lc1):
        if item > lb:
            lc1[index] = lb
    lc2 = l2[:]
    for index, item in enumerate(lc2):
        if item < lb:
            lc2[index] = lb
    ans = lc1 + lc2
    cum = AvalancheDiff(l1, l2, lb)
    index = BinarySearch(ans, lb, 0, len(ans))
    counter = 0
    #print(index, cum)
    while(counter < cum):
        ans[index] += 1
        counter += 1
        index -= 1
    #print("Avalanche Merge answer ", ans)
    #TestStir(l1+l2, ans)
    return ans


def ListAvalancheMerge(lst):
    l = len(lst)
    if l <= 2:
        if l == 1:
            return lst[0]
        return AvalancheMerge(lst[0], lst[1])
    mp = l//2
    return AvalancheMerge(ListAvalancheMerge(lst[:mp]), ListAvalancheMerge(lst[mp:]))


def Stir(lst):
    return ListAvalancheMerge([[k] for k in lst])


T = Stir(S)
TestStir(S, T)


cumSumS = 0
cumSumT = 0
ans = 0
for s, t in zip(S, T):
    cumSumS += s
    cumSumT += t
    ans += cumSumS - cumSumT


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")