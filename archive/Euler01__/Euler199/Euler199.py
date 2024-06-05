#Code written in 2023/11/29
#inCircle is a function that given three circles, finds the smallest circle that is externally tangent to all three, if it exists
#running this 3^9 times computes the exact coordinates and radii of each circle
#float errors do not avalanche because of the decimal library (prec = 10 is enough, this is a mistery)
#Runs in 1.86s

import time
start = time.time()
import math
from ...CL.CL_Geometry import Point
from decimal import Decimal, getcontext
getcontext().prec = 10
PREC = Decimal(10)**(-6)


def inCircle(Ca, Cb, Cc, verbose = False):
    ra = Ca[1]
    rb = Cb[1]
    rc = Cc[1]
    xa = Ca[0].x
    xb = Cb[0].x
    xc = Cc[0].x
    ya = Ca[0].y
    yb = Cb[0].y
    yc = Cc[0].y
    if(verbose):
        print("ra = ", ra, " | xa = ", xa, " | ya = ", ya, " | rb = ", rb, " | xb = ", xb, " | yb = ", yb, " | rc = ", rc, " | xc = ", xc, " | yc = ", yc)
    s11 = Decimal(2)*(ra - rb)
    s21 = Decimal(2)*(rb - rc)
    s12 = ra*ra-rb*rb+yb*yb-ya*ya+xb*xb-xa*xa
    s22 = rb*rb-rc*rc+yc*yc-yb*yb+xc*xc-xb*xb
    if(verbose):
        print("s11 = ", s11, "| s12 = ", s12, "| s21 = ", s21, "| s22 = ", s22)
    m11 = xb - xa
    m12 = yb - ya
    m21 = xc - xb
    m22 = yc - yb
    d = m11*m22-m12*m21
    d *= Decimal(2)
    if(verbose):
        print("M11 = ", m11, "| M12 = ", m12, "| M21 = ", m21, "| M22 = ", m22)
        print("d =  ", d)
    r11 = s11 * m22 - s21 * m12
    r12 = s12 * m22 - s22 * m12
    r21 = s21 * m11 - s11 * m21
    r22 = s22 * m11 - s12 * m21
    if(verbose):
        print("r11 = ", r11, "| r12 = ", r12, "| r21 = ", r21, "| r22 = ", r22)
    r11 /= d
    r21 /= d
    r12 /= d
    r22 /= d
    if(verbose):
        print("r11 = ", r11, "| r12 = ", r12, "| r21 = ", r21, "| r22 = ", r22)
    a = r11*r11+r21*r21 - Decimal(1) 
    b = r11*(r12 - xa) + r21*(r22 - ya) - ra
    b *= Decimal(2)
    c = (r12-xa)*(r12-xa)+(r22-ya)*(r22-ya)-ra*ra
    if a < 0:
        if(verbose):
            print("FLOP")
        a *= -Decimal(1)
        b *= -Decimal(1)
        c *= -Decimal(1)
    if(verbose):
        print("Quad a = ", a,  "| b = ", b, " | c = ", c, b*b, a*c, b*b-Decimal(4)*a*c)
    rm = (-b - Decimal(math.sqrt(b*b-Decimal(4)*a*c)))/(2*a)
    rp = (-b + Decimal(math.sqrt(b*b-Decimal(4)*a*c)))/(2*a)
    
    if(verbose):
        print("Value quadratic ", a*rm*rm+b*rm+c)
    if(verbose):
        print("Value quadratic ", a*rp*rp+b*rp+c)
    xp = r11*rp + r12
    yp = r21*rp + r22

    
    xm = r11*rm + r12
    ym = r21*rm + r22
    if(verbose):
        print([Point(xm, ym), str(rm)], [Point(xp, yp), str(rp)])
    if rm < 0:
        r = rp
    else:
        r = rm
    x = r11*r + r12
    y = r21*r + r22
    if(verbose):
        print(x, y, r)
    if r < 0:
        print("ERROR! r < 0 :: r = " ,r)
    err = (x-xa)**2 + (y-ya)**2 - (r+ra)**2
    if err > PREC:
        print("ERROR = ", err)
    err = (x-xb)**2 + (y-yb)**2 - (r+rb)**2
    if err > PREC:
        print("ERROR = ", err)
    err = (x-xc)**2 + (y-yc)**2 - (r+rc)**2
    if err > PREC:
        print("ERROR = ", err)
    return [Point(x, y), r]



getcontext().prec = 30
R= Decimal(1)
O = Point(0, 0)
r = Decimal(math.sqrt(Decimal(3)))/(Decimal(2)+Decimal(math.sqrt(Decimal(3))))
r0 = Decimal(1) - Decimal(2)*r
C = [O, -R]#maincircle
C1 = [Point(0, r+r0), r]#circle 1, top
C2 = [Point(r, -r/Decimal(math.sqrt(Decimal(3)))), r]#circle 2, right
C3 = [Point(-r, -r/Decimal(math.sqrt(Decimal(3)))), r]#circle 3, left


circles = [C1, C2, C3]
triangles = [[C1, C2, C3], [C1, C3, C], [C3, C2, C], [C1, C2, C]]#

"""
r = Decimal(math.sqrt(2)) + 1
print(inCircle([CG.Point(0, 0), Decimal(1)], [CG.Point(r + 1, 0), r], [CG.Point(0, r + 1), r]))
"""
for i in range(10):
    newtriangles = []
    for t in triangles:
        #print("Evaluating circles, ", t)
        newC = inCircle(t[0], t[1], t[2])
        newtriangles.append([t[0], t[1], newC])
        newtriangles.append([t[0], newC, t[2]])
        newtriangles.append([newC, t[1], t[2]])
        circles.append(newC)
    triangles = newtriangles[:]

ans = 0
for c in circles:
    ans += c[1]**2
print("Answer = ", 1 - ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")