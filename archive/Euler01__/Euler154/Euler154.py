#code written on the 2023/11/03
#Once can compute very efficiently the largest exponent p^t that divides n! (v(p, n) function)
#Very directly computes the exponent of 2 and 5 of binom[N, (a, b, c)] and checks if these are >= 12
#Check the fives condition before checking the twos condition
#runs in 7.8 minutes = 470 seconds

import time
import math
start = time.time()
ans = 0


def v(p, n):
    m = n
    ans = 0
    while(m>1):
        m //= p
        ans += m
    return ans



N = 200000

"""
binom = [[0 for _ in range(i+1)] for i in range(N+1)]
binom[0][0] = 1
for n in range(1, N+1):
    binom[n][0] = 1
    binom[n][n] = 1
    for i in range(1, n):
        binom[n][i] = binom[n-1][i] + binom[n-1][i-1]
count = 0
tt = 0
for i in range(N+1):
    for j in range(N-i+1):
        tt += 1
        if (binom[N][i]*binom[N-i][j])%2 == 0:
            count += 1
print(tt, count)"""


vvec2 = [v(2, n) for n in range(N+1)]
vvec5 = [v(5, n) for n in range(N+1)]
N2 = vvec2[N]
N5 = vvec5[N]

for i in range(N+1):
    for j in range(max(2*i-N, 0), i//2+1):
        if(N5 >= vvec5[N-i]+vvec5[i-j]+vvec5[j] + 12) and (N2 >= vvec2[N-i]+vvec2[i-j]+vvec2[j] + 12):
            if(N-i == i-j):
                if(i-j == j):
                    ans += 1
                else:
                    ans += 3
            else:
                if(i-j == j):
                    ans += 3
                else:
                    ans += 6

print("N = ", N, ", answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")