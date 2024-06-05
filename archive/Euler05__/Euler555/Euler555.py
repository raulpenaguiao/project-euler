# Code written on the 2024/05/29
# Recursive formula can be show to satisfy, for $n \leq m$, that $M_{m, k, s}(n) = n - s + (k-s)(q + 1)$ where $q = \lfloor\frac{m-n}{k-s} \rfloor$
# With this we can show what the fixed points of $M_{m, k, s}$ are 
# If $s-k|s$, they are precisely $m-2s+k-i$ for $i=0, \ldots, k-s-1$.
# Otherwise there are no fixed points
# Summing all these up gives us the formula $SF(m, k, s) = \frac{l(2(m-s)+l+1)}{2}$, where $l = k-s$ divides $s$
# Further grouping the sum over all $s$ and using triangular forumla gets us, if we set $q = \lfloor\frac{m-n}{k-s} \rfloor$, that
# $$S(m, p) = \sum_{l=1}^p \frac{1}{2} (q-1)(l(l+1) + 2lm - l^2q) $$
# Further improvements can be done because this sum is a triangular sum with using $l = q*p+r$ and iterating over $a$ and $r$.
# Runs in 0.13 seconds


import time
start = time.time()
ans = 0

def S(m, p):
    ans = 0
    for l in range(1, p+1):
        q = p//l
        l2 = l*l
        ans += (q-1)*(l2+l + 2*l*m - q*l2)
    return ans//2

EXP = 6
m = 10**EXP
p = 10**EXP
print("Answer = ", S(m, p))
end = time.time()
print("Time elapsed ", end - start, " seconds")