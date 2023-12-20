import time
start = time.time()
from ...CL.CL_SetPartitions import GenerateSetPartitions
from ...CL.CL_Sets import Set

gs = GenerateSetPartitions(Set(elements = [0, 1, 2, 3, 4, 5]))
strT = {s:s.ToString() for s in gs}
print(len(gs))

#gs = GenerateStrings("project", 3)
print("The matrices have size = " , len(gs))
def Id():
    ans = {s:{t:0 for t in gs} for s in gs}
    for s in gs:
        ans[strT[s]][strT[s]] = 1
    return ans

def MatProd(A, B):
    ans = {strT[s]:{strT[t]:0 for t in gs} for s in gs}
    for a in gs:
        for b in gs:
            for c in gs:
                ans[strT[a]][strT[c]] += A[strT[a]][strT[b]]*B[strT[b]][strT[c]]
                ans[strT[a]][strT[c]] %= 1_000_000_000
    return ans

def PowerMat(M, p):
    print(p)
    if p == 0:
        return Id()
    Msq = MatProd(M, M)
    if p%2 == 1:
        return MatProd(M, PowerMat(Msq, p//2))
    return PowerMat(Msq, p//2)



A = {strT[s]:{strT[t]:0 for t in gs} for s in gs}
for part in gs:
    #Generate >pi


    #Generate special pi

print("Matrix A generated")
tMatr = PowerMat(A, 10**12-6)
print("Power matrix computed")

ans = 0
for s in gs:
    for t in gs:
        ans += tMatr[strT[s]][strT[t]]
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")