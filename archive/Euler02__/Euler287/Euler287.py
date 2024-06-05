#Code written on the 14/12/2023
#This just emulates the split for each quadrant
#People seem to find is faster to run a C program than a python on the forums.
#Runs in 331 seconds


import time
start = time.time()
import queue
L = 24
radius = 2**(L-1)


class Square:
    def __init__(self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    def Split(self):
        mh = (self.left + self.right)//2
        mv = (self.down + self.up)//2
        s1 = Square(self.left, mh, mv, self.down)
        s2 = Square(mh+1, self.right, mv, self.down)
        s3 = Square(self.left, mh, self.up, mv+1)
        s4 = Square(mh+1, self.right, self.up, mv+1)
        return [s1, s2, s3, s4]
    
    def IsSplit(self):
        if self.left**2 + self.down**2 <= radius**2:
            if self.right**2 + self.up**2 > radius**2:
                return True
        return False

def CountMinimalString(SQ):
    ans = 0
    sqs = queue.Queue()
    sqs.put(SQ)
    while not sqs.empty():
        s = sqs.get()
        if s.IsSplit():
            ans += 1
            for s1 in s.Split():
                sqs.put(s1)
        else:
            ans += 2
    return ans

tot = 1
tot += CountMinimalString(Square(0, 2**(L-1)-1, 2**(L-1)-1, 0))
tot += 2*CountMinimalString(Square(0, 2**(L-1)-1, 2**(L-1), 1))
tot += CountMinimalString(Square(1, 2**(L-1), 2**(L-1), 1))

print("Answer = ", tot)
end = time.time()
print("Time elapsed ", end - start, " seconds")