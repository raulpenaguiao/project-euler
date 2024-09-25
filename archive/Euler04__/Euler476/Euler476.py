# Code written on the 2024/09/25
# Uses the greedy algorithm to iteratively find the largest circle that fits in the remaining space. This is shown to work here 
# Wiki: https://en.wikipedia.org/wiki/Malfatti_circles
# cite: "triangles a larger area can be achieved by a greedy algorithm"
# Runs in 4 minutes


import time
import math
start = time.time()
ans = 0
tot = 0

N = 1803


def f(a, b, c):
    a2 = a*a
    b2 = b*b
    c2 = c*c
    s = (a + b + c)/2
    alpha = math.acos((b2+c2-a2)/(2*b*c))
    beta = math.acos((a2+c2-b2)/(2*a*c))
    #because a < b < c we have alpha < beta < gamma
    r = math.sqrt((s-a)*(s-b)*(s-c)/s)
    sa = math.sin(alpha/2)
    sb = math.sin(beta/2)
    ra = r*(1 - 2*sa/(1 + sa))
    rb = r*(1 - 2*sb/(1 + sb))
    ra2 = ra*(1 - 2*sa/(1 + sa))
    if rb > ra2:
        return r*r+ra*ra+rb*rb
    return r*r+ra*ra+ra2*ra2


for a in range(1, N+1):
    for b in range(a, N-a+1):
        for c in range(b, a+b):
            tot += 1
            ans += f(a, b, c)

ans *= math.pi

print("Answer = ", ans/tot)
end = time.time()
print("Time elapsed ", end - start, " seconds")