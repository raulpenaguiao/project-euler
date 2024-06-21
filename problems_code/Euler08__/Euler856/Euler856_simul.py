import time
start = time.time()
import random
from math import floor


unpairedCounter = 0
def Generate():
    cards = [floor(random.random()*52)]
    nCards = 1
    while(True):
        newCard = floor(random.random()*52)
        while newCard in cards:
            newCard = floor(random.random()*52)
        if cards[-1]%13 == newCard%13:
            #print(cards + [newCard])
            return nCards + 1
        cards += [newCard]
        nCards += 1
        if nCards == 52:
            #print("OUT")
            global unpairedCounter
            unpairedCounter += 1
            return 52
    


count = 0
hits = 0
while(True):
    count += 1
    hits += Generate()
    if count%530431 == 312:
        print(count, hits/count, unpairedCounter/count)


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")