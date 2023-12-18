import time
import math
start = time.time()
ans = 0

Pieces = 10

T = [[[0 for _ in range(3)] for _ in range(Pieces+1)] for _ in range(Pieces+1)]
T[0][0][1] = 1
T[0][0][2] = 1

for s in range(1, Pieces):
    for M in range(Pieces + 1):
        T[s][M][0] = T[s-1][M][2]
        T[s][M][1] = T[s-1][M][0]
        if(M > 0):
            T[s][M][1] += T[s-1][M-1][0]
        T[s][M][2] = T[s][M][0] + T[s][M][1]

poss = 0
for i in range(Pieces):
    print(i, " - ", T[Pieces][i][2])
    poss += T[Pieces][i][2]

average = 0
for i in range(M):
    average += i * T[Pieces][M][2]/poss

print("Answer = ", average)
end = time.time()
print("Time elapsed ", end - start, " seconds")