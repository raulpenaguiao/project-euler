import time
start_time = time.time()


def conv(n):
    l = [[2, 1]]
    for i in range(n-1):
        an = l[-1][0]
        bn = l[-1][1]
        l += [[2 * an + 5*bn, an + 2* bn]]
    return l
n = 12000
convs = conv(n)
L = [c[1]*c[1] * 5 + 4 * c[0] * c[1] + c[0] * c[0]   for c in convs]
print(sum(L))

print("n = ", n, "--- %s seconds ---" % (time.time() - start_time))
