import time
start = time.time()
ans = 0

def Digits(n, base = 2):
    """returns list with digits in base"""
    if n > base:
        return Digits(n//base) + [n%base]
    return [n%base]

def FromDigits(digs, base = 2):
    """returns int value of digit list in base"""
    ans = 0
    for d in digs:
        ans *= base
        ans += d
    return ans

def f(n, k):
    """returns the sum of all the nodes between n and k in T_n"""
    fi = n - k
    ans = n - fi
    while(fi > 0):
        digs = Digits(fi)
        i = 1
        while(i < len(digs) and digs[i] < 1):
            i+= 1
        sliceLastOne = digs[i:]
        fi = FromDigits(sliceLastOne)
        ans += n - fi
    return ans


print("Answer = ", f(10**17, 9**17))
end = time.time()
print("Time elapsed ", end - start, " seconds")