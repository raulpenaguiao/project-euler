import time
start = time.time()
ans = 0
from math import sqrt, pi

EPS = 0.001

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def MidPoint(self, other):
        return Point((self.x+other.x)/2, (self.y+other.y)/2)


class AxisElipses:
    def __init__(self, center, sx, sy):
        self.center = center
        self.sx = sx
        self.sy = sy
    

    def IsInside(self, point):
        ((self.center.x - point.x)/self.sx)**2 + ((self.center.y - point.y)/self.sy)**2 <= 1 + EPS

    
    def TangentAngle(self, point):
        if self.IsInside(point):
            return 2*pi
        
        return 0


M = Point(-2000, 1500)
G = Point(8000, 1500)
C = M.MidPoint(G)
r = 15000
U = Point(-2000+r, 1500)
E = U.MidPoint(G)
height = sqrt(r*r-(M.x-G.x)**2)
T = Point(G.x, G.y+height)
L = T.MidPoint(M)

s_x = C.x - E.x
s_y = L.y - C.y



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")