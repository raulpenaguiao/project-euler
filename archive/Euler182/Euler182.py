#Code written on 2023/11/15
#ord_a(m) is the smallest integer i such that m**i = 1 mod a
#a message is unconcealed if 
#   a = 0 mod pq, 
#   a = 0 mod p and ord_q(a)| e-1 and (q, a) = 1
#   a = 0 mod q and ord_p(a)| e-1 and (p, a) = 1
#   ord_pq(a)| e-1 and (pq, a) = 1
#Runs in 45s
import time
import math
start = time.time()




def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def Ord(i, mod):
    a = i%mod
    if a == 1:
        return 1
    count = 1
    while(a > 1):
        a *= i
        a %= mod
        count += 1
    return count


def OrdList(M, phi):
    ans = {}
    vis = {}
    
    for i in range(1, M):
        vis[i] = False
        ans[i] = phi
    ans[1] = 1
    for i in range(2, M):
        if gcd(i, M) == 1:
            if not vis[i]:
                a = i
                vis[a] = True
                ans[a] = Ord(a, M)
                count = 1
                while(a > 1):
                    a *= i
                    a %= M
                    count += 1
                    if not vis[a]:
                        vis[a] = True
                        ans[a] = ans[i]//gcd(ans[i], count)
    return ans

ans = 0
p = 1009
q = 3643
M = p*q
phi = (p-1)*(q-1)
minPowerpq = OrdList(p*q, phi)
minPowerq = OrdList(q, q-1)
minPowerp = OrdList(p, p-1)

numUCM = [1 for _ in range(phi)]
#For each e, numUCM[e] counts the number of messages that are unconcealed with exponent e
#This already counts the message m = 0
for i in range(1, q):
    #We are considering messsage m = p*i here
    for e in range(1, phi, minPowerq[(p*i)%q]):
        numUCM[e] += 1
for i in range(1, p):
    #We are considering messsage m = q*i here
    for e in range(1, phi, minPowerp[(q*i)%p]):
        numUCM[e] += 1
for m in range(1, M):
    if gcd(m, M) == 1:
        for e in range(1, phi, minPowerpq[m]):
            numUCM[e] += 1

minValue = M
for e in range(1, phi):
    if gcd(e, phi) == 1:
        if numUCM[e] < minValue:
            minValue = numUCM[e]
count = 0
ans = 0
for e in range(1, phi):
    if gcd(e, phi) == 1 and numUCM[e] == minValue:
        ans += e
        count += 1


print("Answer = ", ans, " with min value ", minValue, " and occurrences ", count)
end = time.time()
print("Time elapsed ", end - start, " seconds")

"""Naive method
def PowerMod(a, m, p):
    if m == 0:
        return 1
    ans = PowerMod((a*a)%p, m//2, p)
    if m%2 == 1:
        ans *= a
        ans %= p
    return ans

def UCM(i, M):
    ans = 0
    for a in range(M):
        if PowerMod(a, i, M) == a:
            ans += 1
    return ans
numUCM = [[UCM(i, M), i] for i in range(1, M) if gcd(i, phi) == 1]
print(numUCM)
numUCM.sort()
mn = min(numUCM)
newans = sum([k[1] for k in numUCM if k[0] == mn])"""

"""
def Exps(p, q):
    M = p*q
    phi = (p-1)*(q-1)
    exps = {}
    for e in range(1, phi):
        UCM = 0
        for m in range(M):
            if PowerMod(m, e, M) == m:
                UCM += 1
        exps[e] = UCM
    return exps


def MinExp(p, q):
    exps = Exps(p, q)
    minUCM = phi
    for e in exps:
        if exps[e] < minUCM:
            minUCM = exps[e]
    return minUCM


def SumMinExps(p, q):
    exps = Exps(p, q)
    minUCM = phi
    for e in exps:
        if exps[e] < minUCM:
            minUCM = exps[e]
    ans = 0
    for e in exps:
        if exps[e] == minUCM:
            ans += e
    return ans

print(Exps(7, 19))"""

