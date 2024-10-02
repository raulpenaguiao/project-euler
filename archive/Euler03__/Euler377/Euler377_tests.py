# note the sequence https://oeis.org/A211072, this is the thing that we are interested in

import time
start = time.time()
ans = 0

LIM = 100
binom = [[0 for _ in range(LIM)] for _ in range(LIM)]
for i in range(LIM):
    binom[0][i] = 1
    binom[i][0] = 1
for n in range(1, LIM):
    for i in range(1, n):
        binom[n][i] = binom[n-1][i] + binom[n-1][i-1]

def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]

def F(n):
    ans_F = 0
    for i in range(1, 10**n):
        digs = digits(i)
        if sum(digs) == n and not(0 in digs):
            ans_F += i
    return ans_F

def Binom(n, k):
    if n < 0 or k > n:
        return 0
    if n >= LIM:
        print("ERROR")
    return binom[n][k]

def f(n):
    ans_f = 0
    for k in range(1, n+1):
        for l in range(1, k+1):
            ans_f += Binom(k, l)*Binom(n-9*l-1, k-1)
    return ans_f

#Testing the fact from OEIS that says the sequence satisfies a recurrence relation
def f_eff_list(n, MOD = 10**9):
    dp_f = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp_c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp_c[0][0] = 1
    for m in range(1, n+1):
        for k in range(1, m + 1):
            for d in range(1, min(9, m)+1):
                dp_c[m][k] += dp_c[m-d][k-1]
                dp_c[m][k] %= MOD
                dp_f[m][k] += dp_f[m-d][k-1] + d*10**(k-1)*dp_c[m-d][k-1]
                dp_f[m][k] %= MOD
    return [sum(r)%MOD for r in dp_f]

coeffs = [11,1,-9,-19,-29,-39,-49,-59,-69,-90,-80,-70,-60,-50,-40,-30,-20,-10]
l = len(coeffs)
num = 22
lst = f_eff_list(num)

print(lst)
print([sum([coef*seq for coef, seq in zip(coeffs, lst[a+l:a:-1])])%10**9 for a in range(num-l)])

for a in range(num-l):
    print("Index = ", a+l, a)
    acc = 0
    for coef, seq in zip(coeffs, lst[a+l:a:-1]):
        acc += coef*seq
        acc %= 10**9
        print(coef, seq, acc)

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")