import time
import math

start_time = time.time()
lis = []


def fun(x, y):
    tot = y * y - x * x - 1
    tot //= 2
    tot *= tot
    tot -= x * x
    #print("x = ", x, " | y = ", y, " | ans = ", tot // 4)
    return tot // 4

"""
for y in range(20):
    for x in range((y + 1)%2, y-1, 2):
        F = (y*y - x*x - 1) // 2
        N = (F * F - x * x) // 4
        #print("y = ", y, " | x = ", x, " | F = ", F , " | N = ", N)
        lis += [N]
lis.sort()
#print(" - ".join([str(i) for i in lis]))
"""


y = 3
stealth = set()
lim = 10 ** 14
big = fun(y-3, y)

while big <= lim:
    x = y - 3
    N = fun(x, y)
    while x >= 0 and N <= lim:
        stealth.add(N)
        x-= 2
        N = fun(x, y)
    y += 1
    big = fun(y-3, y)

print(len(stealth))
"""
lis = list(stealth)
lis.sort()
for key in lis:
    print(key)
"""





print(" --- %s seconds ---"%(time.time() - start_time))
