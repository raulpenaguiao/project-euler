#Code written on the 02/01/2024

#Runs in seconds


import time
from math import sqrt, pi
from ...CL.CL_Rational import Rational
from ...CL.CL_Geometry import Point, TriangleArea, AnglePoints
start = time.time()
ans = 0
verbose = True

def Proba(k):
    Ok = Point(Rational(-1, k).toFloat(), Rational(-1, k).toFloat())
    rs = Rational(1)-Rational(1, 2*k)
    rS = Rational(1)+Rational(1, 2*k)
    l = ((rs-Rational(1, k))*(rs+Rational(1, k))).toFloat()
    if l < 0:
        s = 0
    else:
        s = Rational(-1, k).toFloat() + sqrt(((rs-Rational(1, k))*(rs+Rational(1, k))).toFloat())
    S = Rational(-1, k).toFloat() + sqrt(((rS-Rational(1, k))*(rS+Rational(1, k))).toFloat())
    A = Point(s, 0)
    B = Point(S, 0)
    C = Point(0, s)
    D = Point(0, S)
    if verbose:
        print("----------------  k -> ", k)
        print("Big radius = ", rS.toFloat())
        print("Small radius = ", rs.toFloat())
        print("O = ", Ok)
        print("A = ", A)
        print("B = ", B)
        print("C = ", C)
        print("D = ", D)
        print("Big angle degrees = ", AnglePoints(D, Ok, B)*180/pi)
        print("Big circle section = ", (rS.toFloat())*AnglePoints(D, Ok, B))
        print("Small angle degrees = ", AnglePoints(C, Ok, A)*180/pi)
        print("Small circle section = ", (rs.toFloat())*AnglePoints(C, Ok, A))
        print("Upper triangle = ", abs(TriangleArea(Ok, A, B)))
        print("Lower triangle = ", abs(TriangleArea(Ok, C, D)))
        print("Area = ",  (rS.toFloat())*AnglePoints(D, Ok, B) - (rs.toFloat())*AnglePoints(C, Ok, A) - abs(TriangleArea(Ok, A, B)) - abs(TriangleArea(Ok, C, D)) )
    return (rS.toFloat())*AnglePoints(D, Ok, B) - (rs.toFloat())*AnglePoints(C, Ok, A) - abs(TriangleArea(Ok, A, B)) - abs(TriangleArea(Ok, C, D))
LIM = 10


for k in range(1, LIM+1):
    ans += Proba(k)*k

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")