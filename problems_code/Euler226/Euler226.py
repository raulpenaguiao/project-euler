import time
start = time.time()
from decimal import Decimal, getcontext
getcontext().prec = 40
import math
PREC = Decimal(10)**(-20)
ans = 0


def s(x):
    y = x%1
    return min(y, Decimal(1)-y)

def B(x):
    y = Decimal(x)%1
    z = 1
    ans = s(y)
    while(y*PREC < Decimal(1)):
        y*=Decimal(2)
        z*=Decimal(2)
        ans += s(y)/z
    return ans 


def IsInCircle(x, y):
    return (x-Decimal(0.25))**2 + (y - Decimal(0.5))**2 <= 0.25**2

top = Decimal(0.5)
bot = Decimal(0)
while(top - bot > PREC):
    mid = (top+bot)/2
    ymid = B(mid)
    #Check if (mid, ymid) is inside the circle or not
    if IsInCircle(mid, ymid):
        top = mid
    else:
        bot = mid

def IntegralBM(a):
    if not (0 <= a and a < 1):
        return IntegralBM(a%1) + (a//1)/2
    if a > Decimal(0.5):
        return Decimal(0.5) - IntegralBM(1 - a)
    if a < PREC:
        return 0
    return a*a/2+IntegralBM(2*a)/4

def Angle(v1, v2):
    print((v1[0]*v2[0]+v1[1]*v2[1]))
    print(Norm(v1))
    print(Norm(v2))
    print(Decimal(v1[0]*v2[0]+v1[1]*v2[1]))
    print(Decimal(math.sqrt(Norm(v1)*Norm(v2))))
    return Decimal(math.acos((v1[0]*v2[0]+v1[1]*v2[1])/Decimal(math.sqrt(Norm(v1)*Norm(v2)))))

def Norm(v):
    return v[0]**2 + v[1]**2

def AreaSectionCricle(center, radius, p1, p2):
    #Compute angle between, in radians
    v1 = tuple([center[0] - p1[0], center[1]-p1[1]])
    v2 = tuple([center[0] - p2[0], center[1]-p2[1]])
    alpha = Angle(v1, v2)
    #compute area of triangle in between
    Atriangle = Decimal(math.sin(alpha))*Norm(v1)*Norm(v2)/2
    return alpha*radius - Atriangle

a = AreaSectionCricle(tuple([Decimal(0.25), Decimal(0.5)]), Decimal(0.25), tuple([bot, B(bot)]), tuple([Decimal(0.5), Decimal(0.5)]))
b = IntegralBM(Decimal(0.5)) - IntegralBM(bot)
c = (Decimal(0.5) - bot)*(Decimal(0.5) + B(bot))/2
AREA = a + b - c
print("Answer = ", AREA)
end = time.time()
print("Time elapsed ", end - start, " seconds")