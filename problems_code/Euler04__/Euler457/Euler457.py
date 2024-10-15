import time
start = time.time()
ans = 0

from ....CL.CL_Primes import Primes

#Only for p = 13 we need to find a solution in Z_(p*p)
f13 = 0
def R(p):
    for i in range(p*p):
        if (i*i-3*i-1)%p == 0:
            return i
    return 0

L = 10**3
primes = Primes(10**7)

#Everywhere else we may only find it in Z_p and that is enough
#This exists iff 13 is a square in Z_p
if L >= 2:
    ans += R(2)
    if L >= 13:
        ans += R(13)


nonRes = {2, 5, 6, 7, 8, 11}

def R_eff(p):
    if p%13 in nonRes:
        return 0
    for i in range(p):
        if (i*i-3*i-1)%p == 0:
            #not the correct return, we need to return i - ((i*i-3*i-1)%p*p ) * 2i - 3)^(-1)
            # return i

for p in primes:
    if p == 2 or p == 13:
        continue
    ans += R_eff(p)

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")