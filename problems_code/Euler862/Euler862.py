import time
start = time.time()

def digits(n, base = 10):
    if n < base:
        return [n]
    return [n//base, n%base]


def fromDigits(digs, base = 10):
    l = len(digs)
    powBase = 1
    ans = 0
    for i in range(l-1, -1, -1):
        ans += powBase*digs[i]
        powBase *= base
    return ans


def Partitions(parts, size):
    if parts == 1:
        return [[size]]
    ans = []
    for s in range(size):
        smallerParts = Partitions(parts - 1, s)
    ans = []
    for p in smallerParts:


ans = 0

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")