import time
start = time.time()
ans = 0
MOD = 83456729

from queue import Queue
from ...CL.CL_Arithmetics import gcd

def Generate_Permutations(lst):
    if len(lst) == 0:
        return [[]]
    ans = []
    for p in Generate_Permutations(lst[1:]):
        for i in range(len(lst)):
            ans.append(p[:i] + [lst[0]] + p[i:])
    return ans

def f(n):
    ans = 0
    for per in Generate_Permutations([i for i in range(2, n+1)]):
        flag = True
        for i in range(1, len(per)):
            if gcd(per[i], per[i-1]) > 1:
                flag = False
                break
        if flag:
            ans += 1
    return ans

fact = [1 for _ in range(100)]
for i in range(1, 50):
    fact[i] = fact[i-1]*i


print(sum([fact[17]*fact[16]//(fact[k]*fact[17-k]*fact[16-k]) for k in range(1, 11)]))


def f_eff(n):
    edges = []
    for i in range(3, n+1):
        for j in range(i+1, n+1, 2):
            if gcd(i, j) > 1:
                edges.append([i, j])
    #set of all the graphs
    CAP = Queue() 
    CAP.put([[0 for _ in range(n+1)], 0])


    if n%2 == 0:
        ans = fact[n//2]*fact[n//2]
    else:
        ans = fact[n//2]*fact[n//2+1]
    counter = 0

    while(not CAP.empty()):
        grph = CAP.get()
        #print("Analysing ", grph)
        #Contribution to answer
        counter += 1
        #Add descendants
        for e1, e2 in edges:
            if grph[0][e1] == 1 or grph[0][e2] == 1:
                continue
            if grph[0][e1] == e2:
                continue
            newgrphedges = grph[0][:]
            ngnumber = grph[1]
            ngnumber += 1
            if grph[0][e1] == 0:
                if grph[0][e2] == 0:
                    newgrphedges[e1] = e2
                    newgrphedges[e2] = e1
                else:
                    newgrphedges[e1] = newgrphedges[e2]
                    newgrphedges[e2] = 1
            else:
                if grph[0][e2] == 0:
                    newgrphedges[e2] = newgrphedges[e1]
                    newgrphedges[e1] = 1
                else:
                    continue
            #print("Adding ", [newgrphedges, ngnumber])
            CAP.put([newgrphedges, ngnumber])

    print("We analysed ", counter, " many graphs")
    return ans
    






print("Answer = ", f_eff(18))
end = time.time()
print("Time elapsed ", end - start, " seconds")