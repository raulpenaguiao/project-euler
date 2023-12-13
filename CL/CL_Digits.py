def Digits(num, base = 10):
    if num < base:
        return [num]
    return Digits(num//base, base) + [num%base]


def ToInteger(lst, base=10):
    if lst == []:
        return 0
    return lst[-1] + base*ToInteger(lst[:-1], base)