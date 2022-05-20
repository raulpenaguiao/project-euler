from queue import PriorityQueue
import time
start_time = time.time()

def f(tpl):
    sym = tpl[1] + tpl[0] + tpl[2]
    sym2 = tpl[0]*tpl[1] + tpl[2]*tpl[0] + tpl[1]*tpl[2]
    tq = (tpl[3]-2) * ( tpl[3]-1)
    ans = 2 *  sym2
    ans += sym * 4 * (tpl[3]-1)
    ans += 4 * tq
    return ans

"""
print("f(3, 2, 1, 1) = ", f((3, 2, 1, 1)))
## > 22
print("f(3, 2, 1, 2) = ", f((3, 2, 1, 2)))
## > 46 
print("f(3, 2, 1, 3) = ", f((3, 2, 1, 3)))
## > 78
print("f(3, 2, 1, 4) = ", f((3, 2, 1, 4)))
## > 118
print("f(5, 1, 1, 1) = ", f((5, 1, 1, 1)))
## > 22
print("f(5, 3, 1, 1) = ", f((5, 3, 1, 1)))
## > 46
print("f(7, 2, 1, 1) = ", f((7, 2, 1, 1)))
## > 46
print("f(11,1, 1, 1) = ", f((11,1, 1, 1)))
## > 46
"""

def C(n, counter_LIM):
    queue = PriorityQueue()
    queue.put((f((1, 1, 1, 1)), (1, 1, 1, 1)))
    counter = 0
    prev_value = 0
    prev_value_accum = 0
    while not queue.empty() and counter < counter_LIM:
        (an, tpl) = queue.get()
#        print("f(", tpl, ") = ", an)
        if an == prev_value:
            prev_value_accum += 1
        else:
            if prev_value_accum == n:
                return prev_value
            prev_value = an
            prev_value_accum = 1
        counter += 1
        new_tpl = (tpl[0], tpl[1], tpl[2], tpl[3] + 1)
        val = f(new_tpl)
        queue.put((val, new_tpl))
        if tpl[3] == 1:
            if tpl[2] + 1 <= tpl[1]:
                new_tpl = (tpl[0], tpl[1], tpl[2]+1, tpl[3])
                val = f(new_tpl)
                queue.put((val, new_tpl))
            if tpl[2] == 1:
                if tpl[1] + 1 <= tpl[0]:
                    new_tpl = (tpl[0], tpl[1]+1, tpl[2], tpl[3])
                    val = f(new_tpl)
                    queue.put((val, new_tpl))
                if tpl[1] == 1:
                    new_tpl = (tpl[0]+1, tpl[1], tpl[2], tpl[3])
                    val = f(new_tpl)
                    queue.put((val, new_tpl))
    return "counter ran out"

LIM = 8000000
n = 1000
print(C(n, LIM))

"""
for i in range(1, LIM):
    for j in range(i, LIM):
        for k in range(j, LIM):
            for n in range(1, 10):
                ans = f(i, j, k, n)
                if ans in lis:
                    lis[ans] += [(k, j, i, n)]
                else:
                    lis[ans] = [(k, j, i, n)]
print(lis)
"""



print("n = ", n, " | LIM = ", LIM, " | --- %s seconds ---" % (time.time() - start_time))


