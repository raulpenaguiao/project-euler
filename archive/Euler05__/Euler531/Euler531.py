import time
import math

start_time = time.time()

lLIM = 10**6
uLIM = 10**6+5*10**3

is_prime = [0, 1]*(uLIM//2+1)
is_prime[2] = 1
is_prime[1] = 0
for i in range(3, uLIM, 2):
    if is_prime[i] == 1:
        for m in range(i*i, uLIM, i):
            is_prime[m] = 0

primes = []
for i in range(uLIM):
    if is_prime[i] == 1:
        primes += [i]


def prime_fact(n):
    k = n
    ind = 0
    pis = []
    ais = []
    ai = 0
    p = primes[ind]
    while p*p <= k:
        while k%p == 0:
            ai+= 1
            k //= p
        if ai > 0:
            pis.append(p)
            ais.append(ai)
            ai = 0
        ind += 1
        p = primes[ind]
    if k > 1:
        pis.append(k)
        ais.append(1)
    return [[k[0], k[1], k[0]**k[1]] for k in zip(pis, ais)]


p_facts = [[]]*(uLIM-lLIM)
for i in range(lLIM, uLIM):
    p_facts[i-lLIM] = prime_fact(i)


def euler_phi(n):
    tot = 1
    for p, i, po in p_facts[n-lLIM]:
        tot *= (po - po//p)
    return tot

euler_phis = [[]]*(uLIM-lLIM)
for i in range(lLIM, uLIM):
    k = euler_phi(i)
    res = [k%po for p, i, po in p_facts[i-lLIM]]
    mod = [po for p, i, po in p_facts[i-lLIM]]
    euler_phis[i-lLIM] = [res, mod]


def extended_gcd(a, b):
    ## returns a triple x, y, d such that a*x + b*y = d = gcd(a ,b)
    r = a%b
    if r == 0:
        return [0, 1, b]
    x, y, d = extended_gcd(b, r)
    return [y, x-y*(a//b), d]


def gcd(a, b):
    r = a%b
    if r == 0:
        return b
    return gcd(b, r)


def chinese_rem(res, mod): 
    # returns a pair [a, p] where the solution is a mod p
    # assumes that all mods are coprime
    if len(res) < 3:
        if len(res) == 1:
            return[res[0], mod[0]]
        t, u, d = extended_gcd(mod[0], mod[1])
        if d > 1:
            print("MERDA")
            print(" res = ", res , " and mod = ", mod)
            return "KESTA MERDA"
        m = mod[0]*mod[1]
        r = res[0]*mod[1]*u + res[1]*mod[0]*t
        r %= m
        return [r, m]
    k = chinese_rem(res[1:], mod[1:])
    return chinese_rem([res[0], k[0]], [mod[0], k[1]])



def f(n, m):
    ## returns the value of chinese_rem([phi(n), phi(m)], [n, m])
    ## we need to account for the fact that we have some non-coprimality
    if gcd(m, n) == 1:
        return chinese_rem(euler_phis[n-lLIM][0]+ euler_phis[m-lLIM][0], euler_phis[n-lLIM][1] + euler_phis[m-lLIM][1])
    primes_of_n = len(p_facts[n-lLIM])
    primes_of_m = len(p_facts[m-lLIM])
    vis = [0]*primes_of_m
    res = []
    mod = []
    #print(primes_of_n, " - ", primes_of_m)
    #print(p_facts[n-lLIM], " - ", p_facts[m-lLIM])
    for i in range(primes_of_n):
        found = 0
        for j in range(primes_of_m):
            if p_facts[n-lLIM][i][0] == p_facts[m-lLIM][j][0]:
                vis[j] = 1
                found = 1
                pon = euler_phis[n-lLIM][1][i]
                pom = euler_phis[m-lLIM][1][j]
                ren = euler_phis[n-lLIM][0][i]
                rem = euler_phis[m-lLIM][0][j]
                ##check which one is the largest
                if pon > pom:
                    po = pon
                    re = ren
                    ##check if they contradict eachother
                    if not ren%pom == rem:
                        return [0, 0]
                else:
                    po = pom
                    re = rem
                    ##check if they contradict eachother
                    if not rem%pon == ren:
                        return[0, 0]
                res.append(re)
                mod.append(po)
        if found == 0:
            res.append(euler_phis[n-lLIM][0][i])
            mod.append(euler_phis[n-lLIM][1][i])
    for j in range(primes_of_m):
        if vis[j] == 0:
            res.append(euler_phis[m-lLIM][0][j])
            mod.append(euler_phis[m-lLIM][1][j])
    return chinese_rem(res, mod)

#n = 10**6+4
#m = 10**6+2813
#print(f(n, m))


tot = 0
for n in range(lLIM, uLIM):
    print(n)
    for m in range(n+1, uLIM):
        #print(" m  = ", m, " and n = ", n)
        k = f(n, m)
        if not k == "ERROR":
            tot += k[0]
print("Answer is ", tot)
print(" --- %s seconds --- "%(time.time() - start_time))
