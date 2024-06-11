
def BinomList(lim):
    ans = [[0 for _ in range(lim+1)] for _ in range(lim+1)]
    for i in range(lim+1):
        ans[i][0] = 1
        ans[i][i] = 1
    for n in range(2, lim+1):
        for i in range(1, lim):
            ans[n][i] = ans[n-1][i] + ans[n-1][i-1]
    return ans

binom_LIM = 30
binom = BinomList(binom_LIM)

def Binom(n, k):
    if n < 0 or n < k or k < 0:
        return 0
    global binom_LIM
    global binom
    if n > binom_LIM:
        binom_LIM= n
        binom = BinomList(binom_LIM)
    return binom[n][k]