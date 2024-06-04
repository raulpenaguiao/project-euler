
#Coded on the 26/10/2023
#Creates all binary planar trees with all possible five operations (including concatenation) in internal nodes
#We do not allow for internal nodes to have concat when some child is not concat
#Because of division, we have to check if a number is "close" to an integer
#Make sure that when saving a key to the dictionary, we save the integer (so we dont double count)
#code runs in 476s (8 minutes)

import time
import math
start = time.time()

class RPBTree:
    def __init__(self, op = None, left = None, right = None):
        if(op == None):
            self.canConcatenate = True
            self.isRoot = True
            self.nodes = 1
            self.op = None
            self.left = None
            self.right = None
        else:
            self.canConcatenate = ( left.canConcatenate and right.canConcatenate and op == "conc")
            self.isRoot = False
            self.nodes = left.nodes + right.nodes
            self.op = op
            self.left = left
            self.right = right
    

    def __str__(self):
        if(self.isRoot):
            return "<>"
        return "(" + str(self.left) + ")" + self.op + "(" + str(self.right) + ")"

    def evaluate(self, l):
        #We assume the list has the same number of nodes as the tree
        #Assume that self is not the trivial tree
        if( self.left.isRoot ):
            leftValue = l[0]
        else:
            leftValue = self.left.evaluate(l[:self.left.nodes])
        if( self.right.isRoot ):
            rightValue = l[-1]
        else:
            rightValue = self.right.evaluate(l[-self.right.nodes:])
        if(leftValue == "NAN" or rightValue == "NAN"):
            return "NAN"
        if(self.op == "conc"):
            return leftValue * (10**nDigs(rightValue) ) + rightValue
        if(self.op == "-"):
            return leftValue - rightValue
        if(self.op == "+"):
            return leftValue + rightValue
        if(self.op == "/"):
            if abs(rightValue) < 0.00000000001:
                return "NAN"
            return leftValue / rightValue
        if(self.op == "x"):
            return leftValue * rightValue

#veryverbose = True
veryverbose = False

#verbose = True
verbose = False

DIGS = 3 #12 numbers - 255
DIGS = 4 # 44 numbers - 4179
DIGS = 5 # 181 numbers - 74689
DIGS = 6 # 736 numbers - 1486823
DIGS = 7 # 3258 numbers - 32533866
DIGS = 8 # 15370 numbers - 782204419
DIGS = 9 # 72586 numbers - 20101196798

def nDigs(k):
    n = k
    ans = 1
    while(n > 10):
        n /= 10
        ans += 1
    return ans


trees = [[] for i in range(DIGS + 1)]
trees[1] = [RPBTree()]
ops = ["+", "-", "x", "/", "conc"]
for i in range(2, DIGS+1):
    for j in range(1, i):
        for T1 in trees[j]:
            for T2 in trees[i-j]:
                for op in ops:
                    if(not(op == "conc") or (T1.canConcatenate and T2.canConcatenate)):
                        trees[i].append(RPBTree(op, T1, T2))



ans_dict = {}

for T in trees[DIGS]:
    t = T.evaluate([i for i in range(1, DIGS + 1)])
    if(veryverbose): print(T, " == ", t)
    if (not(t == "NAN") and t > 0 and t - math.floor(t+0.01) < 0.000001):
        if(verbose): print(T, " == ", t)
        ans_dict[math.floor(t+0.01)] = True
ans = 0
number_of_numbers = 0
for t in ans_dict.keys():
    ans += t
    number_of_numbers += 1
    if(veryverbose): print(t)
print("Answer = ", ans)
print("Number of positive reachable integers = ", number_of_numbers)
end = time.time()
print("Time elapsed ", end - start, " seconds")