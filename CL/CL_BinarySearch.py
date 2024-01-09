def BinarySearch(lst, l, val, verbose = False):
    #Returns the largest index of lst s.t. lst[i] <= val
    #If no such index exists, return -1
    #Assumes list lst is sorted
    imin = -1
    imax = l
    if verbose:
        print(lst, l, val)
        print("Interval: ", imin, imax)
    while(imax-imin > 1):
        im = (imax + imin)//2
        if verbose:
            print("New index ", im, " with value ", lst[im])
        if lst[im] > val:
            imax = im
        else:
            imin = im
        if verbose:
            print("New interval: ", imin, imax)
    if verbose:
        print("Index = ", imin)
    return imin


def BinaryFind(lst, l, val, verbose = False):
    ind = BinarySearch(lst, l, val, verbose)
    return ind >= 0 and ind < l and lst[ind] == val


if not BinarySearch([i for i in range(10)], 10, 4.5) == 4:
    BinarySearch([i for i in range(10)], 10, 4.5, True)
    print("Unit test failed")
if not BinarySearch([i for i in range(12)], 12, 13) == 11:
    BinarySearch([i for i in range(12)], 12, 13, True)
    print("Unit test failed")
if not BinarySearch([i for i in range(10)], 10, -3) == -1:
    BinarySearch([i for i in range(10)], 10, -3, True)
    print("Unit test failed")


#Random unit tests
import random
from math import floor
for _ in range(100):
    ln = floor(random.random()*10)
    l = [random.random() for _ in range(ln)]
    l.sort()
    trg = random.random()
    if not BinarySearch(l, ln, trg) == len([k for k in l if k <= trg])-1:
        BinarySearch(l, ln, trg, True)