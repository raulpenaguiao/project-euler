import time
import math

start_time = time.time()
verbose = False

def abv(a):
    return max(a, -a)

if verbose:
    print("Abs ( 8 ) = ", abv(8))
    print("Abs ( -8 ) = ", abv(-8))


def gcd(a, b):
    #print(" a = ", a, " and b = ", b)
    if a < 0 or b < 0:
        return gcd(abv(a), abv(b))
    if b == 0:
        return a
    return gcd(b, a%b)


one = [1, 1]
half =[1, 2]
pi  = [22, 7]

def rRed(r):
    d = gcd(r[0], r[1])
    if d == 0:
        return r
    return [r[0]//d, r[1]//d]

if verbose:
    print("Half fraction reduced is", rRed([3, 6]))

def rAdd(r1, r2):
    return rRed([r1[0]*r2[1]+r2[0]*r1[1], r1[1]*r2[1]])

if verbose:
    print(" 1 + pi = ", rAdd(one, pi))  
    print("1/2+pi = ", rAdd(half, pi))


def rScal(s, r):
    return rRed([s*r[0], r[1]])

def rSub(r1, r2):
    return rAdd(r1, rScal(-1, r2))

def rMult(r1, r2):
    #print("r1 = ", r1, " and r2 = ", r2)
    return rRed([r1[0]*r2[0], r1[1]*r2[1]])

def rInv(r):
    return [r[1], r[0]]

def rDiv(r1, r2):
    return rRed([r1[0]*r2[1], r1[1]*r2[0]])

def rMod(r, m):
    return [r[0]%m, r[1]%m]


## f = [r1, r2] represents r1 sqrt(5) + r2
def fAdd(f1, f2):
    return [rAdd(f1[0], f2[0]), rAdd(f1[1], f2[1])]

def fScal(r, f):
    return [rMult(r, f[0]), rMult(r, f[1])]

def fSub(f1, f2): #f1 - f2
    return [rSub(f1[0], f2[0]), rSub(f1[1], f2[1])]

def fMult(f1, f2):
    return [rAdd(rMult(f1[0], f2[1]), rMult(f1[1], f2[0])), rAdd(rMult(f2[1], f1[1] ), rMult(rMult(f1[0], f2[0]), [5, 1] ))] 

def fDet(f):
    return rSub(rMult(rMult([5, 1], f[0]), f[0]), rMult(f[1], f[1]))

def fInv(f):
    #print("scalar = ", rInv(fDet(f)))
    #print("irrational part = ", f[0])
    #print("rational part = ", f[1])
    return fScal(rInv(fDet(f)), [f[0], rScal(-1, f[1])])

def fDiv(f1, f2):
    return fMult(f1, fInv(f2))

if verbose:
    a = [[2, 3], [1, 9]]
    b = [[2, 1], [3, 2]]
    print("Compare ", a, " and ", fMult(fDiv(a, b), b))


def fMod(f, m):
    return [rMod(f[0], m), rMod(f[1], m)]


def power_mod(a, p, m):
    if p == 1:
        return fMod(a, m)
    if p%2 == 1:
        return fMod(fMult(a, power_mod(fMod(fMult(a, a), m), p//2, m)), m)
    return fMod(power_mod(fMod(fMult(a, a), m), p//2, m), m)

if verbose:
    print("assert if [[1, 8], [1, 4]] = ", power_mod([[1, 4], [1, 4]], 3, 100))

def p_mod(a, p, m):
    if p == 1:
        return a
    if p%2 == 1:
        return (a*p_mod((a*a)%m, p//2, m))%m
    return p_mod((a*a)%m, p//2, m)%m


if verbose:
    print(fMult(phip, phip))
    print(power_mod(phip, 100, MOD))
    print(fMult([[1, 1], [0, 1]], [[1, 1], [0, 1]]))


MOD = 1000000009
MODPHI = 1000000008
p = 10**18

#MOD = 109
#MODPHI = 108
#p = 3

phip = [[1, 2], [1, 2]]
phim = [[-1, 2], [1, 2]]

## Starting to compute the formula
## 
## 
a = fScal([1, 2], phip)
b = power_mod(a, p, MOD)
c = fSub([[0, 1], [1, 1]], b)
d = fMult(phip, [[1, 1], [0, 1]])
e = fMult(c, d)
f = fInv(e)
#print("e = ", e)
#print("f = ", f)
u = fScal([1, 2], phim)
v = power_mod(u, p, MOD)
w = fSub([[0, 1], [1, 1]], v)
x = fMult(phim, [[1, 1], [0, 1]])
y = fMult(w, x)
z = fInv(y)
#print("v = ", v)
#print("z = ", z)
ans = fMod(fSub(f, z), MOD)
ans1 = ans[1]
ans = ans[0]
#print("irrational part  = ", rRed(ans))
#print("rational part = ", rRed(ans1))
print((ans1[0] * p_mod(ans1[1], MODPHI-1, MOD)+ MOD - 1)%MOD)


print(" --- %s seconds --- "%(time.time() - start_time))
