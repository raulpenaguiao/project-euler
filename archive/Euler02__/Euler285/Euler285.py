#Code written on the 04/01/2024
#Sampling a and b is sampling a point in the unit square
#The probability is the area of this square intersected with an anular region
#Compute numerically for each k the angle of the circular sections, minus a triangle, gives the desired area
#Runs in 4.320313692 seconds


import time
from math import acos
from decimal import Decimal, getcontext
pi = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089")
getcontext().prec = 80
from ...CL.CL_Rational import Rational
from ...CL.CL_Geometry import Point, VectorTwoPoints
start = time.time()
O = Point(0, 0)
def AVector(V1, V2):
    return Decimal(acos(V1.innerProduct(V2)/Decimal(V1.norm()*V2.norm())))

def Proba(k):
    Ok = Point(Rational(-1, k).toDecimal(), Rational(-1, k).toDecimal())
    rs = Rational(1)-Rational(1, 2*k)
    rS = Rational(1)+Rational(1, 2*k)
    l = ((rs-Rational(1, k))*(rs+Rational(1, k)))
    if l < Rational(0):
        s = 0
    else:
        s = Rational(-1, k).toDecimal() + l.toDecimal().sqrt()
    L = ((rS-Rational(1, k))*(rS+Rational(1, k)))
    S = Rational(-1, k).toDecimal() + L.toDecimal().sqrt()
    A = Point(s, 0)
    B = Point(S, 0)
    hAreaBigSection =  (rS.toDecimal())*(rS.toDecimal())*AVector(VectorTwoPoints(Ok, O), VectorTwoPoints(Ok, B))/2
    hAreaSmallSection = (rs.toDecimal())*(rs.toDecimal())*AVector(VectorTwoPoints(Ok, O), VectorTwoPoints(Ok, A))/2
    AreaTriangle = Decimal((S - s)/(2*k))
    
    return 2*(hAreaBigSection - hAreaSmallSection - AreaTriangle)

ans = 0
LIM = 10**5
for k in range(1, LIM+1):
    ans += Proba(k)*k

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")