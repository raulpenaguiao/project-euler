import time
start = time.time()
ans = 0

from queue import PriorityQueue, Queue

class BinTree:
    def __init__(self, node, parent, score):
        self.parent = parent
        self.node = node
        self.isLeaf = True
        self.hasLeft = False
        self.hasRight = False
        self.priority = score

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __repr__(self):
        if self.node == "":
            return ""
        return self.parent.__repr__() + self.node

leaves = PriorityQueue()
bt = BinTree("", None, 0)
bt1 = BinTree("0", bt, 1)
bt0 = BinTree("1", bt, 4)
leaves.put(bt0)
leaves.put(bt1)

nOnes = 1
N = 6

while( True ):
    leaf = leaves.get()
    leaf.parent.isLeaf = False
    if leaf.node == "1":
        leaf.parent.hasLeft = True
        leaf.parent.left = leaf
        nOnes += 1
        if nOnes == N:
            break
    if leaf.node == "0":
        leaf.parent.hasRight = True
        leaf.parent.right = leaf

    bt0 = BinTree("0", leaf, leaf.priority+1)
    bt1 = BinTree("1", leaf, leaf.priority+4)
    leaves.put(bt0)
    leaves.put(bt1)


# Search for all leaves in the tree, save them on a list and then backtrack

leavesList = []
pendingNodes = Queue()
pendingNodes.put(bt)
while (not pendingNodes.empty()):
    node = pendingNodes.get()
    if node.isLeaf:
        leavesList.append(node)
    else:
        if node.hasRight:
            pendingNodes.put(node.right)
        if node.hasLeft:
            pendingNodes.put(node.left)

print([k.__repr__() for k in leavesList])




print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")