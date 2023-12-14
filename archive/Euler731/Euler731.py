import time
import math

start_time = time.time()


def power_mod(a, p, m):
    if p == 0:
        return 1
    if a == 1:
        return 1
    if p%2 == 0:
        return power_mod((a*a)%m, p//2, m)
    return (a*power_mod((a*a)%m, p//2, m))%m


def order(i):# Gives the order of 10 module 3**i
    if i < 3:
        return 1
    t = order(i-1)
    p3 = 3**i
    p = power_mod(10, t, p3)
    p10 = p
    count = t
    while p10 > 1:
        count += t
        p10 *= p
        p10 %= p3
    return count

LIM = 10**16
lim = math.log(LIM)/math.log(3)
lim = math.floor(lim)
print("lim = ", lim)

ord_list = [order(i) for i in range(lim)]

term = 1
power = 3
LIM = 10 ** 5


while power < LIM:
    power *= 3
    term += 1

#A = sum_i (3^i 10^(3^i))^-1

#The decimal expantion of the i-th term is controled by the smallest m>0 s.t. 3^i | 10^m - 1
#For i = 1, 2, m = 1 so the cycle expansion has length 1 
#For i > 2, m = 3^(i-2)
#The contribution to A(n) from i = 1 and i = 2, for n > 9, will be
ans = 4444444444

#i = 1 we have 10^-3 * 0.(3)
#i = 2 we have 10^-9 * 0.(1)
#i = 3 we have 10^-27* 0.(037)
#i = 4 we have 10^-81*0.(012345679)


i = 3
rem = 37
cyc = 3


print(" --- %s seconds --- "%(time.time() - start_time))
