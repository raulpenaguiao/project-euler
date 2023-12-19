import time
start = time.time()
def GenerateStrings(st, l):
    if l == 0:
        return [""]
    ans = []
    for s in GenerateStrings(st, l-1):
        for c in st:
            ans.append(c+s)
    return ans

gs = GenerateStrings("project", 2)
print("The matrices have size = " , len(gs))
def Id():
    ans = {s:{t:0 for t in gs} for s in gs}
    for s in gs:
        ans[s][s] = 1
    return ans

def MatProd(A, B):
    ans = {s:{t:0 for t in gs} for s in gs}
    for a in gs:
        for b in gs:
            for c in gs:
                ans[a][c] += A[a][b]*B[b][c]
    return ans

def PowerMat(M, p):
    print(p)
    if p == 0:
        return Id()
    Msq = MatProd(M, M)
    if p%2 == 1:
        return MatProd(M, PowerMat(Msq, p//2))
    return PowerMat(Msq, p//2)


def AllCharsDifferent(st):
    l = len(st)
    for i in range(l):
        for j in range(i):
            if st[i] == st[j]:
                return False
    return True

A = {s:{t:0 for t in gs} for s in gs}
for s in gs:
    flag = AllCharsDifferent(s)
    for c in "project":
        if c == s[0] and flag:
            continue
        t = (s+c)[1:]
        A[s][t] = 1

print("Matrix A generated")
tMatr = PowerMat(A, 10**12-6)
print("Power matrix computed")

ans = 0
for s in gs:
    for t in gs:
        ans += tMatr[s][t]
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")