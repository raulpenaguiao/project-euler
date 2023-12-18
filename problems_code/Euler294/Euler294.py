import time
start = time.time()
ans = [1, 10]

while( ans[-1] > 1):
    ans.append((ans[-1]*10) % 23)


binom = [[0 for _ in range(100)] for _ in range(100)]
for i in range(100):
    binom[i][i] = 1
    binom[i][0] = 1
for n in range(1, 100):
    for i in range(1, i):
        binom[n][i] = binom[n-1][i] + binom[n-1][i-1]


lim = 23

f = [[[0 for _ in range(lim*lim+1)] for _ in range(lim+1)] for _ in range(lim+1)]
f[0][0][0] = 1
for a in range(1, lim):
    for b in range(lim+1):
        for c in range(lim*lim+1):
            for d in range(b+1):
                #Add the digit d at the end
                if c < d*a:
                    continue
                f[a][b][c] +=  f[a-1][b-d][c-d*a]
r = [f[lim-1][lim][lim*c] for c in range(1, lim)]
print(r)
print(sum(r))


"""
f = [[[[] for _ in range(lim*lim+1)] for _ in range(lim+1)] for _ in range(lim+1)]
f[0][0][0] = [[]]
for a in range(1, lim):
    for b in range(lim+1):
        for c in range(lim*lim+1):
            for d in range(b+1):
                #Add the digit d at the end
                if c < d*a:
                    continue
                for lst in f[a-1][b-d][c-d*a]:
                    f[a][b][c].append(lst+[d])

print([len(f[lim-1][lim][lim*c]) for c in range(1, lim)])
"""
print("Answer = ", len(ans))
end = time.time()
print("Time elapsed ", end - start, " seconds")