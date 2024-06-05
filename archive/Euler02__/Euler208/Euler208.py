#Code written on the 2024/06/05
# Meet-in-the-middle: 
# Generate all all paths of size 70/2, making sure to save only the last position and direction
# This is saved on a dictionary. Paths are saved by counting how many times the robot walked a specific step.
# Each step is one of five possible steps corresponding to $5$-th roots of unity
# Directions are saved as a number between $0$ and $4$
# Two paths concatenate to a path back to the origin if they satisfy a shift condition
# A closed loop has to contain exactly the same number of steps in each direction, so this cutoff is used to disregard paths.
#Runs in 114ms



import time
start = time.time()
ans = 0
N = 70
#N = 25#70932
#N = 5#2

dic1 = {(0, 0, 0, 0, 0, 0):1}


def AddToDic(dic, key, val):
    if key in dic:
        dic[key] += val
    else:
        dic[key] = val


def Next(dic):
    newDic = {}
    for key in dic:
        if max(key[:-1]) > N//5:
            continue
        key1 = NextRight(key)
        key2 = NextLeft(key)
        AddToDic(newDic, key1, dic[key])
        AddToDic(newDic, key2, dic[key])
    return newDic

def NextRight(key):
    ans = list(key)
    ans[-1] -= 1
    ans[-1] %= 5
    ans[ans[-1]] += 1
    return tuple(ans)


def NextLeft(key):
    ans = list(key)
    ans[ans[-1]] += 1
    ans[-1] += 1
    ans[-1] %= 5
    return tuple(ans)

for i in range(N//2):
    dic1 = Next(dic1)

if N%2 == 0:
    dic2 = dic1
else:
    dic2 = Next(dic1)


for key in dic1:
    compKey = [N//5 - key[(key[5] + i)%5] for i in range(5)] + [(- key[5])%5]
    compKey = tuple(compKey)
    if compKey in dic2:
        ans += dic2[compKey]*dic1[key]


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")