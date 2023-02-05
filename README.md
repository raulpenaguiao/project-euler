# project-euler
This is where I will leave the code related to project euler



## Problem explanation

### Problem 122 - Efficient exponentiation

**python**

Features:
 - An exponentiation sequence is an *additive* sequence
 - BFS over all possible additive sequences that satisfy some lax inequalities
 - Runs in less than 20 seconds for < 190
 - Runs in 8 min < in UZH computers for m = 200

Bugs:
 - Memory goes bust for m > 190 in a laptop!

---

### Problem 126 - Cuboid layers

**python**

Features:
 - Formula for layer of cuboid computed with tuple f
 - Priority queue to cycle over all tuples
 - Search on the space of tuples is tree-like, so there is no repeated computations
 - Queue search limited in scope for protection
 - Priority is set by the value of f, so when we reach a tuple that has some specific value, all tuples with lower values have already been visited

Time:
 - 27.75s to run for n = 1000
---

### Problem 138 - Special isoceles triangles

**python**

Features:
 - b has to be even number, b = 2 b'
 - Use formula for Pythagorean triples (h, b', L) gives triple (t, r, s)
 - t has to be 1 for mdc considerations
 - Given equation reduces to (s-2 r)^2 - 5 r^2 = +- 1
 - [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation) gives us solution to these equations knowing the convergents of sqrt(5)

Time:
 - 0.05ms for the first 12 isoceles triangles
 - 2.7s for first 12k isoceles triangles
---

### Problem 141 - Investigating progressive numbers, n, which are also square

**python**

Features:
 - Integers are in a geometric series x, y, z if x = a * b^2, y = a * b * c, and z = a * c^2 with b, c coprime and b < c
 - We can take wlog d > q > r
 - Get formula n^2 =a * b * ( a * c^3 + b )
 - Run this formula for all a, b, c in restrictions until we get values larger than the limit


Time: 
 - 10.5s to run until $10^12$

---
### Problem 142 - Perfect Square Collection

**python**

Features:
 - Pitagorean triples: if $f^2+g^2 = h^2$, then there are integers $r, m, n$ such that $f = r(m^2 - n^2)$, $ g = 2 r m n $ and $h=r (m^2+n^2)$, or symmetrically about $f, g$
- Let $a^2 = x - y$, $b^2 = y - z$ and $d^2 = y + z$. These numbers satisfy the following constraints:
$ b \equiv_2 d$, $d > b$, and $ a^2 + b^2, a^2 + d^2, a^2 + b^2 + d^2$ are squares.
 - We can use pitagorean triples on $a^2$, $b^2$ and $a^2+b^2$. Write $a^2 = r (m^2-n^2)$ and $b^2 = 2 r m n$, (OR switch a and b, one of these will find the minimal solution).
 - Find $d, r, m, n$ integers such that the above holds that minimize 
$ d^2\frac{2}{3} + r (m^2-n^2) - r m n$
 - Minimizing formula depends quadratically on $d$, so this is the variable that can grow faster while $r, m, n$ should grow slower$.

Time:
 - 7.333s


---
### Problem 151 - Paper sheets of standard sizes: an expected-value problem

**python**

Features:
 - Random processes
 - Brute force
 - Partitions
 - Hash functions and dictionaries

Time:
1ms

Notes:
This problem could have been done much faster were it to be said how the random removal was to be done.
I, for some reason, assumed that the random extraction of the paper was to be done uniformly over all sizes.


---

### Problem 184 - Triangles containing the origin

**python**

Features:
 - For any general three points on the upper half of the plane, there are 8 possible triangles with vertices on these points or their reflection along the origin that do not contain the origin in its border
 - Of these 8 triangles, exactly two of them have the origin in the interior
 - The "general" condition is satisfied when no two points are colinear with the origin
 - The algorithm runs over all integer points in the upper half plane on a lim x 2lim box, selecting all the points that are inside the desired circle
 - For all such points with "primitive" coordinates (gcd = 1), count how many points are multiples, this is an algebraic computation
 - The final formula can be obtained by knowing all these numbers


Time:
24ms to run up to 105. Complexity is quadratic.


---

### Problem 186 - Connectedness of a network

Features:
Eeach time a call is made we merge trees by point one root to the other root.
This data structure allows for a seamless union of sets.
We just have to remember how many elements are below a root at every time.

Time:
838.96 seconts.
For some reason the code starts to slow down once we pass 1M calls. I want to search the reason for this


---

### Problem 201 - Subsets with a unique sum

**pythohn**


Features:
 - The problem starts with a very scary number of subsets of size 50. This is not the way to do
 - Define v[s][k][t] to be the number of sets of size k that sum up to t
 - s <= 100, k <= s and k <= 50.
 - This satisfies a recursive relation
 - Layer the vector v so that we only use the recursive relation on the previous value, allowing us to save up on 50* less memory.

Time:
204.8 seconds


---

### Problem 202 - Laserbeam
3rd October 2022

**python**

Features:
 - The number of paths with N bounces is the number of pairs (a, b) that are coprime such that a+b = 2 N - 3 and a -b = 0 mod 3
 - We code a function PHI2 that runs over all elements a < M = (N+3)/2, compute its gcd with M-a, and checks if it is one
 - Dues to symmetry, we can stop att M/2
 - In the forum, exact formulas were found for phi2 in the case studied, where it is approximately phi/3

Time: 1828 seconds

---


### Problem 237 - Tours on a 4 x n playing board
17th December 2022

**python**

Features:
 - Interpret a walk on the board as a path of length n between the connections
 - Paths on graphs are powers of matrices
 - Fast exponentiation


Further reading:
Consider the gaph with 6 vertices a, b, c, d, f, g
Reading vertically, representing connections with - and non connections with |, we have
a = --||
b = ||--
c = -||-
d = |--|
f = g = ----
The difference between f and g is how the nodes connect to the left (first with last, second with third OR first with second and third with last)
We draw edges v -> w if v can be placed exactly on the right, allowing for a complete path.


Time: 2.69ms, blazingly fast


### Problem 757 - Stealthy numbers
24th May 2022

**python**

Features:
 - Zeores of a degree two polynomial. If (x-a)(x-b) = x^2 - F'x + N and (x-c)(x-d) = x^2 - Fx + N, these polynomials have integer solutions and F + 1 = F'
 - Integer solutions of quadratics means F^2 - 4N is a square x^2 and (F+1)^2 - 4N = y^2
 - x and y satisfy 0 < x < y - 1 and x = y + 1 mod 2, are integers
 - Given x, y we have 4 N = (y^2 - x^2 - 1)^2 - x^2
 - We can find all N that satisfy an equation of this type by checking all x, y < sqrt(N)
 - This may look O(N) but for each N^(1/4 + eps) < y < sqrt(N) we just need to run x until a bound that only depends on epsilon, so complexity is O(N^(1/4+1/2))

Time:
100 seconds in UZH server

---

### Problem 624 - Two heads are better than one
10th October 2022

**python**

Features:
 - Rational and a sqrt(5) + b numbers data structure that allows for multiplication, division, subtraction etc.
 - Geometric formula for the sum of Fibonnacci numbers
 - The probabilities of the desired events can be written using Fibonnacci numbers

Time:
0.011 seconds, blazingly fast

---

### Problem 630 - Crossed lines 
29th May 2022

**python**

Features:
 - Sorting all the lines according to the slope gives us a partition of the lines into blocks
 - The final answer is, where L is the set of lines and the sum runs over blocks of parallel lines
$$ \sum_{b} |b| \times (|L| - |b|) $$ 
because each line intersects any non-parallel line
 - Used fractions as pairs of integers, so precision will never be an issue


Time: 
73.37s which is just above the threshold

---

### Problem 662 - Fibonacci paths
24th May 2022

**python**

Features:
 - Simple dynamic programming on a 10k x 10k grid
 - There are 20 fibonacci numbers <= 10k and there are 50 + 2*20 = 90 relevant steps in a 10k x 10k grid
 - This all amounts to 900M operations, and the long time is atributed to the poor management of lists from python


Time:
4000 seconds in UZH server

Notes:
This code can be much more eficient in C++

---

### Problem 679 - Freefarea
27th May 2022

**python**

Features:
 - Dynamic programming on a $2^{12}  x 30$  grid
 - DP[n][word][b1, b2, b3, b4] is the number of words of length n that end in word, and have an occurrence of the desired strings or not, according to b1, ..., b4

Time:
0.536 seconds for LIM = 30

---
### Problem 714 - Duodigits
07th January 2022
**python**

Features:
 - Precomputation of all duodigit numbers up to $2^{21}$
 - Brute force

Time: 400s

---
### Problem 717 - Summation of a modular formula
10th Jan 2023
**python**

Features:
 - Modular power and fast exponentiation
 - g(p) has a formula, is the quotient of the following number by p
$$ ( 2^p mod p^2) * (2^{p-2} * 2^{ 2^p mod p-1} mod p) mod p^2$$
This can be proven by a mix of Fermat's theorem and clever rearangement

Time: 17.345s

---

### Problem 727 - Triangle of circular arcs
02nd June 2022
**python**

Features:
 - Computational geometry
 - The point E = (xe, ye) arises as the solution of the following system of three equations, where $r$ is the radius of the inner small circle centered at E
$$ |EB|^2 = x_e^2 + y_e^2 = (r + r_b)^2$$
$$ |EC|^2 = (x_e - x_c)^2 + y_e^2 = (r + r_c)^2 $$
$$ |EA|^2 = (x_e - x_a)^2 + (y_e - y_a)^2 = (r + r_a)^2 $$
 - These three equations all simplify to two linear equations which give $x_e = x_e(r)$ and $y_e = y_e(r)$
 - Using these linear equations on the first equation, we obtain a quadratic formula that $r$ must hold.
 - To distinguish which of these solutions interests us we should pick the smallest such that r > 0
 - Regular python precision is enough to carry the errors

Time: 0.84s

---

### Problem 737 - Coin Loops
10th Jan 2023

**python**

Features:
 - Complex numbers
 - Recursive formula for the center of mass: starting with $y_0 = 1$
$$theta_n = arccos(|y_{n-1}|/2) + cis(y_{n-1})$$
$$y_n = (e^{i theta_{n} * n y_{n-1})/n+1)$$


Time: 861.4s

---

### Problem 772 - Balanceable k-bounded partitions
28th May 2022

**python**

Features:
 - Answer is lcd(1, ..., k) * 2. This can be computed by computing all the primes smaller than k
 - It is easy to observe that 2*j should divide f(k), because if n = 2 j * m + r, for r < 2j, the following partition j + ... + j + r is not balanceable.
 - It turns out that all these partitions cover all n < lcd(1, ..., k) * 2
 - Algorithm can be sped up with fast primality test like miller rabbin, instead of sieving.

Time:
56s for LIM = 10 ** 8

---
### Problem 779 - Prime factor and Exponent
07th Jan 2023

**python**

Features:
 - To compute the limit, we split the terms into sets $M_p = \{n | p(n) = p\}$
 - The sum on each set commutes with the limit, because of monotone convergence theorem
 - A closed form for each term can be computed when $N = p_1... p_{m-1}p_m^a$ and $a$ is brought to infinity.
In this case, there are exactly $\phi(p_1 ... p_{m-1}) (p^{a -b} - p^{a-b-1})$ terms that have $p(n) = p_m$ and $a(n) = b$
 - Simplified formula
$$ \sum_{K\geq 1} f_K = \sum_i \left( \prod_{j<i} \frac{p_j-1}{p_j} \right) \frac{1}{(p_m)^2p_m}$$
 - Precomputing powers up to 1M



Time:
321ms

---

### Problem 788 - Dominating Numbers
26th May 2022

**python**

Features:
 - Combinatorial formula to get DP to work
 - Linear time if binomials are precomputed

$$\sum_{u=0}^{} \zeta(u)\left[ \binom{LIM + 1}{u + 1} - \binom{2*u - 1}{u + 1} \right] $$

Here we are using prod = [1, 9, 9*9, 9*9*8, 9*9*8*7, ...] representing the choices of digits that we have for each block
$$ \zeta(u) = \sum_{\lambda \vdash [u] } prod( \ell(\lambda )) $$

Time:
0.89s after optimization
---

### Problem 804 - Counting Binary Quadratic Representations
1st July 2022

**python**

Features:
 - Counting integer points inside an algebraic curve

Time: 
15s
---


### Problem 813 - XOR-Powers
06th Jan 2023

**python**

Features:
 - Product and sum operations given are equivalent to polynomial ring structure in F2
 - Conversion from a polynomial to the corresponding number is simply evaluation at 2, in Z
 - We can compute powers of polynomials and powers module using fast exponentiation
 - Students' dream formula applies! 
$$(x + y)^{2^k} = x^{2^k} + y^{2^k}$$

This means that computing the power of a polynomial p can be done with the odd and even factors separately.
Specifically, we want to compute $(1 + x + x^3)^{8^12 * 12^8}$ but $8^{12} * 12^8 = 2^{52} * 3^8$
So we can compute (1 + x + x^3)^{3^8}$ directly (giving us a list of size $3^8 * 3 \sim 20k$), the resulting polynomial raised to $2^{52}$ is the same as the polynomial in the variable $x^{2^{52}}$

Time:
42ms
---


