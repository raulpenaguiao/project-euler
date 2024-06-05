#Code written on the 11/12/2023
#Uses matrix multiplication to obtain the n-th value of the sequence
#The problem is that this matrix is 2000x2000
#Code expected to run in 10 hours


import time
start = time.time()
MOD = 20092010

def g(n):
    L = 2000
    A = [[0 for _ in range(L)]for _ in range(L)]
    for i in range(1, L):
        A[i-1][i] = 1
    A[L-1][0] = 1
    A[L-1][1] = 1
    m = n
    x = [[1] for _ in range(L)]
    while m > 0:
        if m%2 == 1:
            #Multiply x = Ax
            x = [[sum([A[i][k] * x[k][0] for k in range(L)])%MOD] for i in range(L)]
        A = [[sum([A[i][k]*A[k][j] for k in range(L)])%MOD for j in range(L)] for i in range(L)]
        m //= 2
    return x[0][0]


print("Answer = ", g(10**18))
end = time.time()
print("Time elapsed ", end - start, " seconds")