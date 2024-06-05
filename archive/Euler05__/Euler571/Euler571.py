# Code written on the 2024/05/30
# We assume that the first 10 such numbers have exactly 12 digits base 12
# This is the munumal amount of digits such a number may have
# We iterate over all permutations of the 12 distinct digits base 12
# The iteration preserves the order of the underlying numbers
# For each permutation, convert to all bases < 12 and check if the condition is satisfied.
# Runs in 4715 seconds (1.5h)

import time
start = time.time()
ans = 0


def digits(n, base = 10):
    if n < base:
        return [n]
    return digits(n//base, base) + [n%base]


def fromDigits(lst, base = 10):
    if lst == []:
        return 0
    return fromDigits(lst[:-1], base)*base + lst[-1]


def CheckPanDigital(lst, b):
    lst.sort()
    index = 0
    if lst[0] > index or lst[-1] < b-1:
        return False
    l = len(lst)
    for i in range(1, l):
        if lst[i]> lst[i-1]+1:
            return False
    return True


def Next(lst):
    l = len(lst)
    for i in range(l-1, 0, -1):
        if lst[i] > lst[i-1]:
            a = lst[i-1]
            lst[i-1:] = sorted(lst[i-1:])
            #find element after a
            for j in range(i-1, l-1):
                if lst[j] == a:
                    b = lst[i-1]
                    lst[i-1] = lst[j+1]
                    lst[j+1] = b
                    lst[i:] = sorted(lst[i:])
                    return
    return "Last"


def findSuperPanDigital(maxBase, N):
    count = 0
    sum = 0
    permsProcessed = 0
    currPal = [1, 0] + [i for i in range(2, maxBase)]
    while(count < N):
        n = fromDigits(currPal, maxBase)
        #if permsProcessed%93_144 == 142:
        #    print("We are at ", n, " with ", permsProcessed, " permutations processed and ", count, " pandigital permutations found.")
        flag = True
        for b in range(maxBase-1, 1, -1):#Reverse order performs fewer checks
            dgs = digits(n, b)
            if not CheckPanDigital(dgs, b):
                flag = False
                break
        if flag:
            count += 1
            sum += n
            #print(n)#, [digits(n, b) for b in range(2, maxBase+1)])
        #Iterate to the next digit
        errorFlag = Next(currPal)
        if errorFlag == "Last":
            print("Not enough palindromes")
            break
        permsProcessed += 1
    return sum



print("Answer = ", findSuperPanDigital(12, 10))
end = time.time()
print("Time elapsed ", end - start, " seconds")