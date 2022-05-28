import time
import math
from itertools import product

start_time = time.time()
    
w = ["AREA", "FARE", "FREE", "REEF"]

ch = ["A", "F", "R", "E"]
n=[0, 1]


def wor(key):
    return key[0] + key[1] + key[2] + key[3]


obj = {}
for c1, c2, c3, c4, d1, d2, d3, d4 in product(ch, ch, ch, ch, n, n, n, n):
    obj[(c1, c2, c3, c4, d1, d2, d3, d4)] = 0


DP = [obj.copy() for _ in range(32)]
#DP[n][key] = number of words of length n that end with key[0]key[1]key[2]key[3] and have key[4 + i] occurences of w[i] for i = 0, ..., 3



for key in obj:
    if not(wor(key) in w) and key[4] == key[5] == key[6] == key[7] == 0:
        DP[4][key] = 1

for index, word in enumerate(w):
    key = [ch for ch in word] + [0 for _ in range(4)]
    key[4+index] = 1
    DP[4][tuple(key)] = 1

LIM = 30

for n in range(5, LIM+1):
    for key in DP[n]:
        for char in ch:
            word = wor(key)
            if word == w[0]:
                if key[4] == 1:
                    DP[n][key] += DP[n-1][tuple([char, key[0], key[1], key[2], key[4]-1, key[5], key[6], key[7]])]
            elif word == w[1]:
                if key[5] == 1:
                    DP[n][key] += DP[n-1][tuple([char, key[0], key[1], key[2], key[4], key[5]-1, key[6], key[7]])]
            elif word == w[2]:
                if key[6] == 1:
                    DP[n][key] += DP[n-1][tuple([char, key[0], key[1], key[2], key[4], key[5], key[6]-1, key[7]])]
            elif word == w[3]:
                if key[7] == 1:
                    DP[n][key] += DP[n-1][tuple([char, key[0], key[1], key[2], key[4], key[5], key[6], key[7]-1])]
            else:
                DP[n][key] += DP[n-1][tuple([char, key[0], key[1], key[2]] + list(key[4:]))]

tot = 0
for key in DP[LIM]:
    if key[4] == key[5] == key[6] == key[7] == 1:
        #print(key, " - ", DP[LIM][key])
        tot += DP[LIM][key]


"""
for key in obj:
    if wor(key) == "AREA":
        print(key, " - ", DP[LIM][key])
"""

print("tot = ", tot)
print(" --- %s seconds --- "%(time.time() - start_time))
