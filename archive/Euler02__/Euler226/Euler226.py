#Code written in 2024/06/04
#To compute desired area, it computes the integral of the BM curve
#Removes area of trapezoid
#Adds chordal section area
#Assumes that the curve intersects the circle in only two points, the second one is computed using binary search
#Runs in 9ms



import time
start = time.time()
from decimal import Decimal, getcontext
getcontext().prec = 40
import math
PREC = Decimal(10)**(-20)
ans = 0


def s(x):
    y = Decimal(x)%Decimal(1)
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


def IntegralBM(a):
    x = Decimal(a)
    if not (0 <= x and x < 1):
        return IntegralBM(x%1) + (x//1)/2
    if x > Decimal(0.5):
        return Decimal(0.5) - IntegralBM(1 - x)
    if x < PREC:
        return 0
    return x*x/2+IntegralBM(2*x)/4

def Angle(v1, v2):
    return Decimal(math.acos((v1[0]*v2[0]+v1[1]*v2[1])/Decimal(math.sqrt(Norm(v1)*Norm(v2)))))


def Norm(v):
    return v[0]**2 + v[1]**2

def AreaSectionCricle(center, radius, p1, p2):
    #Compute angle between, in radians
    v1 = tuple([center[0] - p1[0], center[1]-p1[1]])
    v2 = tuple([center[0] - p2[0], center[1]-p2[1]])
    alpha = Angle(v1, v2)
    #compute area of triangle in between
    Atriangle = Decimal(math.sin(alpha))*Decimal(math.sqrt(Norm(v1)*Norm(v2)))/2
    return alpha*radius*radius/Decimal(2) - Atriangle


#print("pitagoras triangle angle is ", Angle([0, 1], [3, 4])*Decimal(180/3.141592))
#print(AreaSectionCricle([0, 0], 1, [0, 1], [1, 0]))


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

print("Second intersection point is (", bot, ", ", B(bot), ")")

print(IntegralBM(bot))

a = AreaSectionCricle(
    tuple([Decimal(0.25), Decimal(0.5)]), 
    Decimal(0.25), 
    tuple([bot, B(bot)]), 
    tuple([Decimal(0.5), Decimal(0.5)]))

print("chordal secion of circle = ", a)
b = IntegralBM(Decimal(0.5)) - IntegralBM(bot)
print("area under the curve = ", b)
c = (Decimal(0.5) - bot)*(Decimal(0.5) + B(bot))/2
print("trapezoid area = ", c)
AREA = a + b - c


print("Answer = ", AREA)
end = time.time()
print("Time elapsed ", end - start, " seconds")