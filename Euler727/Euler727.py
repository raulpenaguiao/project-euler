import time
import math
import numpy as np
from decimal import Decimal

Decimal('0.0000000001')

start_time = time.time()


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)


def gcd_l(l):
    if len(l) == 1:
        return l[0]
    return gcd_l([gcd(l[0], l[1])] + l[2:])




def d(ra, rb, rc, verbose = False):
    a = rb + rc
    b = rc + ra
    c = ra + rb
    xb = 0
    yb = 0
    xc = rb + rc
    yc = 0
    xa = (a*a + c * c - b * b)/(2*a)
    alphaB = math.acos(xa / c)
    ya = c * c - xa * xa
    ya = math.sqrt(ya)
    xo = rb * xc / a
    yo = math.tan(alphaB/2) * xo
    xca = rb
    yca = 0
    xcb = (xc * ra + xa * rc)/(rc + ra)
    ycb = (yc * ra + ya * rc)/(rc + ra)
    xcc = xa * rb / (rb + ra)
    ycc = ya * rb / (rb + ra)
    xe = 0
    ye = 0
    alpha = (rb - rc) /xc
    beta = (rb ** 2 - rc ** 2 + xc ** 2)/(2*xc)
    alphap = (rb - ra - alpha * xa) / ya
    betap = (rb ** 2 - ra ** 2 + xa ** 2 + ya ** 2 - 2 * beta * xa)/(2 *ya)
    """
    a_2eq = ( xa * (rb - ra) + xa * (rb - rc)) **2 / (ya **2)
    a_2eq += (rb - rc) ** 2
    a_2eq -= xc **2
    b1 = (rb ** 2 - rc ** 2) /2
    b2 = b1 + (xa ** 2 + xb ** 2)/2
    b_2eq = 2* b1 * (rb - rc) / xc
    b_2eq += 2 * (xc * (rb - ra) + xa * (rc - rb)) * (b2 - xa * b1 / xc) / (ya ** 2)
    b_2eq -= 2 * rb
    c_2eq = -rb ** 2
    c_2eq += (b1 / xc) ** 2
    c_2eq += ((b2 - b1 * xa/xc) / ya ) **2
    """
    a_2eq = alpha ** 2 + alphap ** 2 - 1
    b_2eq = 2 * (alpha * beta + alphap * betap - rb)
    c_2eq = beta **2 + betap ** 2 - rb ** 2



    DELTA = b_2eq ** 2 - 4 * a_2eq * c_2eq
    if(verbose):
        print("A = (", xa, ", ", ya, ")")
        print("B = (", xb, ", ", yb, ")")
        print("C = (", xc, ", ", yc, ")")
        print("CA = (", xca, ", ", yca, ")")
        print("CB = (", xcb, ", ", ycb, ")")
        print("CC = (", xcc, ", ", ycc, ")")
        print("alphaB = ", alphaB)
        print("O = (", xo, ", ", yo, ")")
        print("alpha = ", alpha)
        print("beta = ", beta)
        print("alphap = ", alphap)
        print("betap = ", betap)

    if DELTA < 0:
        #There are no real solutions to this problem. This should NEVER happen
        print("FUCK FUCK FUCK")
        r = 0
    else:
        if abs(a_2eq) < 10**-10:#This happens when the tree circles have a common tangent
            r = -c_2eq / b_2eq
            r1 = r
            r2 = r
        else:#In this case there are two solutions
            r2= (-b_2eq - math.sqrt(DELTA))/(2*a_2eq)
            r1= (-b_2eq + math.sqrt(DELTA))/(2*a_2eq)
            if r2 > 0:#if both solutions are positive, both circles are external tangents
                r = r2
            else:#if one solution is negative, it corresponds to an internal tangent
                r = r1
    xe = r * alpha + beta
    ye = r * alphap + betap
    xe1= r1*alpha + beta
    ye1= r1*alphap+ betap
    xe2= r2*alpha + beta
    ye2= r2*alphap+ betap
    if(verbose):
        print(a_2eq, "r^2 + ", b_2eq, " r + ", c_2eq, " = 0")
        print("E = (", xe, ", ", ye, ")")
        print("E1= (", xe1,", ", ye1,") and r1 = ", r1) 
        print("E2= (", xe2,", ", ye2,") and r2 = ", r2)
        print("Let's test tese points")
        print("Distance E to A - ra = ", math.sqrt((xe - xa) ** 2 + (ye - ya)**2)-ra)
        print("Distance E to B - rb = ", math.sqrt((xe - xb) ** 2 + (ye - yb)**2)-rb)
        print("Distance E to C - rc = ", math.sqrt((xe - xc) ** 2 + (ye - yc)**2)-rc)
        print("Distance O to CA = ", math.sqrt((xo - xca) ** 2 + (yo - yca)**2))
        print("Distance O to CB = ", math.sqrt((xo - xcb) ** 2 + (yo - ycb)**2))
        print("Distance O to CC = ", math.sqrt((xo - xcc) ** 2 + (yo - ycc)**2))
    
    ans = math.sqrt((xo - xe)**2 + (yo - ye)**2)
    if ans > 10:
        print("ra = ", ra, " and rb = ", rb, " and rc = ", rc, " | ANS = ", ans)
    return ans

LIM = 101
tot = 0
count = 0
for ra in range(1, LIM):
    for rb in range(ra+1, LIM):
        for rc in range(rb+1, LIM):#This way we have ra < rb < rc, so a > b > c
            if gcd_l([ra, rb, rc]) == 1:
                count += 1
                tot += d(ra, rb, rc)
#print(count) # = 135739
print(tot / count)


print(" --- %s seconds --- "%(time.time() - start_time))
