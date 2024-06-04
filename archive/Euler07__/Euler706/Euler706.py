#Code on 25/10/2023
#Dinamical programing on the number of sequences with a given number (mod 3) of subsequences with a specified sum (mod 3) and sufixes
#Runs in 76.1 seconds

import time
import math
start = time.time()

#In this problem we are only interested in strings that come from positive integers.

MOD = 1_000_000_007
F = [[[[[[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(2)]
#F[N%2][a][b][c][i][j][k] represent the number strings of length N modulo MOD such that
#   the number mod 3 of non-empty substrings == 0 mod 3 is a
#   the number mod 3 of non-empty substrings == 1 mod 3 is b
#   the number mod 3 of non-empty substrings == 2 mod 3 is c
#   the number mod 3 of non-empty sufixes == 0 mod 3 is i
#   the number mod 3 of non-empty sufixes == 1 mod 3 is j
#   the number mod 3 of non-empty sufixes == 2 mod 3 is k

#Recall that 0 is not a string of length 1 because it does not come from a positive integer
F[1][1][0][0][1][0][0] = 3 #3, 6, 9
F[1][0][1][0][0][1][0] = 3 #1, 4, 7
F[1][0][0][1][0][0][1] = 3 #2, 5, 8

#Note that f(n) = sum_{b, c, i, j, k} F[N%2][0][b][c][i][j][k]

n = 1 # 6, as all 1, 2, 4, 5, 7, 8 are 3-like
n = 2 # 30
n = 3 # 342
n = 6 # 290898
n = 100 # 131387729
n = 1000 # 696096950
n = 10000 # 756813992
n = 100000 # 
"""
#Naive method
def digs(n, base = 10):
    if n < base:
        return [n]
    return digs(n//base) + [n%base]


def sssums_list(t):
    if(len(t) == 1):
        return [t[0]]
    sslist = [sum(t[i:]) for i in range(len(t))]
    return sslist + sssums_list(t[:-1])

def is3like(n, verbose = False):
    d = digs(n)
    if(verbose): print(d)
    totsum = 0
    if(verbose): print(sssums_list(d))
    for sssums in sssums_list(d):
        if sssums%3 == 0:
            totsum += 1
    if(verbose): print("totsum = ", totsum)
    return totsum%3 == 0

is3like(243, True)
print(is3like(10, True))
print(is3like(11, True))

pow10 = 10**n
num_3like = 0
for i in range(pow10//10, pow10):
    if(is3like(i)):
        print(i)
        num_3like += 1
print("Number of 3like numbers = ", num_3like)
"""
L = [4, 3, 3]

#We assume n >= 1
totalNumberOf3Like = 6
#print("N = ", 1, " and number of 3 like numbers = ", totalNumberOf3Like)

for N in range(2, n+1):
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            F[N%2][a][b][c][i][j][k]  = L[0] * F[(N+1)%2][(a - i + 3)%3][(b - j + 3)%3][(c - k + 3)%3][(i - 1 + 3)%3][(j)%3][(k)%3]
                            F[N%2][a][b][c][i][j][k] += L[1] * F[(N+1)%2][(a - i + 3)%3][(b - j + 3)%3][(c - j + 3)%3][(j - 1 + 3)%3][(k)%3][(i)%3]
                            F[N%2][a][b][c][i][j][k] += L[2] * F[(N+1)%2][(a - i + 3)%3][(b - j + 3)%3][(c - i + 3)%3][(k - 1 + 3)%3][(i)%3][(j)%3]
                            F[N%2][a][b][c][i][j][k] %= MOD
                            """
    #Add the 3-like numbers of this size
    totalNumberOf3Like = 0
    for b in range(3):
        for c in range(3):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        totalNumberOf3Like += F[N%2][0][b][c][i][j][k]
                        totalNumberOf3Like %= MOD
    print("N = ", N, " and number of 3 like numbers = ", totalNumberOf3Like)"""


totalNumberOf3Like = 0
for b in range(3):
    for c in range(3):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    totalNumberOf3Like += F[N%2][0][b][c][i][j][k]
                    totalNumberOf3Like %= MOD

print("Answer = ", totalNumberOf3Like)
end = time.time()
print("Time elapsed ", end - start, " seconds")