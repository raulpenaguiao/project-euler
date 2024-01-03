from math import acos, sqrt, sin, cos, pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y


    def Plus(self, vector):
        pt = Point(self.x, self.y)
        pt.add(vector)
        return pt

    def rotate(self, alpha):
        newx = self.x * cos(alpha) - self.y * sin(alpha)
        self.y = self.x * sin(alpha) + self.y * cos(alpha)
        self.x = newx
    

    def Rotation(self, alpha):
        pt = Point(self.x, self.y)
        pt.rotate(alpha)
        return pt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def innerProduct(self, vec):
        return self.x*vec.x + self.y*vec.y

def AngleVector(V1, V2):
    return acos(V1.innerProduct(V2)/(V1.norm()*V2.norm()))


def AnglePoints(P1, P2, P3):
    #Returns the angle around P2, in radians, as a non-negative real number
    v1 = Vector(P1.x - P2.x, P1.y - P2.y)
    v2 = Vector(P3.x - P2.x, P3.y - P2.y)
    return AngleVector(v1, v2)


def TriangleArea(P1, P2, P3):
    #Returns the signed area of the triangle
    v1 = Vector(P1.x - P2.x, P1.y - P2.y)
    v2 = Vector(P3.x - P2.x, P3.y - P2.y)
    return v1.innerProduct(v2)/2

import random
random.seed(73)
#Test for translation and rotation
for i in range(100):
    A = Point(random.random(), random.random())
    B = Point(random.random(), random.random())
    C = Point(random.random(), random.random())
    vec = Vector(random.random(), random.random())
    theta = random.random()*2*pi
    if abs(TriangleArea(A, B, C) - TriangleArea(A.Plus(vec).Rotation(theta), B.Plus(vec).Rotation(theta), C.Plus(vec).Rotation(theta))) > 10**-4:
        print("Unit test failed for TriangleArea")
        print(A, B, C, vec, theta)
    if abs(AnglePoints(A, B, C) - AnglePoints(A.Plus(vec).Rotation(theta), B.Plus(vec).Rotation(theta), C.Plus(vec).Rotation(theta))) > 10**-4:
        print("Unit test failed for AnglePoints")
        print(A, B, C, vec, theta)
