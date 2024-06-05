import time
start = time.time()
ans = 0

dic = {(0, 0, 0, 0, 0, 0):True}

def Next(dic):
    newDic = {}
    for key in newDic:
        key1 = NextRight(key)
        key2 = NextLeft(key)
        newDic[key1] = True
        newDic[key2] = True
    return newDic

def NextRight(key):
    return key


def NextRight(key):
    return key


for i in range(N//2)


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")