#P(x) = \sum_{k\geq 0} p(k) x^k = \prod_{l\geq 0} (1 + x^(2^l) + (x^(2^l))^2 + (x^(2^l))^3 + ... 
#= \prod_{l\geq 0} ( 1 - x^(2^l))^{-1}

#P(x^2) = P(x)  * ( 1 - x ) so 
#taking the x^{2k} coefficient gives us p(x) = p(2k) - p(2k - 1)
#taking the x^{2k + 1} coefficient gives us 0 = p(2k + 1) - p(2k)

#This recursive formula tells us that 



import time
start = time.time()
ans = 0
MOD = 10**9 + 7

def p(n):
    p = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        if i%2 == 0:
            p[i] = p[i-1] + p[i//2]
        else:
            p[i] = p[i-1]
    return p[n]

print("Answer = ", p(7**7)%MOD)
end = time.time()
print("Time elapsed ", end - start, " seconds")