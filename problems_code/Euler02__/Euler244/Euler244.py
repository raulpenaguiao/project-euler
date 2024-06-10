#Code written on the 2024/06/10
#Meet in the middle: for each path of length $k$ computes the end result if starting in both displays
#After doing all $k$ length paths, sees if any two reach the same configuration
#Does not end... we need to improve things

import time
start = time.time()
ans = 0


from queue import Queue


class Path:
    def __init__(self, endpoint = 0, permutation = [i for i in range(16)], path = ""):
        self.endpoint = endpoint
        self.permutation = permutation
        self.path = path


    def Advance(self, ch):
        if ch == "U":
            self.permutation[endpoint] = self.permutation[endpoint + 4]
            self.permutation[endpoint + 4] = 0
            self.endpoint += 4 
            self.path += "U"
        if ch == "D":
            self.permutation[endpoint] = self.permutation[endpoint - 4]
            self.permutation[endpoint - 4] = 0
            self.endpoint -= 4
            self.path += "D" 
        if ch == "L":
            self.permutation[endpoint] = self.permutation[endpoint + 1]
            self.permutation[endpoint + 1] = 0
            self.endpoint += 1
            self.path += "L" 
        if ch == "R":
            self.permutation[endpoint] = self.permutation[endpoint - 1]
            self.permutation[endpoint - 1] = 0
            self.endpoint -= 1
            self.path += "R"


    def HashFromHalf(self):
        hashVal = 0
        pow2 = 1
        for p in self.permutation:
            if p%4 > 1:
                hashVal += pow2
            pow2 *= 2
        return hashVal
    

    def HashFromCheckerboard(self):
        hashVal = 0
        pow2 = 1
        for p in self.permutation:
            if p%2 == 1:
                hashVal += pow2
            pow2 *= 2
        return hashVal


    def Copy(self):
        return Path(self.endpoint, self.permutation[:], self.path)
    

    def PermutationCompositionOfPaths(self, other):
        finalPerm = [i for i in range(16)]
        for i in range(16):
            finalPerm[other.permutation[i]] = self.permutation[i]
        return finalPerm


def CheckerboardPatternCheck(permutation):
    for i in range(1, 16, 2):
        if permutation[i]%4 > 1:
            return False
    return True


def ReversePath(string):
    revString = ""
    for ch in string[::-1]:
        if ch == "U":
            revString += "D"
        if ch == "D":
            revString += "U"
        if ch == "L": 
            revString += "R"
        if ch == "R":
            revString += "L"
    return revString


def ChecksumOfPath(string):
    checksum = 0
    for ch in string:
        if ch == "U":
            checksum *= 243
            checksum += 85
            checksum %= 100_000_007
        if ch == "D":
            checksum *= 243
            checksum += 68
            checksum %= 100_000_007
        if ch == "L":
            checksum *= 243
            checksum += 76
            checksum %= 100_000_007
        if ch == "R":
            checksum *= 243
            checksum += 82
            checksum %= 100_000_007
    return checksum


def AddToDic(dic, key, val = 1):
    #print(dic, key, val)
    if key in dic:
        dic[key] += val
    else:
        dic[key] = val

newQ = Queue()
newQ.put(Path())
flagFoundPath = False
steps = 1
while not flagFoundPath:
    #Create new queue
    q = newQ
    newQ = Queue()
    hashHalf = {}
    hashCheckerboard = {}
    while not q.empty():
        path = q.get()
        endpoint = path.endpoint
        if endpoint > 3:
            nPath = path.Copy()
            nPath.Advance("D")
            newQ.put(nPath)
            AddToDic(hashCheckerboard, nPath.HashFromCheckerboard(), [nPath])
            AddToDic(hashHalf, nPath.HashFromHalf(), [nPath])
        if endpoint < 12:
            nPath = path.Copy()
            nPath.Advance("U")
            newQ.put(nPath)
            AddToDic(hashCheckerboard, nPath.HashFromCheckerboard(), [nPath])
            AddToDic(hashHalf, nPath.HashFromHalf(), [nPath])
        if endpoint%4 > 0:
            nPath = path.Copy()
            nPath.Advance("R")
            newQ.put(nPath)
            AddToDic(hashCheckerboard, nPath.HashFromCheckerboard(), [nPath])
            AddToDic(hashHalf, nPath.HashFromHalf(), [nPath])
        if endpoint%4 < 3:
            nPath = path.Copy()
            nPath.Advance("L")
            newQ.put(nPath)
            AddToDic(hashCheckerboard, nPath.HashFromCheckerboard(), [nPath])
            AddToDic(hashHalf, nPath.HashFromHalf(), [nPath])
    steps += 1
    print("We made ", steps, " steps and we have ", sum([len(hashCheckerboard[i]) for i in hashCheckerboard]), " different paths")
    end = time.time()
    print("Time elapsed ", end - start, " seconds")
    
    #Check if any two paths concatenate to the desired path in the old queue
    for keyHalf in hashHalf:
        if keyHalf in hashCheckerboard:
            for p1 in hashHalf[keyHalf]:
                for p2 in hashCheckerboard[keyHalf]:
                    if p1.endpoint == p2.endpoint and CheckerboardPatternCheck(p1.PermutationCompositionOfPaths(p2)):
                        flagFoundPath = True
                        print(p1.path + ReversePath(p2.path))
                        ans += ChecksumOfPath(p1 + ReversePath(p2))



path = Path()
path.Advance("L")
path.Advance("L")
path.Advance("L")
path.Advance("U")
path.Advance("R")
path.Advance("R")
path.Advance("R")
path.Advance("D")
print(path.HashFromCheckerboard())

print("Answer = ", ans)

end = time.time()
print("Time elapsed ", end - start, " seconds")