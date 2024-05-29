# Code written on the 2024/05/29
# Builds the binary tree of binary strings with a priority queue according to skew cost
# A prefix-free code is the set of leaves, so one with $N$ elements is found when our tree has $N$ leaves. 
# The optimal such code contains the set of leaves thusly found, can be found by simple backtracking.
# Runs in 20_000 seconds


import time
start = time.time()
ans = 0

from queue import PriorityQueue, Queue

class BinTree:
    def __init__(self, node, parent, score, len):
        self.parent = parent
        self.node = node
        self.isLeaf = True
        self.hasLeft = False
        self.hasRight = False
        self.priority = score
        self.len = len

    def __lt__(self, other):
        return self.priority < other.priority or (self.priority == other.priority and self.len < other.len)

    def __gt__(self, other):
        return self.priority > other.priority or (self.priority == other.priority and self.len > other.len)

    def __le__(self, other):
        return self.priority < other.priority or (self.priority == other.priority and self.len <= other.len)

    def __ge__(self, other):
        return self.priority > other.priority or (self.priority == other.priority and self.len >= other.len)

    def __eq__(self, other):
        return self.priority == other.priority and self.len == other.len

    def __repr__(self):
        if self.node == "":
            return ""
        return self.parent.__repr__() + self.node

leaves = PriorityQueue()
bt = BinTree("", None, 0, 0)
bt1 = BinTree("0", bt, 1, 1)
bt0 = BinTree("1", bt, 4, 1)
leaves.put(bt0)
leaves.put(bt1)

nOnes = 1
nNodesVisited = 1
nNodesCreated = 3
N = 10**8

while( True ):
    leaf = leaves.get()
    nNodesVisited += 1
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

    bt0 = BinTree("0", leaf, leaf.priority+1, leaf.len + 1)
    bt1 = BinTree("1", leaf, leaf.priority+4, leaf.len + 1)
    nNodesCreated += 2
    leaves.put(bt0)
    leaves.put(bt1)
print("Tree constructed with ", nNodesCreated,  " nodes created and ", nNodesVisited, " nodes visited")
end = time.time()
print("Time elapsed ", end - start, " seconds")


nNodesBacktracked = 0
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
print("Leaves found")
end = time.time()
print("Time elapsed ", end - start, " seconds")

nNodesBacktracked = 0
for leaf in leavesList:
    while not leaf.parent.hasLeft:
        nNodesBacktracked += 1
        leaf = leaf.parent
    ans += leaf.priority

print("N = ", N)
print("Answer = ", ans,  " || ", nNodesBacktracked, " nodes backtracked.")
end = time.time()
print("Time elapsed ", end - start, " seconds")