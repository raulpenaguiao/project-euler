#Code written on the 2024/05/16
#Uses sieve to compute all primes < 10**8
#Creates a tree structure to save all binary expansions of the primes and easily access how many prime numbers have a specific suffix
#For each subtree compute the score (probability of choosing the right number at the root) recursively
#Runs in 70.2 seconds, most of it is in my inefficient sieving


import time
start = time.time()
from ...CL.CL_Primes import MillerRabin, Primes
from ...CL.CL_Rational import Rational

class BinaryTree:
    def __init__(self):
        self.hasLeft = False
        self.hasRight = False
        self.weight = 0
        self.weight_below = 0
        return
    
    def addLeaf(self, sign):
        self.weight += 1
        if sign == []:
            return
        self.weight_below += 1
        if sign[-1] == 0:
            if not self.hasRight:
                self.hasRight = True
                self.right = BinaryTree()
            self.right.addLeaf(sign[:-1])
        else:
            if not self.hasLeft:
                self.hasLeft = True
                self.left = BinaryTree()
            self.left.addLeaf(sign[:-1])

    def total_score(self):
        ans = 0
        if self.hasLeft:
            ans += self.left.weight + self.left.total_score()
        if self.hasRight:
            ans += self.right.weight + self.right.total_score()
            if self.hasLeft:
                ans += max(self.left.weight, self.right.weight)
        return ans    

def digits(n, base = 2):
    if n < base:
        return [n]
    return digits(n//base) + [n%base]


def addNumToTree(bt, num):
    dlist = digits(num)
    bt.addLeaf(dlist)

LIM = 10**8
bt = BinaryTree()
for p in Primes(LIM):
    addNumToTree(bt, p)
print("Primes compiled")
print("Answer = ", Rational(bt.total_score(), bt.weight).toFloat())
end = time.time()
print("Time elapsed ", end - start, " seconds")