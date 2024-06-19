

#For any four internal angles that are integer, creates the fifth and checks if it is integer.
#If so, adds the angles of the quadrilateral, in cyclical order of the vertices, 
# choosing the isometry that minimizes lexicographically this cyclical list
#do not forget ot convert from degrees to radians, as well as the precision


import time
start = time.time()
ans = 0
from math import sin, cos, atan, floor, tan
from decimal import *
import random
from ....CL.CL_Geometry import Point, AnglePoints
getcontext().prec = 46

PI = Decimal(3.1415926535897932384)
PREC = Decimal(10**(-7))
I80 = Decimal(180)

def DegToRad(alph):
    return Decimal(alph)*PI/I80


def RadToDeg(alph):
    return Decimal(alph)*I80/PI


def s(alpha):
    return sin(DegToRad(alpha))


def c(alpha):
    return cos(DegToRad(alpha))


def ct(alpha):
    t = tan(DegToRad(alpha))
    if abs(t) < PREC:
        return 10**89
    return Decimal(1)/Decimal(t)


def A1(DEGgamma1, DEGtau2, DEGtau1, DEGbeta2, DEGbeta1, DEGalpha2):
    a = s(DEGtau1)*s(DEGgamma1)*s(DEGbeta1)
    b = s(DEGtau2)*s(DEGbeta2)*s(DEGalpha2)
    den = a+b*c(DEGtau1+DEGbeta2)
    if abs(den) < PREC:
        DEGa1 = Decimal(90)
    else:
        tanSigma = s(DEGtau1+DEGbeta2)*b/den
        DEGa1 = RadToDeg(atan(tanSigma))
    return DEGa1


def rnd(x):
    return floor(x+Decimal(0.5))

def isInteger(x):
    return abs(rnd(x)-x) < PREC

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



def isKite(quad):
    return quad[0] + quad[1] == 90


def isCyclic(quad):
    return quad[0] == quad[5]

def IsValid(g1, t2, t1, b2, b1, a2, a1, g2):
    if not rnd(g1+t2+t1+b2) == 180:
        return "Triangle 1 not right"
    if not rnd(t1+b2+b1+a2) == 180:
        return "Triangle 2 not right"
    if not rnd(b1+a2+a1+g2) == 180:
        return "Triangle 3 not right"
    if not rnd(a1+g2+g1+t2) == 180:
        return "Triangle 4 not right"
    if g1 <= 0 or t2 <= 0 or t1 <= 0 or b2 <= 0 or b1 <= 0 or a2 <= 0 or a1 <= 0 or g2 <= 0:
        return "Non positive angles"
    if abs(s(a1)*s(b1)*s(g1)*s(t1) - s(a2)*s(b2)*s(g2)*s(t2)) > PREC:
        return "No sine relation"
    return ""

def InnerAnglesFromPoints(A, B, C, D):
    RADgamma1 = Decimal(AnglePoints(D, A, C))
    RADtau2 = Decimal(AnglePoints(B, D, A))
    RADtau1 = Decimal(AnglePoints(C, D, B))
    RADbeta2 = Decimal(AnglePoints(A, C, D))
    RADbeta1 = Decimal(AnglePoints(B, C, A))
    RADalpha2 = Decimal(AnglePoints(D, B, C))
    RADalpha1 = Decimal(AnglePoints(A, B, D))
    RADgamma2 = Decimal(AnglePoints(B, A, C))
    return RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2


#Create 100 random convex squares to test our functions
lst = []
for i in range(10):
    A = Point(Decimal(random.random()) - Decimal(1.5), Decimal(random.random()) + Decimal(0.5))
    B = Point(Decimal(random.random()) + Decimal(0.5), Decimal(random.random()) + Decimal(0.5))
    C = Point(Decimal(random.random()) + Decimal(0.5), Decimal(random.random()) - Decimal(1.5))
    D = Point(Decimal(random.random()) - Decimal(1.5), Decimal(random.random()) - Decimal(1.5))
    RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2 = InnerAnglesFromPoints(A, B, C, D)
    if abs(RADtau1 + RADbeta2 - RADgamma2 - RADalpha1) > PREC:
        print([RadToDeg(RADgamma1), RadToDeg(RADtau2), RadToDeg(RADtau1), RadToDeg(RADbeta2), RadToDeg(RADbeta1), RadToDeg(RADalpha2), RadToDeg(RADalpha1), RadToDeg(RADgamma2)])
    lst += [[RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2]]


