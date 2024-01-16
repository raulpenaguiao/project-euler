#Code written on the 2024/01/16
#We generate all the numbers with digits 0, 1, 2
#For each such number, we see if it is a multiple of one of the numbers between 1 and 10_000
#We regularly shrink the list of missing numbers, so numbers that have a low 012 multiple are not hindering further computations.
#Runs in 2745.782 seconds, most of it is computing the value for 9999
#On a second run where I use the fact that f(9999)/9999 = 1111333355557778  (this can be guessed by the values of 999, 99 and 9)
#we get an answer in 33.9 seconds!


import time
start = time.time()
LIM = 10_000

flag = False
if LIM == 10_000:
    flag = True
    LIM = 9998

def FromBase3To10(n):
    if n < 3:
        return n
    return (n%3)+10*FromBase3To10(n//3)

count = 0
vis = [False for _ in range(LIM+1)]
toFind = [i for i in range(1, LIM+1)]
ans = 0
i = 1

while(count < LIM):
    fb3 = FromBase3To10(i)
    for k in toFind:
        if not vis[k] and fb3%k == 0:
            ans += fb3//k
            count += 1
            vis[k] = True
            if len(toFind) > 1.1*(LIM - count):
                toFind = [i for i in range(1, LIM + 1) if not vis[i]]
    i += 1

if flag:
    ans += 1111333355557779

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")