#Code written on the 2024/06/07
#Dynamic programming computes four important quantities. Let $s(k)$ be the sum of digits of $k$, and $n(k)$ be the number of its digits.
#Note that $s(0) = n(0) = 0$. The following sum runs over non-negative integers
#$Q_0(n, s) = \sum_{n(l) = n, s(l) = s} 1$
#$Q_1(n, s) = \sum_{n(l) = n, s(l) = s} l$
#$T_0(n, s) = \sum_{n(l) = n, s(l) \leq s} 1$
#$T_1(n, s) = \sum_{n(l) = n, s(l) \leq s} l$
#These quantities satisfy a recursive relation, and its dimensions are $(n+1)\times(9n+1)$, where $n$ is the maximal number of digits we are considering.
#In this way, the number of balanced integers with exactly $2h$ digits is 
#$\sum_s 10^h \cdot T_0(h, s) \cdot Q_1(h, s) + 10^{0} \cdot T_1(h, s) \cdot Q_0(h, s)$
#And with exactly $2h+1$ digits is
#$\sum_s 10^{h+1}\cdot 10 \cdot T_0(h, s) \cdot Q_1(h, s) + 10^h\cdot 45 \cdot T_0(h, s) \cdot Q_0(h, s) + 10^{0}\cdot 10 \cdot T_1(h, s) \cdot Q_0(h, s)$
#Runs in 19 miliseconds


import time
start = time.time()
ans = 0

def GenDPLists(n, mod):
    maxsum = 9*n
    Q0 = [[0 for _ in range(maxsum + 1)] for _ in range(n+1)]
    Q1 = [[0 for _ in range(maxsum + 1)] for _ in range(n+1)]
    T0 = [[0 for _ in range(maxsum + 1)] for _ in range(n+1)]
    T1 = [[0 for _ in range(maxsum + 1)] for _ in range(n+1)]

    #initialize grids
    T0[0][0] = 1
    Q0[0][0] = 1
    if n >= 1:
        for s in range(10):
            if s > 0:
                Q0[1][s] = 1
                Q1[1][s] = s
            T0[1][s] = 1
            T1[1][s] = s
    
    #Recursion relation
    for m in range(1, n):
        for s in range(maxsum+1):
            for l in range(s, max(-1, s-10), -1):
                Q0[m+1][s] += Q0[m][l]
                Q0[m+1][s] %= mod
                Q1[m+1][s] += Q1[m][l]*10 + Q0[m][l]*(s-l)
                Q1[m+1][s] %= mod
                T0[m+1][s] += T0[m][l]
                T0[m+1][s] %= mod
                T1[m+1][s] += T1[m][l]*10 + T0[m][l]*(s-l)
                T1[m+1][s] %= mod
    return Q0, Q1, T0, T1

def T(N, mod):
    Half = N//2
    Q0, Q1, T0, T1 = GenDPLists(Half, mod)
    ans = 0
    pow10 = [1]
    for _ in range(Half+1):
        pow10 += [pow10[-1]*10]
        pow10[-1] %= mod
    
    for half in range(1, Half+1):#n even
        for s in range(half*9+1):
            ans += T0[half][s]*Q1[half][s]*pow10[half] + T1[half][s]*Q0[half][s]
            ans %= mod
    if N%2 == 0:
        Half -= 1
    for half in range(Half+1):#n odd
        for s in range(half*9+1):
            ans += pow10[half+1]*T0[half][s]*Q1[half][s]*10 + pow10[half]*Q0[half][s]*T0[half][s]*45 + T1[half][s]*Q0[half][s]*10
            ans %= mod
    return ans    

print("Answer = ", T(47, 3**15))
end = time.time()
print("Time elapsed ", end - start, " seconds")