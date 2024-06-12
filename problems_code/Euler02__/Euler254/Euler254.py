import time
start = time.time()
from ....CL.CL_Partitions import GeneratePartitionsInSquare

fact = [1]
for i in range(1, 10):
    fact.append(i*fact[-1])


def PartScore(part):
    return sum(digits(sum([fact[p] for p in part])))


def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]


def FromDigits(lst, base = 10):
    if lst == []:
        return 0
    return FromDigits(lst[:-1])*base + lst[-1]

def SmallestNumToPart(part):
    modPart = part[:]
    modPart.sort()
    l = len(modPart)
    for i in range(l):
        if i > 0 and modPart[i] == 1:
            modPart[i] = 0
        if modPart[i] > 1:
            break
    #print(part,  " _ ", modPart, " _ ", FromDigits(modPart))
    return FromDigits(modPart)


def gs(n):
    part = []
    currSum = 0
    index = 9
    while(currSum < n):
        vals = (n-currSum)//fact[index]
        part = [[index, vals]] + part
        currSum += vals*fact[index]
    return part


    





N = 150
g = [0 for _ in range(N+1)]
g_vis = [False for _ in range(N+1)]
g[0] = True

sizePartitions = 10
counter = 1
while counter < N:
    for parts in GeneratePartitionsInSquare(sizePartitions, 9):
        for part in parts:
            score = PartScore(part)
            if score > N:
                continue
            num = SmallestNumToPart(part)
            if not g_vis[score]:
                g_vis[score] = True
                counter += 1
            if g[score] == 0 or g[score] > num:
                #print(part, " visited ", score, " _ ", num)
                g[score] = num
    print(sizePartitions, " with counter = ", counter)
    print(g[:40])
    sizePartitions += 1


ans = sum([sum(digits(gi)) for gi in g])
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")