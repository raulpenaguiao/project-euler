#Code written on the 2024/06/04
#Simulates the ant progress until we spot a pattern
#Modular arithmetic to compute the case for $10^{18}$
#Runs in 4ms



import time
start = time.time()
ans = 0

#Black = False
#White = True


def Blacks(N, verbose = False):
    ant = [[0, 0], "N"]
    blacks = {}
    WHITE='\U00002B1C'
    BLACK='\U00002B1B'
    GREEN='\U0001F7E9'
    ORANGE='\U0001F7E7'

    infoFromColour = {True : {
            "N" : ["W", tuple([-1, 0])], 
            "E" : ["N", tuple([0, 1])], 
            "S" : ["E", tuple([1, 0])], 
            "W" : ["S", tuple([0, -1])]}, 
                    False: {
            "N" : ["E", tuple([1, 0])], 
            "E" : ["S", tuple([0, -1])], 
            "S" : ["W", tuple([-1, 0])], 
            "W" : ["N", tuple([0, 1])]}}
    COLOURS = [WHITE, BLACK, GREEN, ORANGE]

    steps = 0
    while(steps < N):
        steps += 1
        Walk(ant, blacks, infoFromColour)
    if verbose:
        PrintTiles(ant, blacks, COLOURS)
    return NumberBlacks(blacks)



def PrintTiles(ant, blacks, colours):
    largestEntry = max(abs(ant[0][0]), abs(ant[0][1])) + 1
    for key in blacks:
        largestEntry = max(largestEntry, key[0])
        largestEntry = max(largestEntry, key[1])
    #print(largestEntry, ant)
    #print(blacks)
    logic = {False:{True:colours[0], False:colours[1]}, True:{True:colours[2], False:colours[3]}}
    for y in range(largestEntry, -largestEntry-1, -1):
        str = ""
        for x in range(-largestEntry, largestEntry+1):
            pt = tuple([x, y])
            flag1 = False
            flag2 = True
            if x == ant[0][0] and y == ant[0][1]:
                flag1 = True
            if pt in blacks and blacks[pt]:
                flag2 = False
            #print(pt, ant, flag1, flag2)
            str += logic[flag1][flag2]
        print(str)

def Walk(ant, blacks, infoFromColour):
    colour = False
    pt = tuple(ant[0])
    if pt in blacks and blacks[pt]:
        colour = True
    blacks[pt] = not colour

    direction, cartesian = infoFromColour[colour][ant[1]]
    ant[0][0] += cartesian[0]
    ant[0][1] += cartesian[1]
    ant[1] = direction

def NumberBlacks(blacks):
    ans = 0
    for key in blacks:
        if blacks[key]:
            ans += 1
    return ans
PERIOD = 104
START_PERIOD = 10_300
START_PERIOD += (- START_PERIOD)%PERIOD
N = 10**18

if N > START_PERIOD:
    b1 = Blacks(START_PERIOD + N%PERIOD)
    b2 = Blacks(START_PERIOD + PERIOD + N%PERIOD)
    ans = b1 + (b2-b1)*(N-(START_PERIOD + N%PERIOD))//PERIOD
else:
    ans = Blacks(N)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")