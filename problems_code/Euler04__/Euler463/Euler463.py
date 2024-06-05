#Code written on the
#
#It runs on 



import time
start = time.time()

def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]


def fromDigits(dgs, base):
    ans = 0
    l = len(dgs)
    pow = 1
    for i in range(l-1, -1, -1):
        ans += dgs[i]*pow
        pow *= base
    return ans


def f(n):
    dgs = digits(n, 2)
    dgs.reverse()
    return fromDigits(dgs, 2)


def power(a, n):
    if n == 0:
        return 1
    if n%2 == 1:
        return a * power(a*a, n//2)
    return power(a*a, n//2)


def intervalS(l, b, a):
    #a is a list of integers, which may not end in zero
    pb = power(2, b)
    if a == [1]:
        if b == 0:
            return 0
        #Just sum the first 2**b numbers
        return power(4, b-1) + intervalS(l, b-1, [1])
    A = a[:]
    A.reverse()
    A[0] = 0
    return power(2, b) * fromDigits(A, 2) + power(2, l) * pb * (pb - 1) // 2


def intervalEP(l, b, a):
    A = a + [0]*(l - len(a))
    A[-1] = 0
    lb = fromDigits(A + [0]*b, 2)
    ub = fromDigits(A + [1]*b, 2)
    if lb == 0:
        lb += 1
    return [lb, ub]


def intervalSNaive(l, b, a):
    A = a + [0]*(l - len(a))
    A[-1] = 0
    lb = fromDigits(A + [0]*b, 2)
    ub = fromDigits(A + [1]*b, 2)
    print(digits(lb, 2), digits(ub, 2))
    ans = 0
    for i in range(lb, ub+1):
        ans += f(i)
    return ans

def S(m):
    mDigs = digits(m, 2)
    ln = len(mDigs)
    ans = 0
    for l in range(1, ln+1):
        if mDigs[l-1] == 1:
            ans += intervalS(l, ln-l, mDigs[:l])
            #print(l, ln-l, mDigs[:l], intervalS(l, ln-l, mDigs[:l]), intervalSNaive(l, ln-l, mDigs[:l]), intervalEP(l, ln-l, mDigs[:l]))
    return ans + f(m)

LIM = 3**27
print(LIM)


print("Answer = ", S(LIM)%1000000000)
end = time.time()
print("Time elapsed ", end - start, " seconds")