import time
start = time.time()
from ...CL.CL_Primes import EulerPhi, Divisors, Primes

ans = 0
primes = Primes(1000)

LIM = 10**15
lim = 10
fact = [1]
for i in range(1, 1+lim*lim):
    fact.append(i*fact[-1])
#Find smallest index such that fact[i] > LIM
IND = 1
while(fact[IND] <= LIM):
    IND += 1
for i in range(1+lim*lim, 1+IND*IND):
    fact.append(i*fact[-1])
lim = IND



def F(m, n):
    tot = 0
    #print("==== computing ", m, n, " =====")
    phi = EulerPhi(n)
    for t in Divisors(n, primes):
        s = phi[t]*fact[m*n//t]//(fact[n//t]**m)
        tot += s
        #print(t, s, phi[t], m*n//t, fact[n]**m)
    return tot//(m*n)



for m in range(2, lim+1):
    f = F(m, 1)
    for n in range(1, lim+1):
        f = F(m, n)
        #print(m, n, f)
        if f <= LIM:
            ans += f
        else:
            break



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")