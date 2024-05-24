def Partition_Generate(n):
    ans = [[[]]]
    l = 0
    while l < n:
        l += 1
        new_parts = []
        for k in range(l):
            for partition in ans[k]:
                new_part = partition + [l-k]
                new_part.sort()
                new_parts.append(new_part[:])
        new_parts.sort()
        ans += [[new_parts[0][:]]]
        for i in range(len(new_parts)-1):
            if not(new_parts[i] == new_parts[i+1]):
                ans[-1] += [new_parts[i+1][:]]

    return ans




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
