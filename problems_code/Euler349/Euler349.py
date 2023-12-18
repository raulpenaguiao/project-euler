import time
start = time.time()
L = 50

tiles = [[True for _ in range(-L, L)] for _ in range(-L, L)]
ant = [[L, L], "N"]

def PrintTiles(mat):
    for l in mat:
        w = ""
        for k in l:
            if k:
                w += "1"
            else:
                w += "0"
        print(w)
ans = []
for i in range(50*L):
    if ant[1] == "N":
        if tiles[ant[0][0]][ant[0][1]]:
            #White tile
            ant[1] = "E"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][0] += 1
            ans.append(1)
        else:
            ant[1] = "W"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][0] -= 1
            ans.append(0)
    elif ant[1] == "E":
        if tiles[ant[0][0]][ant[0][1]]:
            #White tile
            ant[1] = "S"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][1] -= 1
            ans.append(1)
        else:
            ant[1] = "N"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][1] += 1
            ans.append(0)
    elif ant[1] == "S":
        if tiles[ant[0][0]][ant[0][1]]:
            #White tile
            ant[1] = "W"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][0] -= 1
            ans.append(1)
        else:
            ant[1] = "E"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][0] += 1
            ans.append(0)
    elif ant[1] == "W":
        if tiles[ant[0][0]][ant[0][1]]:
            #White tile
            ant[1] = "N"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][1] += 1
            ans.append(1)
        else:
            ant[1] = "S"
            tiles[ant[0][0]][ant[0][1]] = not tiles[ant[0][0]][ant[0][1]]
            ant[0][1] -= 1
            ans.append(0)
    #PrintTiles(tiles)
    print("Step ", i, " ant is in (", ant[0][0]-L, ", ", ant[0][1]-L, ") facing ", ant[1])



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")