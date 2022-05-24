import time
start_time = time.time()


def gcd(b, c):
    if b == 0:
        return c
    return gcd(c%b, b)


def times(l1, l2):
    return red_list([l1[0]*l2[0], l1[1]*l2[1]])

def add_lists(l1, l2):
    return red_list( [l1[0] * l2[1] + l1[1] * l2[0] ,  l1[1] * l2[1]])

def red_list(l):
    d = gcd(l[0], l[1])
    return [l[0]//d, l[1]//d]


def has_one_sheet(tpl):
    count = 0
    for i in tpl:
        count += i
    return count == 1


n = 4
batch = 1

queue = {
        tuple([1]*n) : [1, 1]
}

empty = tuple([0]*n)

tot = [0, 1]

while not(empty in queue):
    batch += 1
    new_queue = {}
    for tpl in queue:
        if has_one_sheet(tpl):
            tot = add_lists(tot, queue[tpl])
        #count non-zero entries
        count = 0
        for i in range(n):
            count += tpl[i]
        for i in range(n):
            if not tpl[i] == 0:
                new_p = list(tpl)
                new_p[i] -= 1
                for k in range(i):
                    new_p[k] += 1
                new_tpl = tuple(new_p)
                toadd = times(queue[tpl], [tpl[i], count])
                if new_tpl in new_queue:
                    new_queue[new_tpl] = add_lists(new_queue[new_tpl], toadd)
                else:
                    new_queue[new_tpl] = toadd
    queue = new_queue
    for tpl in queue:
        print(tpl, " -> ", queue[tpl])
    print("End of batch ", batch)
    print("tot = ", tot[0], " / ", tot[1])
    print("_______________________________")


print("tot = ", tot[0], " / ", tot[1])
print(tot[0]/tot[1])

print("--- %s seconds "%(time.time() - start_time))