#For each test square, see if the angles formed are indeed valid or not
#If not, then this will print a message
for RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2 in lst:
    isv = IsValid(RadToDeg(RADgamma1), RadToDeg(RADtau2), RadToDeg(RADtau1), RadToDeg(RADbeta2), RadToDeg(RADbeta1), RadToDeg(RADalpha2), RadToDeg(RADalpha1), RadToDeg(RADgamma2))
    if not isv == "":
        print(isv, RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2)
    if abs(RADtau1 + RADbeta2 - RADgamma2 - RADalpha1) > PREC:
        print("Angle sum criteria", RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2 )
    if abs( s(RadToDeg(RADgamma2))  - (s(RadToDeg(RADtau1+RADbeta2))*c(RadToDeg(RADalpha1)) - c(RadToDeg(RADtau1+RADbeta2))*s(RadToDeg(RADalpha1)))) > PREC:
        print("Sine sum criteria", RADgamma1, RADtau2, RADtau1, RADbeta2, RADbeta1, RADalpha2, RADalpha1, RADgamma2 )
    diff = abs(A1(RadToDeg(RADgamma1), RadToDeg(RADtau2), RadToDeg(RADtau1), RadToDeg(RADbeta2), RadToDeg(RADbeta1), RadToDeg(RADalpha2)) - RadToDeg(RADalpha1))
    if diff > PREC:
        print("Diff crit ",diff, RADalpha1)



#Our square of interest has vertices ABCD (think A top right, B top left, C bottom right, D bottom left)
#The angles are 
# gamma1 = angle(DAC)
# tau2 = angle(BDA)
# tau1 = angle(CDB)
# beta2 = angle(ACD)
# beta1 = angle(BCA)
# alpha2 = angle(DBC)
# alpha1 = angle(ABC)
# gamma2 = angle(CAB)
#We are finding all quadrilaterals whose beta1, beta2, tau1, tau2 are integer angles s.t. beta2 is one of the smallest angles of these four

squares = {}
for b2 in range(1, 46):
    #end = time.time()
    #print("b2 = " ,  b2, " Time elapsed ", end - start, " seconds")
    beta2 = Decimal(b2)
    for b1 in range(b2, 180 - b2):#We can assume that b1 >= b2 to break the symmetry
        beta1 = Decimal(b1)
        for t1 in range(b1, 180 - b1 - b2):#We can assume that t1 >= b2 to break the symmetry
            tau1 = Decimal(t1)
            a2 = 180 - t1 - b1 - b2
            if a2 < b2:#We can assume that a2 >= b2 to break the symmetry
                continue
            alpha2 = Decimal(a2)
            for t2 in range(b1, 180 - t1 - b2):#We can assume that t2 >= b2 to break the symmetry
                g1 = 180 - t1 - t2 - b2
                if g1 < b2:#We can assume that g1 >= b2 to break the symmetry
                    continue
                tau2 = Decimal(t2)
                gamma1 = Decimal(g1)
                alpha1 = A1(gamma1, tau2, tau1, beta2, beta1, alpha2)
                if not isInteger(alpha1):
                    continue
                a1 = rnd(alpha1)
                g2 = t1 + b2 - a1
                if  a1 < b2 or g2 < b2:#We can assume that a1 >= b2 and g2 >= b2 to break the symmetry
                    continue
                isvalid = IsValid(g1, t2, t1, b2, b1, a2, a1, g2)
                if isvalid == "":
                    squares[(g1, t2, t1, b2, b1, a2, a1, g2)] = True


def PointFromAngles(DEGbeta, DEGalpha):
    if abs(DEGbeta + DEGalpha - 180) < PREC:
        return Point(10**86, ct(DEGalpha)*10**86)
    x = Decimal(1)/(ct(DEGbeta) + ct(DEGalpha))
    return Point(x, ct(DEGalpha)*x)


def FindPoints(quad):
    A = Point(0, 0)
    B = PointFromAngles(quad[0] + quad[7], quad[2])
    C = PointFromAngles(quad[0], quad[1] + quad[2])
    D = Point(0, 1)
    return [A, B, C, D]

#Let's write each quadrilateral found in a file, along with a possible representation (i.e. four points)
open("quads_list.txt", "w").close()
f = open("quads_list.txt", "w")

ansKite = 0
ansCyclic = 0
lst = []
for quad in squares:
    if squares[quad]:
        f.write(str(quad))
        f.write(" _ ")
        A, B, C, D = FindPoints(quad)
        f.write(str([rnd(RadToDeg(a)) for a in InnerAnglesFromPoints(A, B, C, D)]))
        #Instead of writing representation we write the angles and compare
        #This is to test if the function is working. IT IS NOT WORKING
        ans += 1
        geniso = GenerateIsoQuads(quad)
        if isKite(quad):
            ansKite += 1
        if isCyclic(quad):
            ansCyclic += 1
        for q in geniso:
            if q in squares:
                squares[q] = False
        f.write("\n")

f.close()
print("Kites = ", ansKite)
print("Cyclic = ", ansCyclic)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")
