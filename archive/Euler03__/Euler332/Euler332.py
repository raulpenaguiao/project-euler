#Code written on the 21/12/2023
#For each integer vector in a 100x100x100 cube see if it has a ninteger distanc to the origin
#If so, save it on the corresponding slot
#For each slot, generate all triangles and compute the area
#Area is given by Girard's theorem, that says the area of a triangle is given by the sum of its angles
#We actually compute the angle between the normals, which gives the complementary angle
#Runs in 1107.95 seconds


import time
start = time.time()
from decimal import Decimal, getcontext
getcontext().prec = 46
import math


def Normal(p1, p2):
    return[p1[1]*p2[2]-p1[2]*p2[1], p1[2]*p2[0]-p1[0]*p2[2], p1[0]*p2[1]-p1[1]*p2[0]]


def NormS(p):
    return DotProduct(p, p)

def DotProduct(p1, p2):
    return p1[0]*p2[0]+p1[1]*p2[1]+p1[2]*p2[2]

def Angle(p1, p2):
    return Decimal(math.acos(DotProduct(p1, p2)/Decimal(math.sqrt(NormS(p1)*NormS(p2)))))

#print("Angle = ", Angle([1, 0, 0], [1, 1, 1]))
#print(math.atan(math.sqrt(2)))
#print("Angle = ", Angle([1, 0, 0], [1, 1, 0]))

def Det(p1, p2, p3):
    return p1[0]*p2[1]*p3[2]+p1[1]*p2[2]*p3[0]+p1[2]*p2[0]*p3[1]-p1[0]*p2[2]*p3[1]-p1[2]*p2[1]*p3[0]-p1[1]*p2[0]*p3[2]

if not Det([1, 0, 0], [0, 2, 1] ,[0, 1, 2]) == 3:
    raise Exception("Something wrong is not right")



LIM = 50
pts = {i*i:[] for i in range(1, LIM+1)}
PREC = Decimal("0.0000000000001")
PI = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")

def AreaInSphere(p1, p2, p3, radS):
    d = Det(p1, p2, p3)
    if abs(d) < PREC:
        return 0
    n1 = Normal(p2, p3)
    if d*Det(n1, p2, p3) < 0:
        n1 = [-n for n in n1]
    n2 = Normal(p3, p1)
    if d*Det(p1, n2, p3) < 0:
        n2 = [-n for n in n2]
    n3 = Normal(p1, p2)
    if d*Det(p1, p2, n3) < 0:
        n3 = [-n for n in n3]
    return (2*PI - Angle(n1, n2) - Angle(n2, n3) - Angle(n3, n1))*radS


for a in range(-LIM, LIM+1):
    for b in range(-LIM, LIM+1):
        for c in range(-LIM, LIM+1):
            rsq = a**2+b**2+c**2
            if rsq in pts:
                pts[rsq].append([Decimal(a), Decimal(b), Decimal(c)])

def A(i):
    l = len(pts[i])
    minArea = PI*i/Decimal(2)    
    for l1 in range(l):
        p1 = pts[i][l1]
        for l2 in range(l1):
            p2 = pts[i][l2]
            for l3 in range(l2):
                p3 = pts[i][l3]
                area = AreaInSphere(p1, p2, p3, Decimal(i))
                if area > PREC and area < minArea:
                    minArea = area 
                    #print(minArea,  " updated from ", p1, p2, p3)
    return minArea

tot = 0
for i in pts:
    end = time.time()
    tot += A(i)

print("Answer = ", tot)
end = time.time()
print("Time elapsed ", end - start, " seconds")