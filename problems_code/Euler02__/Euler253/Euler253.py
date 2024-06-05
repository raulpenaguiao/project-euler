import time
start = time.time()

LIM = 50
d = [ [ [ [ 0 for _ in range(LIM)] for _ in range(LIM)] for _ in range(3)] for _ in range(3)]
d[1][1][1][1] = 1



ans = 0
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")