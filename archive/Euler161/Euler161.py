#Code writtein on 2023/12/01
#In each partially filled board, we identify the uppermost tile to the left that is free, and try to put any tile possible there
#We use memoisation to make sure we dont evaluate a partially filled board twice
#Runs in 593 seconds

import time
start = time.time()

from queue import PriorityQueue


class Table:
    def __init__(self, *args, **kwargs):
        if kwargs["type"] == "EMPTY":
            self.N = kwargs["N"]
            self.M = kwargs["M"]
            self.board = [[False for _ in range(kwargs["M"])] for _ in range(kwargs["N"])]
            self.lastPosition = [0, 0]
            self.isFull = False
        elif kwargs["type"] == "FROMTUPLE":
            self.N = len(kwargs["board"])
            self.M = len(kwargs["board"][0])
            self.board = [[kwargs["board"][i][j] for j in range(self.M)] for i in range(self.N)]
            self.lastPosition = [kwargs["pos"][0], kwargs["pos"][1]]
            self.isFull = kwargs["isFull"]
        
    def __repr__(self):
        return str(self.toTuple())
    

    def toTuple(self):
        return tuple([tuple([tuple(self.board[i]) for i in range(self.N)]), tuple([self.lastPosition[0], self.lastPosition[1]])])


    def __lt__(self, other):
        if self.lastPosition[1] == other.lastPosition[1]:
            return self.lastPosition[0] < other.lastPosition[0]
        return self.lastPosition[1] < other.lastPosition[1]


    def UpdateLastPosition(self):
        #print("Updating = ", self)
        while self.board[self.lastPosition[1]][self.lastPosition[0]]:
            #print(self.lastPosition)
            self.lastPosition[0] += 1
            if self.lastPosition[0] == self.M:
                self.lastPosition[0] = 0
                self.lastPosition[1] += 1
                if self.lastPosition[1] == self.N:
                    #There is no last position as the board is filled
                    self.isFull = True
                    self.lastPosition = [0, self.N]
                    return


    def Place(self, tile):
        for p in tile:
            pos = [p[0] + self.lastPosition[0], p[1] + self.lastPosition[1]]
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= self.M or pos[1] >= self.N or self.board[pos[1]][pos[0]]:
                raise Exception("Cannot place tile in this board")
            self.board[pos[1]][pos[0]] = True
        self.UpdateLastPosition()

    def CreatePlace(self, tile):
        ans = Table(type = "FROMTUPLE", board = self.toTuple()[0], pos = self.lastPosition, isFull = self.isFull)
        ans.Place(tile)
        return ans


M = 12
N = 9
tiles = [[[0 ,0], [1, 0], [0, 1]], [[0 ,0], [1, 0], [1, 1]], [[0 ,0], [0, 1], [1, 1]], [[0 ,0], [1, 0], [2, 0]], [[0, 0], [0, 1], [0, 2]], [[0, 0], [-1, 1], [0, 1]]]
tilings = {}

et = Table(type = "EMPTY", M = M, N = N)
tilings[et.toTuple()] = 1
q = PriorityQueue()
q.put(et)
vis = {et: True}
while not q.empty():
    table = q.get()
    for tile in tiles:
        try:
            newboard = table.CreatePlace(tile)
            if (not newboard.isFull) and (not newboard.toTuple() in vis):
                q.put(newboard)
                vis[newboard.toTuple()] = True
            tpl = newboard.toTuple()
            if tpl in tilings:
                tilings[tpl] += tilings[table.toTuple()]
            else:
                tilings[tpl] = tilings[table.toTuple()]
        except Exception as e :
            pass
        
max = 0
for k in tilings:
    if tilings[k] > max:
        max = tilings[k]

print("Answer = ", max)
end = time.time()
print("Time elapsed ", end - start, " seconds")








"""
def Add(table, tile):
    #Check
    print(table, " // ", tile)
    board = table[0][:]
    pivot = table[1][:]
    for pos in tile:
        x = pos[0] + pivot[0]
        y = pos[1] + pivot[1]
        if 0 <= x and x < M and y >= 0 and y < N and not board[y][x]:
            board[y][x] = True
        else:
            print("x = ", x, "y = ",  y, 0 <= x, x < M, " y >= 0 - ",  y >= 0, y < N, M, N )
            return "NOFIT"
    while not board[pivot[1]][pivot[0]]:
        pivot[0] += 1
        if pivot[0] == M:
            pivot[0] = 0
            pivot[1] += 1
            if pivot[1] == N:
                return ""
    return [board, pivot]
    
    """