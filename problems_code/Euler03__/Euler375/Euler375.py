import time
start = time.time()
ans = 0

s = 290797
mod = 50515093
Mindex = 0
firstRepeat = 0
dic = {}
seq = []
while not s in dic:
    seq.append(s)
    dic[s] = True
    s = s*s%mod
firstRepeat = s

s = 290797
mindex = 0
while not s == firstRepeat:
    s = s*s%mod
    mindex += 1



print("Answer = ", mindex, Mindex)
end = time.time()
print("Time elapsed ", end - start, " seconds")