import time
import math

start_time = time.time()


N = 10 ** 16
LIM = math.floor(math.sqrt(N / 40.75))
tot = -1
#We should not count (x, y) = (0, 0)


for y in range(-LIM, LIM+1):
    s = math.sqrt(N - 40.75 * y * y)
    add = 2 * math.floor(s) + 1
    tot += add
    #print(" y = ", y, " and s = ", s)
    if y%2 == 1:
        if s - math.floor(s) < 0.5:
            tot -= 1
        else:
            tot += 1

print("tot =", tot)
print(" ---%s seconds --- "%(time.time() - start_time))
