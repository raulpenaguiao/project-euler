# Code written on the 2023/01/04
# This is a simple brute force program and memoisation.
# For each losing strategy, we can determine that all states that reach this point are winning strategies
# So run increasingly in the amount of stones in a pile, when finding a losing strategy mark all coresponding winning strategies
# Possible optimizations:
# - just run for a <= b <= c, would get a *6 improvement. 
# - Use C++, would get a 10* improvement
# - Cap the loop on k to the maximum value automatically, would get a *2 improvement
# Runs in 780 seconds

import time
start = time.time()
ans = 0


LIM = 1000
isLosing = [[[True for _ in range(LIM+1)] for _ in range(LIM+1)] for _ in range(LIM+1)]

def SetToWinning(a, b, c):
    if a <= LIM and b <= LIM and c <= LIM:
        isLosing[a][b][c] = False

for a in range(LIM+1):
    for b in range(LIM+1):
        for c in range(LIM+1):
            if isLosing[a][b][c]:
                if a <= b and b <= c:
                    ans += a + b + c
                for k in range(LIM+1):
                    SetToWinning(a + k, b, c)
                    SetToWinning(a, b + k, c)
                    SetToWinning(a, b, c + k)
                    SetToWinning(a + k, b + k, c)
                    SetToWinning(a + k, b, c + k)
                    SetToWinning(a, b + k, c + k)
                    SetToWinning(a + k, b + k, c + k)



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")