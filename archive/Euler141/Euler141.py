import time
import math
start_time = time.time()

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    

def brute(LIM):    
    L = []
    for n in range(LIM):
        nsq = n * n
        boolean = False
        for q in range(1, n):
            r = nsq % q
            d = (nsq - r)// q
            if  q * q == d * r:
                boolean = True
                print("nsq = ", nsq, " | r = ", r, " | q = ", q, " | d = ", d)
                #print("ratio = ", q / r)
                a = gcd(d, r)
                b = math.floor(math.sqrt(r //a))
                c = math.floor(math.sqrt(d // a))
                print("a = ", a,  " | b = ", b, " | c = ", c)
        if boolean:
            print("FOUND = ", n)
            L += [nsq]
    print(L)


def is_sq(n):
    k = math.floor(math.sqrt(n))
    return n == k * k


def fun(a, b, c):
    return a * b * ( a * c * c * c + b)


def run(LIM):
    L = []
    a = 1
    while True:
        b = 1
        c = 2
        f = fun(a, b, c)
        if f > LIM:
            break
        while True:
            c = b + 1
            f = fun(a, b, c)
            if f > LIM:
                break
            while f <= LIM:
                if gcd(b, c) == 1 and  is_sq(f):
                    L += [f]
                c += 1
                f = fun(a, b, c)
            b += 1
        a += 1
    print(sum(L))

#brute(4000)
run(10**12)
print("--- %s seconds ---" % (time.time() - start_time))
