

#For any four internal angles that are integer, creates the fifth and checks if it is integer.
#If so, adds the angles of the quadrilateral, in cyclical order of the vertices, 
# choosing the isometry that minimizes lexicographically this cyclical list
#do not forget ot convert from degrees to radians, as well as the precision


import time
start = time.time()
from math import sin, cos, atan, floor
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
    return sin(DegToRad(alpha))


def c(alpha):
    return cos(DegToRad(alpha))


def Sigma(alpha, beta, gamma, tau):
    a = I80 - alpha - beta
    b = I80 - alpha
    d = alpha - gamma
    e = I80 - b - tau
    tansigma = s(alpha)*s(e)*s(a)*s(gamma)/(s(d)*s(beta)*s(tau) + s(e)*s(a)*s(gamma)*c(alpha))
    return RadToDeg(atan(tansigma))


def rnd(x):
    return floor(x+Decimal(0.5))


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
        #print(quad)
        l = len(ans)
        nans = ans[:]
        for q in ans:
            nans.append(Rotation(q))
            nans.append(Reflection(q))
        ans = DeleteCopies(nans)
    #print("ans = ", ans)
    return ans

squares = {}



for a in range(1, 91):
    end = time.time()
    print(" a = ", a,  "|Time elapsed ", end - start, " seconds")
    alpha = Decimal(a)
    for b in range(1, 180-a):
        end = time.time()
        #print(" a = ", a," b = ", b,  "|Time elapsed ", end - start, " seconds")
        beta = Decimal(b)
        for g in range(1, a):
            end = time.time()
            #print(" a = ", a," b = ", b," c = ", g,  "|Time elapsed ", end - start, " seconds")
            gamma = Decimal(g)
            for t in range(b+1, 180-g):
                tau = Decimal(t)
                sg = Sigma(a, b, g, t)
                if isInteger(sg):
                    quad = Quadrilateral(a, b, g, t, rnd(sg))
                    #print(GenerateIsoQuads(quad))
                    for q in GenerateIsoQuads(quad):
                        squares[q] = True


def TestSquare(q):
    if not sum(q) == 360:
        return False
    if q[0] + q[1] >= 180:
        return False
    if q[2] + q[3] >= 180:
        return False
    if q[4] + q[5] >= 180:
        return False
    if q[6] + q[7] >= 180:
        return False
    if q[2] + q[1] >= 180:
        return False
    if q[4] + q[3] >= 180:
        return False
    if q[6] + q[5] >= 180:
        return False
    if q[0] + q[7] >= 180:
        return False
    if not q[1]+q[2]+q[3]+q[4] == 180:
        return False
    if not q[3]+q[4]+q[5]+q[6] == 180:
        return False
    if not q[5]+q[6]+q[7]+q[0] == 180:
        return False
    if not q[7]+q[0]+q[1]+q[2] == 180:
        return False
    if not q[1]+q[2] == q[5] + q[6]:
        return False
    return True

def IsKite(q):
    return q[1]+q[2] == 90


def IsCyclic(q):
    return q[0] + q[1] + q[4] + q[5] == 180

end = time.time()
print("Time elapsed ", end - start, " seconds")
tot = 0
num = 0
cksquares = 0
for q in squares:
    num += 1
    if not TestSquare(q):
        print(q,  " does not conform with the required shape")
    if squares[q]:
        tot += 1
        if IsKite(q) and IsCyclic(q):
            cksquares += 1
            print(q)
        for p in GenerateIsoQuads(q):
            squares[p] = False

print("Answer up to symetry = ", tot, " not up to symetry = ", num, " cyclic kites = ", cksquares)
end = time.time()
print("Time elapsed ", end - start, " seconds")



"""
def G1(b, c, d, e):
    return math.atan((math.sin(b+e)*math.sin(e)*math.sin(b+e-c)*math.sin(b))/( (math.sin(d)*math.sin(b+d+e)*math.sin(c)) - (math.sin(b+e-c)*math.sin(b)*math.sin(e)*math.cos(b+e)) ))


def RemoveCopies(l):
    if l == []:
        return []
    s = sorted(l)
    ans = [s[0]]
    for i in range(1, len(s)):
        if not(s[i] == s[i-1]):
            ans += [s[i-1]]
    return ans


def SortedQuad(l, m, n):
    o = 360 - l - m - n
    allIso = [(l, m, n, o), (o, l, m, n), (n, o, l, m), (m, n, o, l), (o, n, m, l), (n, m, l, o), (m, l, o, n), (l, o, n, m)]
    allIso.sort()
    return allIso[0]


for b in range(1, 46):
    c = 45
    d = 45
    e = 90 - b
    print("b = ", b, " and gamma = ", RadToDeg(G1(DegToRad(180-e-d), DegToRad(b), DegToRad(c), DegToRad(d))))


a = 60
b = 60
c = 30
d = 60
gamma = 60
l1 = 1
l2 = math.sqrt(3)
l3 = math.sqrt(3)
l4 = 1

print(math.sin(DegToRad(c))/l4, math.sin(DegToRad(a+b+c))/l1)
print(math.sin(DegToRad(b))/l2, math.sin(DegToRad(b+c+d))/l1)
print(math.sin(DegToRad(a))/l3, math.sin(DegToRad(b+c-gamma))/l4)
print(math.sin(DegToRad(d))/l3, math.sin(DegToRad(gamma))/l2)

def Gamma(a, b, c, d):
    return RadToDeg(math.atan( (math.sin(DegToRad(b))*math.sin(DegToRad(d))*math.sin(DegToRad(a+b+c))*math.sin(DegToRad(a+b))) /
                      ((math.sin(DegToRad(c))*math.sin(DegToRad(a))*math.sin(DegToRad(b+c+d)))+
                       (math.sin(DegToRad(b))*math.sin(DegToRad(d))*math.sin(DegToRad(a+b+c))*math.cos(DegToRad(a+b))))))

def GamTop(a, b, c, d):
    return (math.sin(DegToRad(b))*math.sin(DegToRad(d))*math.sin(DegToRad(a+b+c))*math.sin(DegToRad(a+b)))


def GamBot1(a, b, c, d):
    return math.sin(DegToRad(c))*math.sin(DegToRad(a))*math.sin(DegToRad(b+c+d))


def GamBot2(a, b, c, d):
    return math.sin(DegToRad(b))*math.sin(DegToRad(d))*math.sin(DegToRad(a+b+c))*math.cos(DegToRad(a+b))

print(math.sin(DegToRad(a)))
print(math.sin(DegToRad(b)))
print(math.sin(DegToRad(c)))
print(math.sin(DegToRad(d)))
print(Gamma(a, b, c, d), GamTop(a, b, c ,d), GamBot1(a, b, c ,d), GamBot2(a, b, c ,d))

for b in range(1, 46):
    for c in range(b, 180-b):
        for d in range(b, 180-b-1):
            for e in range(b, 180-2*b-d):
                g1 = RadToDeg(G1(DegToRad(b), DegToRad(c), DegToRad(d), DegToRad(e)))
                g1INT = math.floor(g1+TOL)
                y = 180 - g1INT - e
                if( y > 0 and y < 180 and abs(g1 - g1INT) < TOL):
                    ans += [SortedQuad(b+c, 180 - b - d, y)]
"""