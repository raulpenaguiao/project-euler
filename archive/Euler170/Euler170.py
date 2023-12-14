#Code written in 2023/12/07
#Generates and orders permutations
#For each permutation, breaks up into pieces and computes the gcd
#For each divisor, tests if this can be the first integer
#Runs in 31.29 seconds until finding a solution, 10s of which is generating all permutations

import time
start = time.time()
import CL_Primes as CP
import CL_Arithmetics as CA
ans = 0

prms = CP.Primes(10**6)

def GeneratePermutations(lst):
    if lst == []:
        return [[]]
    ans = []
    for i in lst:
        for p in GeneratePermutations([k for k in lst if not k == i]):
            ans.append([i]+p)
    return ans

def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base)+[n%base]


def GenerateCompositions(n):
    if n == 1:
        return [tuple([1])]
    ans = []
    for a in GenerateCompositions(n-1):
        l = list(a)
        ans.append(tuple([1]+l))
        l[0] += 1
        ans.append(tuple(l))
    return ans

def ToInteger(lst):
    if lst == []:
        return 0
    return int("".join([str(a) for a in lst]))


comps = GenerateCompositions(10)
DIGITS = [i for i in range(10)]



def ListNumbers(lst, comp):
    nms = []
    index = 0
    for a in comp:
        if lst[index] == 0:#This ensures that we do not have any leading zeroes
            return ""
        nms.append(lst[index:index+a])
        index += a
    return nms


#print(ListNumbers([2, 5, 4, 3, 6, 4], tuple([2, 4])))#[25, 4364]
#print(ListNumbers([2, 5, 4, 3, 6, 4], tuple([2, 2, 2])))#[25, 43, 64]
#print(ListNumbers([2, 5, 0, 4, 3, 2], tuple([2, 4])))# ""


def Match(lst):
    if not len(lst) == 10:
        return False
    lst.sort()
    for i in range(10):
        if not i == lst[i]:
            return False
    return True


def listGCD(lst):
    if len(lst) < 2:
        return lst[0]
    return listGCD([CA.gcd(lst[0], lst[1])]+lst[2:])

def isConcatenationOfProduct(lst):
    for comp in comps:
        if len(comp) < 2:
            continue
        nms = ListNumbers(lst, comp)
        if nms == "":
            continue
        dvs = CP.Divisors(listGCD([ToInteger(n) for n in nms]), prms)
        #print(lst, " :: ", comp, " ::: ", nms, " ::-:: ", dvs)
        for d in dvs:
            dgs = digits(d)
            for n in nms:
                nm = ToInteger(n)
                dgs += digits(nm//d)
            #print(dgs)
            if Match(dgs):
                print( [lst, comp])
                return True
    return False


def isConcatenatedProduct(lst):
    for comp in comps:
        if len(comp) < 3:
            continue
        nms = []
        index = 0
        flag = False
        for a in comp:
            if lst[index] == 0:#This ensures that we do not have any leading zeroes
                flag = True
                break
            nms.append(lst[index:index+a])
            index += a
        if flag:
            continue
        ndigs = []
        #print(nms, comp, len(comp))
        frst = ToInteger(nms[0])
        for i in range(len(comp)-1):
            ndigs += digits(frst*ToInteger(nms[i+1]))
        #print("number = ", lst, " and comp = ", comp, " and ndigs = ", ndigs)
        ndigs.sort()
        if len(ndigs) == 10:
            flag = True
            for i in range(10):
                if not ndigs[i] == i:
                    flag = False
            if flag:
                print(comp, nms, ndigs)
                return True
    return False

ints = [p for p in GeneratePermutations([i for i in range(10)]) if p[0] > 0]
print("Permutations generated")
ints.sort()
ints = ints[::-1]

for n in ints:
    print(n)
    if isConcatenationOfProduct(n):
        print("Answer = ", "".join([str(i) for i in n]))
        break
end = time.time()
print("Time elapsed ", end - start, " seconds")