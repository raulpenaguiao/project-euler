#Code written in 2023/12/05
#Fixed an arbitrary limit and computed all the sums of squares and cubes up to this limit
#Memorised these sums in dictionaries to count occurrences
#Lim = 10**9 magically words
#Code runs in 27.26 seconds

import time
start = time.time()
import math
ans = 0

def AddOne(dic, val):
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1

def digits(a, base = 10):
    if a < base:
        return [a]
    return digits(a//base, base)+ [a%base]

def isPalindrome(a):
    d = digits(a)
    return d == d[::-1]


sumCounter = {}

LIM = 10**9
LIMC = math.ceil(math.pow(LIM, 1/3))
LIMS = math.ceil(math.pow(LIM, 1/2))
for i in range(LIMC):
    for j in range(LIMS):
        a = i**3+j**2
        if isPalindrome(a):
            AddOne(sumCounter, a)
answers = []
for k in sumCounter:
    if sumCounter[k] == 4 and k < LIM:
        answers.append(k)
answers.sort()

if len(answers) > 4:
    print("Answer = ", sum(answers[:5]))
else:
    print("Not enough answers, ", answers)
end = time.time()
print("Time elapsed ", end - start, " seconds")