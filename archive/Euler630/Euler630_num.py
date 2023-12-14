import time
import math

start_time = time.time()


LIM = 2500
NUM = 50515093


def next(a):
    return (a ** 2) % NUM
#computes the next term in the S sequence


def red(a):
    return (a%2000 - 1000)
#reduces the term into the [-1000, 1000] interval, as per the problem setting


a = next(290797)
T = set()
index = 0
while len(T) < LIM:
    b = next(a)
    pt = (red(a), red(b))
    T.add(pt)
    a = next(b)
#This creates the set of LIM points
#print("There are ", len(T), " points")

lines = set()

def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a%b)



def create_line(pt1, pt2):
    if pt1[0] == pt2[0]:
        return ((0, -1), (pt1[0], 1))
    U = pt1[1] - pt2[1]
    S = pt1[0] - pt2[0]
    d = gcd(U, S)
    slope = (S // d, U //d)
    if slope[0] < 0:
        slope = (-slope[0], -slope[1])
    
    u = slope[0] * pt1[1] - slope[1] * pt1[0]
    s = slope[0]
    d = gcd(s, u)
    y_inter = (s // d, u // d)
    if y_inter[0] < 0:
        y_inter = (-y_inter[0], -y_inter[1])
    return (slope, y_inter)
#Given two points, this code creates the line that goes through the points
#The data structure is the following: ((a, b), (c, d)) where a/b is the slope, in coprime integers, c/d is the y_intersect
#Be careful when the line is parallel to the y axis


def compare_slopes(l1, l2):
    return l1[0][1] * l2[0][0] == l1[0][0] * l2[0][1]

def compare_y_intersect(l1, l2):
    return l1[1][1] * l2[1][0] == l1[1][0] * l2[1][1]


#We now create all lines. We use sets to delete duplicates, python prefers it done this way rather than aposteriori
for pt1 in T:
    for pt2 in T:
        if not pt1 == pt2:
            lines.add(create_line(pt1, pt2))
lines_list = []
for l in lines:
    lines_list += [l]


def compare_key(l):
    if l[0][0] == 0:
        return [0, 1]
    return [1, l[0][1] / l[0][0]]
lines_list.sort(key= compare_key )
#print_lines(lines_list)
#This sorts the lines int increasing slope, which will be useful for the next block formation step

it = 1
l = len(lines_list)
box = 0
lines_list_boxed = [[lines_list[0]]]
while it < l:
    #compare lines_list[it] and lines_list[it-1]
    #if they have the same slope, just check if they have the same y_intersect as well or smth
        #if yes, DANGER, print error message
        #if not add lines_list[it] to lines_list_boxed[box]
    #if they do not have the same slope, add [lines_list[it]] to lines_list_boxed and box += 1
    if compare_slopes(lines_list[it], lines_list[it-1]):
        #do they have the same intersect
        if compare_y_intersect(lines_list[it], lines_list[it-1]):
            print("DANGER")
        else:
            lines_list_boxed[box].append(lines_list[it])
    else:
        lines_list_boxed.append([])
        box += 1
        lines_list_boxed[box].append(lines_list[it])
    it += 1

#lines_list_boxed corresponds to the set of lines with each box having all the lines paralel to eachother
#print("The partition of the lines is ",  " - ".join([str(len(k)) for k in lines_list_boxed if len(k) > 1 ]))
ans_M = len(lines_list)
ans_S = 0
for box in lines_list_boxed:
    ans_S += len(box) * (ans_M - len(box))

print("M(", LIM , ") = ", ans_M, " and S(", LIM, ") = ", ans_S)
print(" --- %s seconds --- "%(time.time() - start_time))
