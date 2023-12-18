import time
start = time.time()
import math
from decimal import *
getcontext().prec = 16

PI = Decimal(3.1415926535897932384)
PREC = Decimal(10**-14)
I80 = Decimal(180)

def DegToRad(alph):
    return Decimal(alph)*PI/I80


def RadToDeg(alph):
    return Decimal(alph)*I80/PI


def s(alpha):
    return math.sin(DegToRad(alpha))


def c(alpha):
    return math.cos(DegToRad(alpha))


def Sigma(alpha, beta, gamma, tau):
    a = I80 - alpha - beta
    b = I80 - alpha
    d = alpha - gamma
    e = alpha - tau
    tansigma = 0
    if abs(s(d)*s(beta)*s(tau) + s(e)*s(a)*s(gamma)*c(b)) < PREC:
        return 90
    tansigma = s(b)*s(e)*s(a)*s(gamma)/(s(d)*s(beta)*s(tau) + s(e)*s(a)*s(gamma)*c(b))
    ans = RadToDeg(math.atan(tansigma))
    if ans < 0:
        ans += 180
    return ans


def rnd(x):
    return math.floor(x+Decimal(0.5))


def isInteger(x):
    return abs(rnd(x)-x) < PREC


def Quadrilateral(alpha, beta, gamma, tau, sigma):
    a = 180 - alpha - beta
    b = 180 - alpha
    d = alpha - gamma
    e = 180 - tau - b
    pi = b - sigma
    return (gamma, beta, a, tau, e, sigma, pi, d)

def Rotation(quad):
    return tuple([quad[i] for i in range(2, 8)] + [quad[0], quad[1]])

def Reflection(quad):
    return tuple([quad[i] for i in range(7, -1, -1)])

def DeleteCopies(lst):
    if lst == []:
        return []
    lst.sort()
    ans = [lst[0]]
    l = len(lst)
    for i in range(1, l):
        if not ans[-1] == lst[i]:
            ans.append(lst[i])
    return ans


def GenerateIsoQuads(quad):
    l = 0
    ans = [quad]
    while(len(ans) > l):
        l = len(ans)
        nans = ans[:]
        for q in ans:
            nans.append(Rotation(q))
            nans.append(Reflection(q))
        ans = DeleteCopies(nans)
    return ans


squares = {}

for a in range(1, 91):
    end = time.time()
    print(" a = ", a,  "|Time elapsed ", end - start, " seconds")
    alpha = Decimal(a)
    for b in range(1, 180-a):
        end = time.time()
        beta = Decimal(b)
        for g in range(1, a):
            end = time.time()
            gamma = Decimal(g)
            for t in range(1, a):
                tau = Decimal(t)
                sg = Sigma(a, b, g, t)
                if isInteger(sg):
                    quad = Quadrilateral(a, b, g, t, rnd(sg))
                    for q in GenerateIsoQuads(quad):
                        squares[q] = True


end = time.time()
print("List generated. Time elapsed ", end - start, " seconds")

f = open("Euler177_squares_list.txt", "w")

for q in squares:
    if squares[q]:
        f.write(str(q[0]) + " " + str(q[1]) + " " + str(q[2]) + " " + str(q[3]) + " " + str(q[4]) + " " + str(q[5]) + " " + str(q[6]) + " " + str(q[7]) +"\n")
        for p in GenerateIsoQuads(q):
            squares[p] = False


f.close()
end = time.time()
print("Program finished. Time elapsed ", end - start, " seconds")

