#Prints all the groups of squares that have the same set of angles together
#Runs in 5 secs


import time
start = time.time()
import math
from decimal import *
getcontext().prec = 16
PI = Decimal(3.1415926535897932384)
PREC = Decimal(10**-9)
I80 = Decimal(180)

def DegToRad(alph):
    return Decimal(alph)*PI/I80


def s(alpha):
    return math.sin(DegToRad(alpha))


def c(alpha):
    return math.cos(DegToRad(alpha))


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
f = open("Euler177_squares_list.txt", "r")
for st in f.read().split("\n"):
    if st == "":
        continue
    quad = tuple([int(v) for v in st.split(" ")])
    for p in GenerateIsoQuads(quad):
        if p in squares:
            print(quad, " - ", p)
    squares[quad] = True


def TestSquare(q):
    if not sum(q) == 360:
        return "sum relation"
    for v in q:
        if v <= 0:
            return "not positive"
    if not q[1]+q[2]+q[3]+q[4] == 180:
        return "side triangle relation"
    if not q[3]+q[4]+q[5]+q[6] == 180:
        return "side triangle relation"
    if not q[5]+q[6]+q[7]+q[0] == 180:
        return "side triangle relation"
    if not q[7]+q[0]+q[1]+q[2] == 180:
        return "side triangle relation"
    if not q[1]+q[2] == q[5] + q[6]:
        return "middle line relation"
    df1 = s(q[0])*s(q[2])*s(q[4])*s(q[6])
    df2 = s(q[1])*s(q[3])*s(q[5])*s(q[7])
    if abs(df1 - df2) > PREC:
        return "sine relation"
    return ""

def IsKite(q):
    return q[1]+q[2] == 90


def IsCyclic(q):
    return q[0] + q[1] + q[4] + q[5] == 180

end = time.time()
print("Time elapsed ", end - start, " seconds")
tot = 0
num = 0
error = 0
cksquares = 0
for q in squares:
    num += 1
    test = TestSquare(q)
    if not test == "":
        error += 1
        print(q,  " does not conform with the required shape because " + test)
    if squares[q]:
        tot += 1
        if IsKite(q) and IsCyclic(q):
            cksquares += 1


sameSet = {}
for q in squares:
    stuple = tuple(sorted(list(q)))
    if stuple in sameSet:
        sameSet[stuple] += [q]
        print(sameSet[stuple])
    else:
        sameSet[stuple] = [q]

print("Answer up to symetry = ", tot, " cyclic kites = ", cksquares, " without errors ", tot - error)
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