import time
import math

b_time = time.time()
LIM = 21
tens_sum = []

duo_list = []
p_10 = 1
p_10_s = 1
for exp in range(LIM):
    for j in range(1, 10):
        ## iterate powers of two
        for s in tens_sum:
            for k in range(10):
                if not(k == j):
                    duo_list += [j * p_10_s + (k - j)*s]    
        duo_list += [j*p_10_s]
    tens_sum += [l+p_10 for l in tens_sum]
    tens_sum += [p_10]
    tens_sum.sort()
    p_10 *= 10
    p_10_s+= p_10

duo_list.sort()
m = len(duo_list)
print(m)
def d(n):
    i = 0
    while i < m:
        if duo_list[i]%n == 0:
            return duo_list[i]
        i += 1
    print("d(", n, ") was not found")
    return 0

def D(N):
    tot = 0
    for i in range(1, N+1):
        tot += d(i)
    return tot

print(D(50000))
#print(d(32570))
print("Time ellapsed:", (math.floor((time.time() - b_time)*10_000_000)/10000), "ms")
