import time
import math

start_time = time.time()

class Tree:
    def __init__(self, l_branch = None, r_branch = None):
        if l_branch == None or r_branch == None:
            self.leaves = 1
        else:
            self.leaves = l_branch.leaves + r_branch.leaves
        self.l_branch = l_branch
        self.r_branch = r_branch
    
    def print_tree(self):
            if self.leaves == 1:
                return "*"
            return "( " + self.l_branch.print_tree() + ", " + self.r_branch.print_tree() + " )"

    def eval(self, op_map, values):
        #op_map is a list with leaves-1 elements
        #values is a list with leaves elements
        if not(len(op_map) == self.leaves - 1 ) or not(len(values) == self.leaves):
            print("KESTA MERDA - A, leaves = ", self.leaves, ", values = ", values , ", and ops = ", op_map)
            return "KESTA MERDA - B"
        if self.leaves == 1:
            return values[0]
        mid = self.l_branch.leaves
        a = self.l_branch.eval(op_map[1:mid], values[:mid])
        #print(op_map[1:mid], " - ", values[:mid], " - ", a)
        b = self.r_branch.eval(op_map[mid:], values[mid:])
        #print(op_map[mid:1], " - ", values[mid:], " - ", b)
        #print("mid = ", mid, " a = ", a, " and b = ", b, " and op_map = ", op_map[0])
        op = op_map[0]
        if a == "invalid" or b == "invalid":
            return "invalid"
        if op == "+":
            return a + b
        if op == "-":
            if a > b:
                return a - b
            return "invalid"
        if op == "*":
            return a*b
        if op == "/":
            if a%b == 0:
                return a//b
            return "invalid"
        print("HAN")
        return "KESTA MERDA - C"

trees = [[] for i in range(7)]
trees[0] = [Tree()]
for i in range(1, 7):
    for k in range(i):
        for T in trees[k]:
            for U in trees[i-k-1]:
                trees[i].append(Tree(T, U))



## Generate all maps of operations with 0, 1, ..., 6 maps
ops = [[] for i in range(7)]
ops[0] = [[]]
l_o= ["+", "*", "-", "/"]
for i in range(1, 7):
    for lop in ops[i-1]:
        for op in l_o:
            ops[i].append(lop + [op])


"""
T =Tree(Tree(Tree(Tree(), Tree()), Tree()), Tree(Tree(Tree(), Tree()), Tree()))
v = [3, 6, 25, 4, 7, 2]
o = ["-", "*", "+", "/", "*"]
print(T.eval(o, v))
print(sum(list(v)))
"""


from itertools import combinations, permutations

pow3 = 3
mod = 1005075251
tot = 0
count = 1
f = open("chall.txt", "r")
for l in f:
    print("Line nr ", count)
    count += 1
    values = l[:-1].split(",")
    g = values[0].split(":")
    target = int(g[0])
    values[0] = g[1]
    values = [int(v) for v in values]
    s = sum(values)
    min_sum = sum(values) + 1
    for i in range(7):
        for c in combinations(values, i+1):
            s = sum(list(c))
            if s < min_sum:
                for p in permutations(c):
                    for op in ops[i]:
                        for T in trees[i]:
                            t = T.eval(op, list(p))
                            if t == target:
                                min_sum = s
    if min_sum > sum(values):
        min_sum = 0
    tot += pow3*min_sum
    pow3 *= 3
    tot %= mod
    pow3 %= mod

print(tot)
print(" --- %s seconds --- "%(time.time() - start_time))
