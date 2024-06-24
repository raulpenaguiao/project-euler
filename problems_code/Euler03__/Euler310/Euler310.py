import time
start = time.time()
from math import floor, sqrt
ans = 0

def strat1D(LIM):
    hasNoStrat = [[True for _ in range(LIM+1)] for _ in range(LIM+1)]
    squares = [i*i for i in range(1, floor(sqrt(LIM)+.01)+1)]
    for i in range(LIM+1):
        if hasNoStrat[i]:
            for sq in squares:
                next = i + sq
                if next <= LIM:
                    hasNoStrat[next] = False
    ans = []
    for index, item in enumerate(hasNoStrat):
        if item:
            ans.append(index)
    return ans

print(strat1D(100))


def strat3D(LIM):
    hasNoStrat = [[[True for _ in range(LIM+1)] for _ in range(LIM+1)] for _ in range(LIM+1)]
    #hasNoStrat[a][b][c] = True if the first player has no strategy
    squares = [i*i for i in range(1, floor(sqrt(LIM)+.01)+1)]
    for i in range(LIM+1):
        for j in range(LIM+1):
            for k in range(LIM+1):
                if hasNoStrat[i][j][k]:
                    for sq in squares:
                        next = i + sq
                        if next <= LIM:
                            hasNoStrat[next][j][k] = False
                        next = j + sq
                        if next <= LIM:
                            hasNoStrat[i][next][k] = False
                        next = k + sq
                        if next <= LIM:
                            hasNoStrat[i][j][next] = False
    return hasNoStrat

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")