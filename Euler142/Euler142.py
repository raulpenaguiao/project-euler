import time
import math

start_time = time.time()


def sqQ(n):
    t = math.sqrt(n)
    return int(t + 0.5)**2 == n


def checkabd(a_s, b_s, d_s):
    return sqQ(a_s+d_s) and sqQ(a_s+b_s+d_s)

LIMsq = 100
LIM = 1000
minimal_sum = 10**16

for d in range(2, LIM):
    for r in range(1, LIMsq):
        lim_m = math.sqrt(d/r+1)
        lim_m = math.floor(lim_m)
        for m in range(lim_m+1, LIMsq):
            lim_n = math.sqrt(m**2 - d/r)
            lim_n = math.ceil(lim_n)
            for n in range(lim_n, m):
                a = 2 * r * m * n
                b = r *(m**2 - n**2)
                if d%2 == b%2 and checkabd(a*a, b*b, d*d):
                    y = (d**2+b**2)//2
                    z = (d**2 - b**2)//2
                    x = y + a**2
                    if x + y + z < minimal_sum:
                        minimal_sum = x+y+z
                        print("x = ", x, " | y = ", y, " | z = ", z)
for d in range(2, LIM):
    for r in range(1, d//2):
        Lim_m = d/(2*r)
        Lim_m = math.floor(Lim_m)
        for m in range(1, Lim_m):
            Lim_n =d/(2*r*m)
            Lim_n = math.floor(Lim_n)+1
            Lim_n = min(Lim_n, m)
            for n in range(2, Lim_n):
                a = r * (m**2 - n**2)
                b = 2 * r * m * n
                if d%2 == b%2 and checkabd(a*a, b*b, d*d):
                    y = (d**2+b**2)//2
                    z = (d**2 - b**2)//2
                    x = y + a**2
                    if x + y + z < minimal_sum:
                        minimal_sum = x+y+z
                        print("x = ", x, " | y = ", y, " | z = ", z)

print(minimal_sum)
print(" --- %s seconds --- "%(time.time() - start_time))
