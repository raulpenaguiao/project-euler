#Code written on the 02/01/2024

#Runs in seconds


import time
from math import sqrt, pi
from decimal import Decimal, getcontext
getcontext().prec = 40
from ...CL.CL_Rational import Rational
from ...CL.CL_Geometry import Point, TriangleArea, AnglePoints, VectorTwoPoints
start = time.time()
ans = 0
verbose = True

def Proba(k):
    Ok = Point(Rational(-1, k).toDecimal(), Rational(-1, k).toDecimal())
    rs = Rational(1)-Rational(1, 2*k)
    rS = Rational(1)+Rational(1, 2*k)
    l = ((rs-Rational(1, k))*(rs+Rational(1, k)))
    if l < Rational(0):
        s = 0
    else:
        s = Rational(-1, k).toDecimal() + Decimal(sqrt(l.toDecimal()))
    S = Rational(-1, k).toDecimal() + Decimal(sqrt(((rS-Rational(1, k))*(rS+Rational(1, k))).toDecimal()))
    A = Point(s, 0)
    B = Point(S, 0)
    C = Point(0, s)
    D = Point(0, S)
    AreaBigSection = (rS.toDecimal())*Decimal(AnglePoints(D, Ok, B))
    AreaSmallSection = (rs.toDecimal())*Decimal(AnglePoints(C, Ok, A))
    AreaTriangle = Decimal((S - s)/(2*k))


    vecA = VectorTwoPoints(Ok, A)
    vecB = VectorTwoPoints(Ok, B)
    if abs(Decimal(vecA.norm())-rs.toDecimal())> 10**-4 and not(A.x == 0 and A.y == 0):
        print("----------------  k -> ", k)
        print("########## small Point in wrong place")
        print(A, vecA)
    if abs(Decimal(vecB.norm())-rS.toDecimal())> 10**-4:
        print("----------------  k -> ", k)
        print("########## big Point in wrong place")
    if abs(abs(float(TriangleArea(Ok, C, D))) - float((S - s)/(2*k))) > 10**-4:
        print(abs(float(TriangleArea(Ok, C, D))))
        print(Decimal((S - s)/(2*k)))
        print("########## Triangle area approx does not work")
    if abs(abs(float(TriangleArea(Ok, A, B))) - float((S - s)/(2*k))) > 10**-4:
        print(abs(float(TriangleArea(Ok, A, B))))
        print(Decimal((S - s)/(2*k)))
        print("########## Triangle area approx does not work")
    
    
    if verbose:
        print("----------------  k -> ", k)
        print("Big radius = ", rS.toDecimal())
        print("Small radius = ", rs.toDecimal())
        print("O = ", Ok)
        print("A = ", A)
        print("B = ", B)
        print("Big angle degrees = ", AnglePoints(D, Ok, B)*180/pi)
        print("Big circle section = ", (rS.toDecimal())*Decimal(AnglePoints(D, Ok, B)))
        print("Small angle degrees = ", AnglePoints(C, Ok, A)*180/pi)
        print("Small circle section = ", (rs.toDecimal())*Decimal(AnglePoints(C, Ok, A)))
        print("Upper triangle = ", abs(TriangleArea(Ok, A, B)), " or ", Decimal((S - s)/(2*k)))
        print("Area = ",  (rS.toDecimal())*Decimal(AnglePoints(D, Ok, B)) - (rs.toDecimal())*Decimal(AnglePoints(C, Ok, A)) - abs(TriangleArea(Ok, A, B)) - abs(TriangleArea(Ok, C, D)) )
    
    
    
    
    return AreaBigSection - AreaSmallSection - AreaTriangle*2



LIM = 10
for k in range(1, LIM+1):
    l = Proba(k)*k
    print(l)
    ans += l

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")