#Code written on the 13/11/2023
#For four points, computes four determinantes to check that the points form a convex hull in the determined order
#In this case, we compute the desired intersection point
#We need to rule out the case of several lines intersecting at the same point
#For that we develop a rational data class to be able to check if a point is already the intersection
#Runs in 32.2 seconds



import time
import math
start = time.time()
ans = 0

MOD = 50515093
LINES = 5000
t = 290797
s = [t]

PI = 3.1415926535
PREC = 0.00001


def Det(mat):
    ans = mat[0][0]*mat[1][1]*mat[2][2]+mat[0][1]*mat[1][2]*mat[2][0]+mat[0][2]*mat[1][0]*mat[2][1]
    ans -= mat[0][0]*mat[1][2]*mat[2][1]+mat[0][1]*mat[1][0]*mat[2][2]+mat[0][2]*mat[1][1]*mat[2][0]
    return ans

def isTrueIntersection(l1, l2):
    a = Det([[l1[1], l1[3], l2[1]], [l1[2], l1[4], l2[2]], [1, 1, 1]])
    b = Det([[l1[1], l1[3], l2[3]], [l1[2], l1[4], l2[4]], [1, 1, 1]])
    if a*b >= 0:
        return False
    c = Det([[l2[1], l2[3], l1[1]], [l2[2], l2[4], l1[2]], [1, 1, 1]])
    d = Det([[l2[1], l2[3], l1[3]], [l2[2], l2[4], l1[4]], [1, 1, 1]])
    if c*d >= 0:
        return False
    return True


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)


def Reduce(l):
    if(l[1] == 0):
        raise Exception("Division by zero")
    if l[0] > 0:
        if l[1] > 0:
            d = GCD(l[0], l[1])
            return [l[0]//d, l[1]//d]
        if l[1] < 0:
            d = GCD(l[0], -l[1])
            return [-l[0]//d, -l[1]//d]
    if l[0] < 0:
        if l[1] > 0:
            d = GCD(-l[0], l[1])
            return [l[0]//d, l[1]//d]
        if l[1] < 0:
            d = GCD(-l[0], -l[1])
            return [-l[0]//d, -l[1]//d]
    return [0, 1]


def IntersectionPoint(l1, l2):
    a = l1[2] - l1[4]
    b = l2[2] - l2[4]
    c = l1[3] - l1[1]
    d = l2[3] - l2[1]
    b1 = l1[3]*l1[2]-l1[1]*l1[4]
    b2 = l2[3]*l2[2]-l2[1]*l2[4]
    return [ Reduce([d*b1-c*b2, a*d-b*c]) , Reduce([a*b2-b*b1, a*d-b*c])]


def DeleteCopies(st):
    if st == []:
        return []
    t = sorted(st)
    ans = [t[0]]
    for i in range(1, len(t)):
        if not(t[i][1:] == t[i-1][1:]):
            ans += [t[i]]
    return ans


def DeleteCopiesRationalPoints(st):
    if st == []:
        return []
    t = sorted(st)
    ans = [t[0]]
    for i in range(1, len(t)):
        if not( t[i][0][0]*t[i-1][0][1] == t[i][0][1]*t[i-1][0][0]) or not(t[i][1][0]*t[i-1][1][1] == t[i][1][1]*t[i-1][1][0]) :
            ans += [t[i]]
    return ans

for _ in range(1, 4*LINES+1):
    t = t*t
    t %= MOD
    s += [t%500]

lns = [[0, s[4*i+1], s[4*i+2], s[4*i+3], s[4*i+4]] for i in range(LINES)]
lns = DeleteCopies(lns)

def CountTrueIntersections(lns):
    l = len(lns)
    ans = []
    for i in range(l):
        for j in range(i):
            if isTrueIntersection(lns[i], lns[j]):
                pt = IntersectionPoint(lns[i], lns[j])
                ans += [pt]    
    ans = DeleteCopiesRationalPoints(ans)
    return len(ans)


#print(CountTrueIntersections([[0, 2, 5, 5, 6], [0, 4, 1, 6, 3], [0, 2, 2, 8, 2], [0, 4, 1, 2, 8], [0, 6, 1, 3, 4]])) # > 4
#print(CountTrueIntersections([[0, 27, 44, 12, 32], [0, 46, 53, 17, 62], [0, 46, 70, 22, 40]])) # > 1


print("Answer = ", CountTrueIntersections(lns))
end = time.time()
print("Time elapsed ", end - start, " seconds")