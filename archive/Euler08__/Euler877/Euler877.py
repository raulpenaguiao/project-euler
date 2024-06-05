import time
start = time.time()
ans = 0

def Digits(num, base=2):
    if num < base:
        return [num]
    return Digits(num//base, base) + [num%base]


def FromDigits(digs, base = 2):
    pow = 1
    ans = 0
    for i in range(len(digs), -1, -1):
        ans += pow*digs[i]
        pow *= base
    return ans

def XORsum(a, b):
    """Returns the XOR sum

    Args:
        a (int): 
        b (int): 

    Returns:
        int
    """
    if a == 0:
        return b
    return 2*XORsum(a//2, b//2) + (a + b)%2


def XORproduct(a, b):
    """Returns the XOR product

    Args:
        a (int): 
        b (int): 

    Returns:
        int
    """
    if a == 0:
        return 0
    if a > b:
        return XORproduct(b, a)
    if a%2 == 0:
        return 2*XORproduct(a//2, b)
    else:
        return XORsum(b, 2*XORproduct(a//2, b))

def testS(a, b):
    print("XORsum(", a, ", ", b, ") = ", XORsum(a, b))


def testP(a, b):
    print("XORproduct(", a, ", ", b, ") = ", XORproduct(a, b))

"""
testS(1, 1)
testS(3, 1)
testS(7, 13)
testP(1, 1)
testP(3, 1)
testP(13, 7)
testP(5, 5)
"""

def Value(a, b):
    """Returns the result of the equation a^2 + xab + b^2

    Args:
        a (int): 
        b (int): 

    Returns:
        list: matches lst if sz < len(lst)
    """
    b2 = XORproduct(b, b)
    bx = 2*b
    a2 = XORproduct(a, a)
    return XORsum(XORsum(a2, XORproduct(bx, a)), b2)

def testV(a, b):
    print("Value(", a, ", ", b, ") = ", Value(a, b))

"""
testV(1, 1)
testV(3, 6)
testV(13, 7)"""

def PadWithZeroes(lst, sz):
    """Returns an enlarged list from a given list with zeroes on the left

    Args:
        lst (list): a python list
        sz (int): a desired size for the output list

    Returns:
        list: matches lst if sz < len(lst)
    """
    if sz > len(lst):
        return [0]*(sz-len(lst)) + lst
    return lst

"""Test run to see some solutions, runs in 300 seconds
N = 10000
for b in range(N):
    b2 = XORproduct(b, b)
    bx = 2*b
    for a in range(b+1):
        a2 = XORproduct(a, a)
        val = XORsum(XORsum(a2, XORproduct(bx, a)), b2)
        if val == 5:
            #print("(a, b) solution is (", a, " , ", b, ")")
            #print(Digits(a))
            print(b)
            #print(PadWithZeroes(Digits(b), 25))
            tot = XORsum(tot, b)
"""

N = 10**18
ans = [0, 3]
tot = 3
while(True):
    an = XORsum(2*ans[-1], ans[-2])
    if(an > N):
        break
    tot = XORsum(tot, an)
    ans+=[an]




print("Answer = ", tot)
end = time.time()
print("Time elapsed ", end - start, " seconds")