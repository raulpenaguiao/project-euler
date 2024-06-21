#P(T = n) = sum_{a + 2b + 3c + 4d = n-1, L} P(seq arrives at (a, b, c, d, L)) * P(we get a pair now | seq arrives at (a, b, c, d, L))
# P(we get a pair now | seq arrives at (a, b, c, d, L)) = (4 - L)/(52 - a - 2b - 3c - 4d)
# P(seq arrives at (a, b, c, d)) = numCases(a, b, c, d, L)/ numSequences of size a + 2b + 3c + 4d

# monte carlo simulation 
# expectation = 17.097416584220394 
# prob no pairs showing = 0.045477436839857006

import time
start = time.time()
from decimal import Decimal, getcontext 
getcontext().prec = 40
ans = 0


numCases = [[[[[0 for _ in range(5)] for _ in range(14)] for _ in range(14)] for _ in range(14)] for _ in range(14)]
numCases[1][0][0][0][1] = 52
verbose = False
aTrack = 3
bTrack = 1
cTrack = 0
dTrack = 0
LTrack = 2

for n in range(2, 53):
    for d in range(14):
        if 4*d > n:
            continue
        for c in range(14):
            if 4*d+3*c > n:
                continue
            for b in range(14):
                if 4*d+3*c+2*b > n:
                    continue
                a = n - (4*d+3*c+2*b)
                if a > 13:
                    continue
                if a > 0:
                    numCases[a][b][c][d][1] += numCases[a - 1][b][c][d][1]*(13 - a - b - c - d + 1)*4
                    numCases[a][b][c][d][1] += numCases[a - 1][b][c][d][2]*(13 - a - b - c - d + 1)*4
                    numCases[a][b][c][d][1] += numCases[a - 1][b][c][d][3]*(13 - a - b - c - d + 1)*4
                    numCases[a][b][c][d][1] += numCases[a - 1][b][c][d][4]*(13 - a - b - c - d + 1)*4
                if b > 0 and a < 13:
                    numCases[a][b][c][d][2] += numCases[a + 1][b - 1][c][d][1]*(a + 1 - 1)*3
                    numCases[a][b][c][d][2] += numCases[a + 1][b - 1][c][d][2]*(a + 1)*3
                    numCases[a][b][c][d][2] += numCases[a + 1][b - 1][c][d][3]*(a + 1)*3
                    numCases[a][b][c][d][2] += numCases[a + 1][b - 1][c][d][4]*(a + 1)*3
                if c > 0 and b < 13:
                    numCases[a][b][c][d][3] += numCases[a][b + 1][c - 1][d][1]*(b + 1)*2
                    numCases[a][b][c][d][3] += numCases[a][b + 1][c - 1][d][2]*(b + 1 - 1)*2
                    numCases[a][b][c][d][3] += numCases[a][b + 1][c - 1][d][3]*(b + 1)*2
                    numCases[a][b][c][d][3] += numCases[a][b + 1][c - 1][d][4]*(b + 1)*2
                if d > 0 and c < 13:
                    numCases[a][b][c][d][4] += numCases[a][b][c + 1][d - 1][1]*(c + 1)*1
                    numCases[a][b][c][d][4] += numCases[a][b][c + 1][d - 1][2]*(c + 1)*1
                    numCases[a][b][c][d][4] += numCases[a][b][c + 1][d - 1][3]*(c + 1 - 1)*1
                    numCases[a][b][c][d][4] += numCases[a][b][c + 1][d - 1][4]*(c + 1)*1

Prob = [Decimal(0) for _ in range(53)]
descFact = [1]
for i in range(52, 0, -1):
    descFact += [descFact[-1]*i]

for a in range(14):
    for b in range(14 - a):
        for c in range(14 - a - b):
            for d in range(14 - a - b - c):
                if d == 13:
                    continue
                n = a + 2*b + 3*c + 4*d + 1
                if n < 1:
                    continue
                for L in range(1, 4):
                    if n < 6 and numCases[a][b][c][d][L] > 0:
                        print(n, a, b, c, d, L, Decimal(numCases[a][b][c][d][L]*(4 - L))/Decimal(descFact[n]))
                    if n < 52:
                        Prob[n] += Decimal(numCases[a][b][c][d][L]*(4 - L))/Decimal(descFact[n])
                    if n == 52:
                        Prob[n] += Decimal(numCases[a][b][c][d][L]*1)/Decimal(descFact[n])

print(Prob[52])
ans = sum([index*prob for index, prob in enumerate(Prob)])
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")