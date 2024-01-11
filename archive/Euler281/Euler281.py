#Code completed on the 2024/01/10
#Burnside lemma. The number of orbits of a group action is given by a simple sum
#In this case, the set of pizza toppings $X_{m, n}$ has an action of the cyclic group $C_{mn}$, we wish to count $X_{m, n}/_{C_{mn}}$
#Burnside's lemma predicts that $|X_{m, n}/_{C_{mn}}| * |C_{m n}| = \sum_{g\in C_{mn}} |X_{m, n}^g|$
#Counting $|X_{m, n}|$ is easy with a combinatorial argument. Labelling all the different toppings we count $(mn)!$,
# but permuting each subset of toppings gives a class of size $n!$ so $|X_{m, n}| = \frac{(mn)!}{(n!)^m}$
#We need to count the size of the stabilizer. Let $e$ be the rotation given by $\frac{2 \pi}{mn}$, a generator of $C_{mn}$, and $g = e^k$.
#A pizza topping is stabilized by $g$ if and only if it is stabilized by $e^{(k, mn)}$. Let $d = (k, mn)$.
#There are $d$ groups of size $t = mn/d$ slices that have to have the same topping.
#Counting such toppings is equivalent of counting
#   the number of toppings with $m$ different toppings on $d$ larger slices,
#   where we want each topping to be in $n/t$ such slices. 
#Thus $t$ has to be a divisor of $n$. In this case the number is thus $|X_{m, n/t}|$
#We get the following formula for $f(m, n) = \sum_{t | n} \sum_{k = 1, \ldots , mn :  (k, mn) = mn/t} |X_{m, n/t}|$
#Finally, we note that the number of indices $k = 1, \ldots , mn$ for which $(k, mn) = mn/t$ for a fixed $t$ is $\phi(t)$
#   as these are given by $k = mn*t \times z$ where $z\perp t$ is an integer in $1, \ldots t$.
#Code runs in 3 ms


import time
start = time.time()
from ...CL.CL_Primes import EulerPhi, Divisors, Primes

ans = 0
primes = Primes(1000)

LIM = 10**15
lim = 10
fact = [1]
for i in range(1, 1+lim*lim):
    fact.append(i*fact[-1])
#Find smallest index such that fact[i] > LIM
IND = 1
while(fact[IND] <= LIM):
    IND += 1
for i in range(1+lim*lim, 1+(IND+2)*(2+ IND)):
    fact.append(i*fact[-1])
lim = IND + 2



def F(m, n):
    tot = 0
    phi = EulerPhi(n)
    for t in Divisors(n, primes):
        s = phi[t]*fact[m*n//t]//(fact[n//t]**m)
        tot += s
    return tot//(m*n)



for m in range(2, lim+1):
    n = 1
    f = F(m, n)
    if f > LIM:
        break
    while(f <= LIM):
        ans += f
        n += 1
        f = F(m, n)


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")