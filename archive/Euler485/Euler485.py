#Code written on the 15/02/2024
#Uses an interval union structure which envolves a binary search and a case analysis to see what to do in the union of intervals
#Runs in 204 seconds

import time
start = time.time()

def FindInIntervalUnion(number, intervalList):
    ubd = len(intervalList)
    lbd = -1
    while ubd > lbd + 1:
        mbd = (ubd + lbd)//2
        if intervalList[mbd][0] > number:
            ubd = mbd
        elif intervalList[mbd][1] < number:
            lbd = mbd
        else:
            return mbd, True
    return lbd, False


def AddInterval(collectionIntervals, newInterval):
    #this function alters the "collectionIntervals" variable
    #it returns the number of elements added to the new collection
    iFound0, found0 = FindInIntervalUnion(newInterval[0], collectionIntervals)
    iFound1, found1 = FindInIntervalUnion(newInterval[1], collectionIntervals)
    if iFound0 == iFound1:
        if found0:
            if found1:
                #in this case both endpoints are inside the same interval, nothing to do
                return collectionIntervals, 0
            else:
                #in this case the larger endpoint stradles a bit outside of the interval
                ans = newInterval[1] - collectionIntervals[iFound0][1]
                collectionIntervals[iFound0][1] = newInterval[1]
                return collectionIntervals, ans
        else:
            #then found1 should also be false, and we get a new interval to be added
            return collectionIntervals[:iFound0+1] + [[newInterval[0], newInterval[1]]] + collectionIntervals[iFound0+1:], newInterval[1] - newInterval[0] + 1
    else:
        #in this case found1 is on the interval above the one of found0
        #Because of size considerations, this has to be precisely the interval above and found1 has to be true
        if found0:
            #in this case the interval stradles the whole gap
            #we also know because of the size of intervals that the largest endpoint will be inside iFound1 interval
            ans = collectionIntervals[iFound1][0] - collectionIntervals[iFound0][1] - 1
            return collectionIntervals[:iFound0] + [[collectionIntervals[iFound0][0], collectionIntervals[iFound1][1]]] + collectionIntervals[iFound1+1:], ans
        else:
            #in this case the lower endpoint is not inside any interval. Note that this means iFound0 can be -1
            #Because of size, this means that the largest endpoint has to be inside iFound1 interval
            ans = collectionIntervals[iFound1][0] - newInterval[0]
            collectionIntervals[iFound1][0] = newInterval[0]
            return collectionIntervals, ans

LIM = 10**8
K = 10**5
ndivs = [1 for _ in range(LIM+1)]

for i in range(2, LIM+1):
    for j in range(i, LIM+1, i):
        ndivs[j] += 1

rast = [[ndivs[i], i] for i in range(1, LIM+1)]
rast.sort(reverse = True)

count = 0
ans = 0
index = 0
vis = []
while count < LIM-K+1:
    newMax = rast[index][1]
    newVal = rast[index][0]
    vis, newValHits = AddInterval(vis, [max(newMax-K+1, 1), min(newMax, LIM-K+1)])
    count += newValHits
    ans += newVal * newValHits
    index += 1
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")