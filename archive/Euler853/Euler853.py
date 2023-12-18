#Code written on 2023/11/27
#Computes pi(p) for every prime below 10**9, for those that divide 120 includes the respective powers
#Use the fact that pi(mn) = lcm(pi(m), pi(n)) if m, n are coprime
#Runs in 26 seconds

from ...CL.CL_Arithmetics import lcm
import time
import math
start = time.time()
ans = 0

N = 10**9
NsqrtLIM = math.floor(math.sqrt(N)) + 10
primes = [2]
sieve = [True for _ in range(NsqrtLIM+1)]
for i in range(4, NsqrtLIM+1, 2):
    sieve[i] = False
for i in range(3, NsqrtLIM+1, 2):
    if sieve[i]:
        primes.append(i)
        for j in range(i*i, NsqrtLIM+1, i):
            sieve[j] = False

print(len(primes))

def PrimeQ(i):
    for p in primes:
        if i%p == 0:
            return i == p
    return True

def AddToList(p, base, lim):
    ans = [1]
    while(base <= lim):
        ans += [base]
        base *= p
    return [p, ans]

targ = 120
prods = []
if targ >= 3:
    prods.append(AddToList(2, 3, targ))
if targ >= 20:
    prods.append(AddToList(5, 20, targ))

fibbs = [0, 1]
for i in range(2, targ + 2):
    fibbs.append(fibbs[-1]+fibbs[-2])

divs = []
for i in range(1, targ+1):
    if targ%i == 0:
        divs += [[i, fibbs[i], fibbs[i+1]]]


print(divs)

for i in range(1, N+1, 10):
    #First see if pi(j) divides targ
    if fibbs[targ]%i == 0 and fibbs[targ+1]%i == 1:
        #See if this is a prime number
        if PrimeQ(i):
            #Compute pi(j) explicitly
            j = 0
            flag = True
            while(flag and j < len(divs)):
                if fibbs[divs[j][0]]%i == 0 and fibbs[divs[j][0]+1]%i == 1:
                    flag = False
                else:
                    j+= 1
            if not flag:
                pi = divs[j][0]
                #Should be a divisor of i-1
                prods.append(AddToList(i, pi, targ))

for i in range(9, N+1, 10):
    #First see if pi(j) divides targ
    if fibbs[targ]%i == 0 and fibbs[targ+1]%i == 1:
        #See if this is a prime number
        if PrimeQ(i):
            #Compute pi(j) explicitly
            j = 0
            flag = True
            while(flag and j < len(divs)):
                if fibbs[divs[j][0]]%i == 0 and fibbs[divs[j][0]+1]%i == 1:
                    flag = False
                else:
                    j+= 1
            if not flag:
                pi = divs[j][0]
                #Should be a divisor of i-1
                prods.append(AddToList(i, pi, targ))


for i in range(3, N+1, 10):
    #First see if pi(j) divides targ
    if fibbs[targ]%i == 0 and fibbs[targ+1]%i == 1:
        #See if this is a prime number
        if PrimeQ(i):
            #Compute pi(j) explicitly
            j = 0
            flag = True
            while(flag and j < len(divs)):
                if fibbs[divs[j][0]]%i == 0 and fibbs[divs[j][0]+1]%i == 1:
                    flag = False
                else:
                    j+= 1
            if not flag:
                pi = divs[j][0]
                #Should be a divisor of i-1
                prods.append(AddToList(i, pi, targ))

for i in range(7, N+1, 10):
    #First see if pi(j) divides targ
    if fibbs[targ]%i == 0 and fibbs[targ+1]%i == 1:
        #See if this is a prime number
        if PrimeQ(i):
            #Compute pi(j) explicitly
            j = 0
            flag = True
            while(flag and j < len(divs)):
                if fibbs[divs[j][0]]%i == 0 and fibbs[divs[j][0]+1]%i == 1:
                    flag = False
                else:
                    j+= 1
            if not flag:
                pi = divs[j][0]
                #Should be a divisor of i-1
                prods.append(AddToList(i, pi, targ))


def AddOne(it, lims):
    for i in range(len(lims)-1, -1, -1):
        if it[i] < lims[i] - 1:
            it[i] += 1
            return True
        else:
            it[i] = 0
    return False


def ProdPos(it, d):
    ans = 1
    for i in range(len(it)):
        ans = lcm(ans, d[i][1][it[i]])
    return ans



def ProdNum(it, d):
    ans = 1
    for i in range(len(it)):
        ans *= d[i][0]**it[i]
    return ans

l = len(prods)
it = [0 for _ in range(l)]
flag = True
lms = [len(d[1]) for d in prods]
print(prods)
while(flag):
    if ProdPos(it, prods) == 120 and ProdNum(it, prods) < N:
        ans += ProdNum(it, prods)
    flag = AddOne(it, lms)


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")