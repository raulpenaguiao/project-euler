import time
start = time.time()
ans = 0


def E(N, M):
    int_sum = 0
    for i in range(1, N+1):
        int_sum += ((N*N - 4 * i * (N-i+1) + 2)**M)/((N*N)**M)
    return (N+int_sum)/2

ans = E(10**3, 4000)
#ans = E(10**10, 4000)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")