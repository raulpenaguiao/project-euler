import time
start = time.time()
from ...CL.CL_Primes import MillerRabin

class BinaryTree:
    def __init__(self):
        self.hasElement = False
        self.hasLeft = False
        self.hasRight = False
        self.elementsBelow = 0
        self.elements = 0
        return
    
    def addElement(self, path):
        self.elements += 1
        if path == []:
            self.hasElement = True
        else:
            self.elementsBelow += 1
            if path[0] == 0:
                if self.hasRight:
                    self.right.addElement(path[1:])
                else:
                    self.hasRight = True
                    self.right = BinaryTree()
                    self.right.addElement(path[1:])
            else:
                if self.hasLeft:
                    self.left.addElement(path[1:])
                else:
                    self.hasLeft = True
                    self.left = BinaryTree()
                    self.left.addElement(path[1:])
    
    def hits(self):
        if not self.hasLeft:
            if not self.hasRight:
                return 0
            else:
                return self.right.hits()+1
        else:
            if not self.hasRight:
                return self.left.hits()+1
            else:
                maxBranch = max(self.left.elementsBelow, self.right.elementsBelow)
                return (self.left.hits()*self.left.elements + self.right.hits()*self.right.elements + maxBranch)/self.elements
                

    def __repr__(self):
        if self.hasElement and self.hasLeft and self.hasRight:
            return "( " + self.left.__repr__() + " )" + " <> " + "[ " + self.right.__repr__() + " ]"
        if self.hasElement and self.hasLeft and not self.hasRight:
            return "( " + self.left.__repr__() + " )" + " <> []"
        if self.hasElement and not self.hasLeft and self.hasRight:
            return "() <> " + "[ " + self.right.__repr__() + " ]"
        if self.hasElement and not self.hasLeft and not self.hasRight:
            return "() <> []"
        if not self.hasElement and self.hasLeft and self.hasRight:
            return "( " + self.left.__repr__() + " )"+ "[ " + self.right.__repr__() + " ]"
        if not self.hasElement and self.hasLeft and not self.hasRight:
            return "( " + self.left.__repr__() + " ) []"
        if not self.hasElement and not self.hasLeft and self.hasRight:
            return "() [ " + self.right.__repr__() + " ]"
        if not self.hasElement and not self.hasLeft and not self.hasRight:
            return "() : []"


def digits(n, base = 2):
    if n < base:
        return [n]
    return digits(n//base) + [n%base]


def addNumToTree(bt, num):
    dlist = digits(num)
    dlist.reverse()
    bt.addElement(dlist)

LIM = 30
bt = BinaryTree()
addNumToTree(bt, 2)
for i in range(3, LIM+1, 2):
    if MillerRabin(i):
        addNumToTree(bt, i)

def printHits(bt):
    print(bt.hits(), bt)
    if bt.hasLeft and bt.hasRight:
        printHits(bt.right)
        printHits(bt.left)
    if bt.hasLeft and not bt.hasRight:
        printHits(bt.left)
    if not bt.hasLeft and bt.hasRight:
        printHits(bt.right)


printHits(bt)
ans = bt.hits()


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")