#Code written on the 2024/06/10
#For $n = 3 mod 4$, we can show that $f(n, k)$ is always even
# Indeed, by performing a shift $s \mapsto n - s + 1$, we obtain another set with the same parity.
# This will be the same set as the original one if total sum is a multiple of $\frac{n+1}{2}$, which is even.
#For $n = 1 mod 4$ and $k = 3 mod 4$ we can show that $f(n, k)$ is always even. Let $m = \frac{n-1}{2}$, which is necessarily even.
# Indeed, the previous pairing between sets will have some fixed points: the sets that contain $m+1$, plus exactly $j = \frac{k-1}{2}$ pairs of the form $s, n - s + 1$
# There are $\binom{m}{j}$ such pairs, which is necessarily an even number because $m$ is even and $j$ is odd.
#For $n = k = 1 mod 4$, by the previous reasoning $f(n, k)$ has the parity of $\binom{m}{j} = \binom{(m-1)/2}{(j-1)/2} mod 2$
#Therefore, the number of desired odd triplets with $n < N$ is the number of pairs $j_0 \leq m_0 < \frac{N}{4}$ such that $\binom{m_0}{j_0}$ is odd.
#Runs in 0 ms


import time
start = time.time()
ans = 0

def digits(n, base = 2):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]

def F(m):
    n = (m-1)//4 + 1
    digs = digits(n)
    l = len(digs)
    ans = 0
    pow2 = 1
    for i in range(l):
        if digs[i] == 1:
            ans += 3**(l-i-1)*pow2
            pow2 *= 2
    return ans

print("Answer = ", F(10**12))
end = time.time()
print("Time elapsed ", end - start, " seconds")