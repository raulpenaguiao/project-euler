def PowerMod(a, d, p):
    if d == 0:
        return 1
    if d == 1:
        return a%p
    ans = PowerMod((a*a)%p, d//2, p)
    if d % 2 == 1:
        ans *= a
        ans %= p
    return ans



def lcm(a, b):
    return a*b//gcd(a, b)


def gcd(a, b):
    if a < 0:
        return gcd(b, -a)
    if b == 0:
        return a
    return gcd(b, a%b)



def ExtendedGCD(a, b):
    x = [1, 0]
    y = [0, 1]
    s = [a, b]
    while not(s[-1] == 0):
        q = s[-2]//s[-1]
        x.append(x[-2]-x[-1]*q)
        y.append(y[-2]-y[-1]*q)
        s.append(s[-2]-s[-1]*q)
    return [s[-2], x[-2], y[-2]]



def InverseMod(a, m):
    s, x, y = ExtendedGCD(a, m)
    if not s == 1:
        raise Exception("Numbers must be coprime")
    return (x%m + m)%m


def ChineseRemainder(lst):
    if len(lst) < 2:
        return lst[0][0]%lst[0][1]
    a1 = lst[0][0]
    a2 = lst[1][0]
    m1 = lst[0][1]
    m2 = lst[1][1]
    x = a1 * m2 * InverseMod(m2, m1) + a2 * m1 * InverseMod(m1, m2)
    m = m1*m2
    return ChineseRemainder([[x%m, m]]+ lst[2:])