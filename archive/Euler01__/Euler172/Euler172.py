#Code written on 2023/12/01
#Dinamic programming, by counting the number of integers with a digits occurring trice, b digits occurring twice and c digits occurring once
#deleting the last digit gives us an easy recursive formula
#Runs in 3ms

import time
import math
start = time.time()

def f(N):
    nDigs = 10
    dp = [[[[0  for _ in range(nDigs+1)]for _ in range(nDigs+1)]for _ in range(nDigs+1)] for _ in range(2)]
    dp[1][0][0][1] = 9
    ans = 0
    for n in range(2, N+1):
        ans = 0
        for a in range(nDigs+1):
            for b in range(nDigs+1-a):
                for c in range(nDigs - a - b + 1):
                    d = nDigs - a - b - c
                    dp[n%2][a][b][c] = 0
                    if a > 0 and b < nDigs:
                        dp[n%2][a][b][c] += dp[(n-1)%2][a-1][b+1][c]*(b+1)
                    if b > 0 and c < nDigs:
                        dp[n%2][a][b][c] += dp[(n-1)%2][a][b-1][c+1]*(c+1)
                    if c > 0 and d < nDigs:
                        dp[n%2][a][b][c] += dp[(n-1)%2][a][b][c-1]*(d+1)
                    ans += dp[n%2][a][b][c]
    return ans

print("Answer = ", f(18))
#print("Proportions = ", [f(i)/(9*10**(i-1)) for i in range(2, 32)])
end = time.time()
print("Time elapsed ", end - start, " seconds")