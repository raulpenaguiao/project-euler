#Code written on the 12/12/2023
#Computes the transition matrix between the boards after 50 jumps
#Afterwards, sums the probability that no bug will end up in this square d
#This latter probability is 1 - p_{e, d}
#Possible optimization cuts time in half: the markov chain is bipartite, explore only the 2-step markov chain
#Runs in 592 seconds


import time
start = time.time()
from decimal import *
getcontext().prec = 40


def Multiply(A, B, L):
    return [[sum([A[i][k]*B[k][j] for k in range(L)]) for j in range(L)] for i in range(L)]

#print("Multiplication = ", Multiply([[1, 2], [3, 4]], [[1, 5], [2, -1]], 2))#[[5, 3], [11, 11]]



def PowerMatrix(B, n, L):
    A = B[:]
    ans = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(L):
        ans[i][i] = 1
    m = n
    while m > 0:
        print(m)
        if m%2 == 1:
            ans = Multiply(ans, A, L)
        A = Multiply(A, A, L)
        m //= 2
    return ans

#print("Power matrix ", PowerMatrix([[1, 2], [3, 4]], 5, 2))#[[1069, 1558], [2337, 3406]]


def ListNeigbors(tile, L):
    ans = []
    if tile[0] > 0:
        ans.append((tile[0]-1, tile[1]))
    if tile[1] > 0:
        ans.append((tile[0], tile[1]-1))
    if tile[0] < L - 1:
        ans.append((tile[0]+1, tile[1]))
    if tile[1] < L - 1:
        ans.append((tile[0], tile[1]+1))
    return ans

board = []
L = 30
for i in range(L):
    for j in range(L):
        board.append((i, j))
l = len(board)
print("length = ", l)
#print("board = ", board)
transMatrix = [[0 for _ in board] for _ in board]
for d in range(l):
    lstNeighbors = ListNeigbors(board[d], L)
    #print(board[d], " neigbors ", lstNeighbors)
    for tile in lstNeighbors:
        i = board.index(tile)
        transMatrix[i][d] = 1/len(lstNeighbors)
powMatrix = PowerMatrix(transMatrix, 50, l)

ans = 0
for d in range(l):
    pieceEmpty = 1
    for e in range(l):
        pieceEmpty *= 1 - powMatrix[d][e]
    ans += pieceEmpty
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")