import time
start_time = time.time()

def compute_sum(LIM):
    vis = ["off" for i in range(LIM+1)]
    counter = 1
    vis[0] = 0
    vis[1] = 0
    queue = {(1,)}
    turn = 0
    while counter < LIM and turn <= 10:
        turn += 1
        newQueue = set(())
        for tuple_additive in queue:
            l = len(tuple_additive)
            for i in range(l):
                for j in range(i, l):
                    new_el = tuple_additive[i] + tuple_additive[j]
                    if new_el > tuple_additive[-1] and new_el <= LIM:
                        if vis[new_el] == "off":
                            counter += 1
                            vis[new_el] = turn
                        newQueue.add(tuple_additive + (new_el,))
        queue = newQueue.copy()
    return vis

## This program does not run correctly for numbers > 190, it has memory issues!
##For numbers smaller, it runs for < 20s
LIM = 185
vis = compute_sum(LIM)
print(sum(vis))
print("LIM = ", LIM, "--- %s seconds ---" % (time.time() - start_time))

