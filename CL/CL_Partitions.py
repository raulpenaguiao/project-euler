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