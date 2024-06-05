import time
start = time.time()
ans = 0


def GeneratePartitionsInSquare(a, b):
    if a == 0 or b == 0:
        return []
    partitionList = [[] for _ in range(a*b+1)]
    partitionList[1].append([1])
    partitionList[0].append([])
    for i in range(2, a*b+1):
        for part in partitionList[i-1]:
            if part[0] < b and (len(part) == 1 or part[1] > part[0]):
                newPart = part[:]
                newPart[0] += 1
                partitionList[i] += [newPart[:]]
            if len(part) < a:
                newPart = part[:]
                newPart = [1] + newPart
                partitionList[i] += [newPart[:]]
    return partitionList


def NoCopies(lst):
    if lst == []:
        return []
    ans = [lst[0]]
    for i in range(1, len(lst)):
        if not(lst[i] == lst[i-1]):
            ans += [lst[i]]
    return ans


def Mark(listParts):
    ans = []
    for part in listParts:
        partWithNoCopies = NoCopies(part)
        for p in partWithNoCopies:
            ans += [[p, part]]
    return ans


def FromPartitionToString(part):
    ans = "{"
    for p in part:
        ans += str(p) + ", "
    return ans + "}"


squarePartitions = GeneratePartitionsInSquare(13, 4)
squarePartitionsWithPrev = [Mark(squarePartitionWithNumber) for squarePartitionWithNumber in squarePartitions]
print(squarePartitionsWithPrev[:4])
print([len(k) for k in squarePartitions])
print([len(k) for k in squarePartitionsWithPrev])
print(sum([len(k) for k in squarePartitionsWithPrev]))

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")