#Code written on the 2023/11/08
#recursively checks what are the numbers that can be obtained for capacity structures
#for precision reasons we use precise rational structure
#Run in 102.44 seconds


import time
import math
start = time.time()

N = 18


def RemoveCopies(lst):
    if lst == []:
        return []
    a = sorted(lst)
    ans = [a[0]]
    for i in range(1, len(a)):
        if not(a[i] == a[i-1]):
            ans.append(a[i])
    return ans


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)


def ReduceRational(l):
    if l[0] < 0:
        d = GCD(l[0], l[1])
        return [l[0]//d, l[1]//d]
    d = GCD(-l[0], -l[1])
    return [-l[0]//d, -l[1]//d]
    


def AddRationals(l1, l2):
    return ReduceRational([l1[0]*l2[1]+l1[1]*l2[0], l1[1]*l2[1]])


def InvertRational(l):
    return [l[1], l[0]]


caps = [[], [[1, 1]]]
for i in range(2, N+1):
    new_caps = []
    for j in range(1, i):
        for cap1 in caps[j]:
            for cap2 in caps[i-j]:
                new_caps.append(AddRationals(cap1,cap2))#paralel
                new_caps.append(InvertRational(AddRationals(InvertRational(cap1), InvertRational(cap2))))#series
    #print("i = ", i, " :: ",  new_caps)
    new_caps = RemoveCopies(new_caps)
    caps += [new_caps[:]]

all_caps = []
for c in caps:
    all_caps += c
all_caps = RemoveCopies(all_caps)
#print(all_caps)
#print(caps)

print("For N = ", N, " the answer = ", len(all_caps))
end = time.time()
print("Time elapsed ", end - start, " seconds")