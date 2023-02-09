import time
import math

start_time = time.time()

d = 2_000_000
#d = 14
LIM = 2*d
mod = 50515093
s = [290797]*LIM

for i in range(LIM-1):
    s[i+1]=(s[i]**2)%mod
points = [[s[2*i], s[2*i+1]] for i in range(d)]

def d_s(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

sections = 1000
width = 1 + (mod-1)//sections

print("Sections = ", sections)
print("Width = ", width)


def section_of_a_point(P):
    return [p[0]%width, p[1]%width]

points_by_sections = [[[] for j in range(sections)] for k in range(sections)]
for P in points:
    points_by_sections[P[0]//width][P[1]//width].append(P)



def smallest_distance(P, s):
    min_distance = 10**16
    for Q in s:
        if not(P[0] == Q[0]) or not(P[1] == Q[1]):
            min_distance = min(min_distance, d_s(Q, P))
    return min_distance

ans = 10**16

def print_sec(k ,j):
    l = len(print_by_sections[k][j])
    if l > 0:
        print("Section ", k, " - ", j, " has ", len(points_by_sections[k][j]), " elements")

for k in range(sections):
    for j in range(sections):
        ##print("Analyzing secion ", k, " - ", j)
        ##For each point in a section, find point that is closest: our guess is that such a point is within 1 block
        for P in points_by_sections[k][j]:
            d = smallest_distance(P, points_by_sections[k][j])
            if k > 0:
                d = min(d, smallest_distance(P, points_by_sections[k-1][j]))
            if k < sections-1:
                d = min(d,  smallest_distance(P, points_by_sections[k+1][j]))
            if k > 0 and j > 0:
                d = min(d,  smallest_distance(P, points_by_sections[k-1][j-1]))
            if k > 0 and j < sections - 1:
                d = min(d,  smallest_distance(P, points_by_sections[k-1][j+1]))
            if j > 0:
                d = min(d,  smallest_distance(P, points_by_sections[k][j-1]))
            if k < sections - 1 and j > 0:
                d = min(d,  smallest_distance(P, points_by_sections[k+1][j-1]))
            if k < sections - 1 and j < sections - 1:
                d = min(d,  smallest_distance(P, points_by_sections[k+1][j+1]))
            if j < sections - 1:
                d = min(d,  smallest_distance(P, points_by_sections[k][j+1]))
            ans = min(d, ans)
ans = math.sqrt(ans)
print("The shortest distance in the cloud of points is d = ", ans)

print(" --- %s seconds --- "%(time.time() - start_time))
