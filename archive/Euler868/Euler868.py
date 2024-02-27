#Code written on the 22/02/2024
#The order can be computed recursively, as the largest element moves in a predictable pattern, whereas the rest moves along the rule as if the other element were not there
#Runs in 10ms


import time
start = time.time()
import string


def FindPosition(item, tuple):
    for index, i in enumerate(tuple):
        if item == i:
            return index

def IsIn(item, ls):
    for i in ls:
        if item == i:
            return True
    return False

def ToListNumbers(str):
    toIndex = [string.ascii_uppercase.index(c) for c in str]
    sortedIndex = toIndex[:]
    sortedIndex.sort()
    return [FindPosition(i, sortedIndex) for i in toIndex]


def PosNumList(lst):
    l = len(lst)
    if l == 1:
        return 0
    pos = FindPosition(l-1, lst)
    posStar = PosNumList(lst[:pos] + lst[pos+1:])
    if posStar%2 == 1:
        return l*posStar+pos
    return l*posStar+l-1-pos

def PosString(str):
    return  PosNumList(ToListNumbers(str))

#print("Answer = ", PosString("BELFRY"))
print("Answer = ", PosString("NOWPICKBELFRYMATHS"))
end = time.time()
print("Time elapsed ", end - start, " seconds")