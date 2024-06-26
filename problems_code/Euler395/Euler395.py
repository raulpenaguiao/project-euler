import time
start = time.time()
from decimal import Decimal, getcontext
getcontext().prec = 46
from queue import Queue
from math import sqrt

fx = Decimal(4)/Decimal(5)
fy = Decimal(3)/Decimal(5)

zx = Decimal(9)/Decimal(5)
zy = Decimal(3)/Decimal(5)


zlen = sqrt(zx*zx+zy*zy)

def MultComplexNumbers(ax, ay, bx, by):
    return ax*bx-ay*by, ax*by+ay*bx


def Rop(ptx, pty, dirx, diry):
    dirfx, dirfy = MultComplexNumbers(dirx, diry, fx, fy)
    return ptx+dirx, pty+diry, dirfx*Decimal(3)/Decimal(5), dirfy*Decimal(3)/Decimal(5)

def Lop(ptx, pty, dirx, diry):
    dirzx, dirzy = MultComplexNumbers(dirx, diry, zx, zy)
    dirfx, dirfy = MultComplexNumbers(dirx, diry, fx, fy)
    dirfex, dirfey = MultComplexNumbers(dirfx, dirfy, Decimal(0), Decimal(1))
    return ptx+dirzx, pty+dirzy, dirfex*Decimal(4)/Decimal(5), dirfey*Decimal(4)/Decimal(5)



q = Queue()
q.put([0, 0, 0, 1])
minx = 0

#Find leftmost guy
while not q.empty():

    x1, x2, x3, x4 = q.get()

    a1, a2, a3, a4 = Lop(x1, x2, x3, x4)
    b1, b2, b3, b4 = Rop(x1, x2, x3, x4)

    veca = sqrt(a3*a3+a4*a4)
    if a1 < minx + veca*zlen*4:
        q.put([a1, a2, a3, a4])
    
    vecb = sqrt(b3*b3+b4*b4)
    if b1 < minx + vecb*zlen*4:
        q.put([b1, b2, b3, b4])
    




print("Answer = ", minx)
end = time.time()
print("Time elapsed ", end - start, " seconds")