#Code written on the 2024/09/30
# note the sequence https://oeis.org/A211072, this is the thing that we are interested in. There, the recurrence relation is given, but this is not hard to derive
#Runs in 0.25 seconds


import time
start = time.time()
mod = 10**9


def mat_mult(mat1, mat2, len1, len2, len3, MOD):
    ans_mat = [[0 for _ in range(len3)] for _ in range(len1)]
    for i in range(len1):
        for j in range(len2):
            for k in range(len3):
                ans_mat[i][k] += mat1[i][j]*mat2[j][k]
    for i in range(len1):
        for k in range(len3):
            ans_mat[i][k] %= MOD
    return ans_mat


#Compute the initial vector
def f_list(n, MOD):
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


def f_eff(n, MOD):
    coeffs = [11,1,-9,-19,-29,-39,-49,-59,-69,-90,-80,-70,-60,-50,-40,-30,-20,-10]
    l = len(coeffs)
    curr_vec = [[k] for k in f_list(l-1, mod)]

    pow_trans_mat = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l-1):
        pow_trans_mat[i][i+1] = 1
    pow_trans_mat[l-1][:] = coeffs[::-1]
    m = n

    while(m > 0):
        if m%2 == 1:
            curr_vec = mat_mult(pow_trans_mat, curr_vec, l, l, 1, MOD)
        pow_trans_mat=mat_mult(pow_trans_mat, pow_trans_mat, l, l, l, MOD)
        m//=2
    return curr_vec[0][0]

print(sum([f_eff(13**i, mod) for i in range(1, 18)])%mod)
end = time.time()
print("Time elapsed ", end - start, " seconds")