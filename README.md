# project-euler
This is where I will leave the code related to project euler



For python, to make sure we have the right classes on the code, we have to run in the uppermost folder (project-euler) the following command

```bash
python3 -m project-euler.problems_code.EulerXXX.EulerXXX
```

or
```bash
python3 -m project-euler.archive.EulerXXX.EulerXXX
```
This guarantees that all modules are correctly loaded.
Note that you should not type the extention .py of the file

## Problem explanation

### Problem 122 - Efficient exponentiation

**python**

Features:
 - An exponentiation sequence is an *additive* sequence
 - BFS over all possible additive sequences that satisfy some lax inequalities
 - Runs in less than 20 seconds for < 190
 - Runs in 8 min < in UZH computers for $m = 200$

Bugs:
 - Memory goes bust for $m > 190$ in a laptop!

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
    27.75s to run for $n = 1000$

---

### Problem 138 - Special isoceles triangles

**python**

Features:
 - b has to be even number, $b = 2 b'$
 - Use formula for Pythagorean triples $(h, b', L)$ gives triple $(t, r, s)$
 - t has to be 1 for mdc considerations
 - Given equation reduces to $(s-2 r)^2 - 5 r^2 = +- 1$
 - [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation) gives us solution to these equations knowing the convergents of sqrt(5)

Time:
    0.05ms for the first 12 isoceles triangles
    2.7s for first 12k isoceles triangles


---

### Problem 141 - Investigating progressive numbers, n, which are also square

**python**

Features:
 - Integers are in a geometric series $x, y, z$ if $x = a * b^2$, $y = a * b * c$, and $z = a * c^2$ with $b, c$ coprime and $b < c$
 - We can take wlog $d > q > r$
 - Get formula $n^2 =a * b * ( a * c^3 + b )$
 - Run this formula for all a, b, c in restrictions until we get values larger than the limit


Time: 
    10.5s to run until $10^{12}$

---
### Problem 142 - Perfect Square Collection

**python**

Features:
 - Pitagorean triples: if $f^2+g^2 = h^2$, then there are integers $r, m, n$ such that $f = r(m^2 - n^2)$, $ g = 2 r m n $ and $h=r (m^2+n^2)$, or symmetrically about $f, g$
 - Let $a^2 = x - y$, $b^2 = y - z$ and $d^2 = y + z$. These numbers satisfy the following constraints:
$ b \equiv_2 d$, $d > b$, and $ a^2 + b^2, a^2 + d^2, a^2 + b^2 + d^2$ are squares.
 - We can use pitagorean triples on $a^2$, $b^2$ and $a^2+b^2$. Write $a^2 = r (m^2-n^2)$ and $b^2 = 2 r m n$, (OR switch a and b, one of these will find the minimal solution). There is also a coprimality condition but I don't care too much for that.
 - Find $d, r, m, n$ integers such that the above holds that minimize  $$ d^2\frac{2}{3} + r (m^2-n^2) - r m n $$
 - Minimizing formula depends quadratically on $d$, so this is the variable that can grow faster while $r, m, n$ should grow slower.

Time:
 - 7.333s
---

### Problem 143 - Torricelli Triangles

- Code created on the 30/10/2023
- Uses the fact that the angles at X are 120
- Cosine law tells us that a**2 = p**2 + p*q + q**2 and so on
- Solutions to this equation can be generated with the formula in
    https://www.had2know.org/academics/integer-triangles-120-degree-angle.html
- Generate first all allowed pairs (p, q) that have an integer solution above, there are $3\times 10^5$ such pairs
    then run over all p and try to find q and r that are themselves an allowed pair

Time: 
    Runs in 8.61 seconds


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
### Problem xxx - 
18th January 2024

**python**

Features:
 - Miller Rabin
 - Meet in the middle
 - Set of sums
 - Set of sums within interval
 - Rationals class
 - Divisibility

Notes:
This was really a tough nut to crack. I believe the hardest problem in PE that I have solved. For sure the one that took the most time from me.
I tried a bunch of strategies, like meet in the middle and creating sum sets that sum in a bounded target
I came across a really nice fact when searching for this problem on the net (kudos to  [Setphan Brumme](https://euler.stephan-brumme.com/152/) for pointing it out).
I don't usually search for ideas on the internet and if I do it is often on [Project Euler chat](projecteuler.chat)
The idea presented there is that for you to clear primes from the denominator, you have to use denominators with this prime.
This clears all primes that occur once, and the ones that occur more than once can be tested individually to find all the sums that clear the denominators
To be careful that some numbers are multiples of different large primes (ex 35=5*7) so make sure you test it on only one prime
To be careful as well on the meet in the middle strategy that when we find a hit, there may be another term just behind the hit that should be counted. This makes a huge difference!
The roller coaster of this problem proved to be extremely interesting but frustrating...

Time:
2.509976 seconds seconds




---
### Problem 153 - Investigating Gaussian Integers

**python**

Features:
 - Divisors of integers

Notes:
    Code made on the 26/10/2023
    For each divisor d we count how many positive integers $k$ are there such that $d|k$, and multiply by $re(d)$.
    If $d$ is integer, this is done directly (add $i\times (N//i)$)
    if $a, b > 0$, then $a + ib$ divides all the multiples of $d(a'^2 + b'^2)$, where $d = gcd(a, b)$, $a' = a/d$, $b' = b/d$
    so for all $a', b'$ coprime, we simply sum $d a' (N//(d(a'^2 + b'^2)))$
    if $im(d) < 0$, we just copy what happens on the positive side (multiply by 2)

Time: 
    74.51598477363586s

---
### Problem 154 - Exploring Pascal's Pyramid


**python**

Features:
 - Largest prime power dividing $n!$
 - Do rare checks first

Notes:
    Code written on the 2023/11/03
    Once can compute very efficiently the largest exponent $p^t$ that divides $n!$ ($v(p, n)$ function)
    Very directly computes the exponent of 2 and 5 of $\binom{N}{a, b, c}$ and checks if these are >= 12
    Check the fives condition before checking the twos condition

Time: 
    7.8 minutes
    or 470 seconds

---
### Problem 155 - Counting Capacitor Circuits

**python**

Features:
 - Recursion
 - Rational structure

Notes:
    Code written on the 2023/11/08
    Recursively checks what are the numbers that can be obtained for capacity structures
    for precision reasons we use precise rational structure

Time: 
    102.44 seconds


---
### Problem 156 - Counting Digits
3rd November 2023

**python**

Features:
 - Divide and conquer
 - Recursion

Notes:
    Use a divide and conquer approach. if we know $f(n\times 10^s-1, d)$ we can compute $f((n\times 10+t)\times 10^{s-1} - 1, d)$ very easily
    Only divide when there is any chance there is a solution in the interval.

Time: 
    0.023s

---
### Problem 158 - Lexicographical neighbours

**python**

Features:
 - Binomial numbers

Notes:
Code on the 13/11/2023
Formula for $p(n) = (2^n - n - 1)\times \binom{26}{n}$

Time: 
    0.0000 seconds

---
### Problem 161 - Triominoes
1st December 2023

**python**

Features:
 - Memoisation with dictionaries
 - Partitions


Notes:
    In each partially filled board, we identify the uppermost tile to the left that is free, and try to put any tile possible there
    We use memoisation to make sure we dont evaluate a partially filled board twice

Time: 
    593 seconds

---
### Problem 165 - Intersections
13th November 2023

**python**

Features:
 - Geometry
 - Determinant formula for convex points
 - Rational class

Notes:
    For four points, computes four determinantes to check that the points form a convex hull in the determined order
    In this case, we compute the desired intersection point
    We need to rule out the case of several lines intersecting at the same point
    For that we develop a rational data class to be able to check if a point is already the intersection

Time: 
    32.2 seconds

---
### Problem 170 - Pandigital Concatenating Products
7th December 2023

**python**

Features:
 - Permutations
 - GCD and divisors

Notes:
    Generates and orders permutations
    For each permutation, breaks up into pieces and computes the gcd
    For each divisor, tests if this can be the first integer

Time: 
    31.29 seconds
    10s of which is generating all permutations


---
### Problem 171 - Square Sum of the Digital Squares

**python**

Features:
 - Dinamic programing with a recursive relation

Notes:
Code written on the 30/10/2023
Dinamic programing. These numbers satisfy an easy recursive relation
First compute how many numbers with at most N digits have $f(k) = M$
Use this to compute the sum of the numbers with this property

Time: 0.145 seconds


---
### Problem 172 - Few Repeated Digits

**python**

Features:
 - Dinamic programing with a recursive relation

Notes:
Code written on 2023/12/01
Dinamic programming, by counting the number of integers with a digits occurring trice, b digits occurring twice and c digits occurring once
deleting the last digit gives us an easy recursive formula

Time: 3ms

---
###Problem 176 - Right-angled triangles that share a cathetus

**python** and **pen and paper**

Features:
 - Pythagorean triplets $(a, b, c)$ satisfy a formula.
 - Number of solutions of $a=t$, for a fixed $t$, depends on the number of prime factors of $t$ and powers of $2$ that divide $t$.
 - If $F(t)$ is the number of triangles with $t$ as a side, $F(t) = 0$ if $2|t$ but$t$ is not a multiple of $4$.
 - For $t$ odd, $1+2 F(t) = \sigma(t^2)$, for $t$ multiple of $4$, $1+2F(t) = \sigma((t/2)^2)$. The second formula grows much faster.
 - Formula for $\sigma$ wrt its prime factorization.

Time: < 1ms

---
### Problem 180 - Golden Triplets

**python**

Features:
 - Fermat Last Theorem
 - Rational class, this time implemented in an external file

Notes:
Code written on the 2023/11/23
Expression reduces to $(x+y+z)(x^n + y^n - z^n)$ allowed rationals are $a/b$ between $0$ and $1$ such that $b <= K$
Finds all rationals of order 35 (there are 383 such rationals)
for two rationals, compute the four possible z and sees if they are
 - between 0 and 1
 - of the given order

Time: 1.18 seconds

---
### Problem 182 - RSA Encryption

**python**

Features:
 - PowerMod
 - Order of an element of a group

Notes:
Code written on 2023/11/15
$ord_a(m)$ is the smallest integer $i$ such that $m^i = 1 mod a$
a message is unconcealed if 
 -  $a = 0$ mod $pq$, 
 -  a = 0 mod p and ord_q(a)| e-1 and (q, a) = 1
 -  a = 0 mod q and ord_p(a)| e-1 and (p, a) = 1
 -  ord_pq(a)| e-1 and (pq, a) = 1

Time: 45s

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
### Problem 185 - Number Mind
15th November 2023

**python**

Features:
 - BFS on possible solutions

Notes:
Code written in 2023/11/15
Runs in $10^{n/2}$ memory and time, where $n = 16$.
Python seems to be really bat at
For each 8 dig number, computes the number of matching chars on the left side and saves the result
For each 8 dig number, computes the number of matching chats on the right and sees it it complements well with some of the saved results

Time: 2421 seconds

---

### Problem 186 - Connectedness of a network

Features:
 - Each time a call is made we merge trees by point one root to the other root.
 - This data structure allows for a seamless union of sets.
 - We just have to remember how many elements are below a root at every time.

Time:
838.96 seconts.
For some reason the code starts to slow down once we pass 1M calls.

---
### Problem 189 - Tri-colouring a Triangular Grid
15th November 2023

**python**

Features:
 - Dynamic prgramming
 - Exponential growth optimization

Notes:
Dynamic programming allows us to compute the number of colourings of a triangle of size n by knowing colourings of size n-1
#We have to know the number of colourings that have a specific colouring on the bottom row

Time:
19.98s
N = 9 runs in 185s and gives 104224568112581443584

---
### Problem 192 - Best Approximations
23rd November 2023

**python**

Features:
 - Continued Fractions
 - Best rational aproximation

Notes:
Computes the continued fraction of all the square roots up to 100.000, this is the part that takes time
Then generates all the convergents and semiconvergents (with last entry at least half of the same entry of sqrt(n))
There is a theorem that tells us exactly which of the convergents are the ones that we want
But I just select all of them, sort and pick the closest one


Time:
78910 seconds 


---
### Problem 194 - Coloured Configurations
5th December 2023

**python**

Features:
 - Dinamic Programing
 - Chromatic number of a graph

Notes:
Recursive formula with the linear structure of the problem

Time:
16.19 ms

---
### Problem 195 - 60-degree Triangle Inscribed Circles
21st November 2023

**python**

Features:
 - Cosine law
 - Generating formula for triangles with a fixed angle

Notes:
Equilateral triangles do not count
If $a$ is the side opposing to the 60 deg angle, inradius is $\frac{b+c-a}{2 \sqrt{3}}$
Every primitive such triangle has a unique $m, n$ coprime with $a, b, c$ given below, $(m, n) = 1$ and $2n < m$

Time: 13.9 seconds

---
### Problem 196 - Prime Triplets
20th November 2023

**C++**

Features:
 - Miller Rabin

Notes:
Possible memory optimisation by sweeping the grid instead of generating it

Time: 505.325 seconds

---
### Problem 199 - Iterative Circle Packing
29th November 2023

**python**

Features:
 - Sodii circles
 - Computational geometry
 - Degree two polynomial formula


Notes:
 - inCircle is a function that given three circles, finds the smallest circle that is externally tangent to all three, if it exists
 - running this $3^9$ times computes the exact coordinates and radii of each circle
 - float errors do not avalanche because of the decimal library (prec = 10 is enough, this is a mistery)


Time:
1.86s


---
### Problem 200 - Prime-proof Squbes
6th December 2023

**python**

Features:
 - Miller Rabin
 - Prive sieve
 - Digits computation

Notes:
Fix arbitrary upper bound, $10^12$ works
Uses Miller Rabin to check primality (helped me find a bug!)
Uses sieve up to square root (upper bound/8), dont do square root (upper bound)/8.
Prime-proof and contaning contiguous substring is naive algorithm
make sure to generate squbes by using only primes with the right size, created two lists for the effect. Break when you are already above cuts 75% of time

Time:
0.302422 seconds

---
### Problem 201 - Subsets with a unique sum

**pythohn**


Features:
 - The problem starts with a very scary number of subsets of size 50. This is not the way to do
 - Define v[s][k][t] to be the number of sets of size $k$ that sum up to $t$
 - $s <= 100$, $k <= s$ and $k <= 50$.
 - This satisfies a recursive relation
 - Layer the vector v so that we only use the recursive relation on the previous value, allowing us to save up on $50$ times less memory.

Time:
204.8 seconds


---

### Problem 202 - Laserbeam
3rd October 2022

**python**

Features:
 - The number of paths with $N$ bounces is the number of pairs $(a, b)$ that are coprime such that $a+b = 2 N - 3$ and $a -b = 0$ mod $3$
 - We code a function PHI2 that runs over all elements $a < M = (N+3)/2$, compute its gcd with $M-a$, and checks if it is one
 - Dues to symmetry, we can stop at $M/2$
 - In the forum, exact formulas were found for phi2 in the case studied, where it is approximately $phi/3$

Time: 1828 seconds


---
### Problem 210 - Obtuse Angled Triangles
30th October 2023

**python**

Features:
 - Computational Geometry

Notes:
There are three types of points, the hardest ones are in the circle that are dealt with a sweeping algorithm.

Time:
14.14 seconds

---
### Problem 213 - Flea Circus
12th December 2023

**python**

Features:
 - Markov Chain
 - Expectation is the sum of the probabilities of 0-1 sum decomposition variables.
 - Power optimization for matrices
 - Marge matrix multiplication

Notes:
Computes the transition matrix between the boards after 50 jumps
#Afterwards, sums the probability that no bug will end up in this square d
This latter probability is $1 - p_{e, d}$
Possible optimization cuts time in half: the markov chain is bipartite, explore only the 2-step markov chain

Time:
592 seconds

---
### Problem 223 - Almost Right-angled Triangles I
12th December 2023

**python**

Features:
 - Divisors of a number
 - Prime sieve

Notes:
For each possible length a computes all the possible sides b, c
These satisfy $(b+c)\times (c-b) = a\times a - 1$
This means that $b+c$ is a divisor of $a \times a-1$, that satisfies some bounds, so for all $a\times a-1$ count such divisors and add everything up
Make sure to precompute the factorization of all integers < 25\times 10^6 /3 to factor $(a-1)(a+1)$

Time:
6.6 minutes


---
### Problem 226 - A Scoop of Blancmange
04th June 2024

**python**

Features:
 - Graphical plotting for intuition
 - Binary search numerical method
 - Infinite series

Notes:
To compute desired area, it computes the integral of the BM curve
Removes area of trapezoid
Adds chordal section area
Assumes that the curve intersects the circle in only two points, the second one is computed using binary search

Time:
9 mili seconds

---
### Problem 233 - Lattice Points on a Circle
1st November 2023

**python**

Features:
 - Generate partitions of a number

Notes:
How many numbers have a given factorization below a certain threshold
Use the fact that $f(N) = 4 + 4 \prod_i(1+2a_i)$ where $a_i$ are exponends of primes $p = 1 mod 4$ on the factorization of $N$.
We also include an excel that was helpful to find the pattern.

Time:
9.68 seconds

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


---
### Problem 240 - Top Dice
04th January 2024

**python**

Features:
 - Combinatorics
 - Generate partitions

Notes:
First generate all possible decreasing lists of ten integers that sum to 70
For each such list, we can place them in any of the 20 positions (divide by suitable binomial coef)
Careful that there may be some copies of the lowest term of this list in the other positions, so take care of that in the combinatorics
Precompute factorials
Function "PermutationOfLists" gives the number of different lists that are permutations of a given list
Function "ExtentionPermutations" computes, for a given list, the number of ways of filling out all 20 positions with this list and weakly lower numbers
Possible improvements:
 - Precompute binomials

Time:
0.582 seconds


---
### Problem 247 - Squares Under a Hyperbola
18th December 2023

**python**

Features:
 - Priority queue
 - Computational geometry
 - Quadratic formula

Notes:
Observe that there is a bijection between squares and finite strings of two characters "U" and "R"
This bijection behaves very well with the index: the tindex of a string is the pair of occurrences of "U" and "R"
We generate all the strings with 3 "R" and 3 "U", compute the side length of each of the corresponding squares
The smallest such square serves as a limit to stop the search
For the search, we use a priority queue to only expore a square when no larger square exists


Time:
4.39 s


---
### Problem 248 - Euler Totient Function Equals 13!
11th January 2024

**python**

Features:
 - Euler Totioent function
 - Divisors function
 - Cartesian product
 

Notes:
This function finds all the numbers $n$ that have $\phi(n)$
Uses the fact that if $\phi(n) = N$, then $\prod_i \phi(p_i^{a_i}) = N$ is a factorisation of $N$
So we generate all factorisations of $N$ and for each factor we find all the ways of writting it as $\phi(p_i^{a_i})$ for some prime $p_i$ (called Euler decs).
An optimization implemented is that we only generate factorisations using factors that do accept some called Euler dec.
Do not forget that $1$ can also be a factor in the factorisation. We only need to include this factor once because there is only one Euler dec that interests us.
Function DCPPrime
   Computes how many ways we can write a number $k$ as phi of a prime number. That is $k = p^a - p^{a-1}$
   The case $p = 2$ has to be dealt separately
   For each possible exponent $a$ we know $p$ is close and larger than $\sqrt[a]{k}$. We hope it's precisely the ceiling
   We use Miller Rabin for primality test
Function Product Partitions
   Computes all factorisations, different ways of writting a number $N$ as a product of different numbers
   It accepts a dictionary, and we will ignore all factors that are keys in this dictionary
Function AllAreDistinct, DeleteCopies, CartesianProduct manipulate lists
Function FromPrimeFactToNum converts a prime factorisation into the number it represents
   Example [[2, 3], [3, 1]] -> 24
Function ListNumPhiIsN is the meat of the code. For an input $N$ creates all numbers $n$ such that $\phi(n) = N$.
   For each possible factorisation where each factor can be written

Time:
12.88 seconds

---
### Problem 249 - Prime subset sums
08th January 2024

**python**

Features:
 - Exponential constructions
 - Dynamic programming
 - Sums of sests with bounded size
 - Primes sieving

Notes:
The code generates a list sprimes, such that sprimes[i] = number of subsets with sum i
The way this generation is done is fast because we only record the number of such sums, which allows this to have size |sprimes|*maxsum ~ 1000 * 1M
We add all the values of this list for prime indices buy sieving a larger set of primes
We could use MillerRabin instead, but I found an error in my MR code so I will need to take care of that

Time:
48.72416 seconds


---
### Problem 258 - A Lagged Fibonacci Sequence
12th December 2023

**C++**

Features: 
 - Fast exponentiation
 - Matrix form of recursive formulas

Notes:
This sequence can be computed by powering a $2000 \times 2000$ matrix $10^{18}$ times
We use a log complexity algorithm for that matrix power, and make sure all the multiplications are done module 20092010
There seem to be two imediate impovements ( found on the forums )
 - First is to compute twice module the two factors $~10k$ of $20092010$ and use chinese remainder theorem
 - The second is to compute $A^k$ for $k = 0, 1, ..., 1999$ and using Cayley hamilton $A^2000 = A+Id$
The forums also invented a great optimization. The matrix $A^k$ can be easily computed only knowing the last column, so we just compute this last column and that's it
This reduces the complexity to $k^2 \log n$, which allows us to have solutions that run under a minute
We also include a first attempt of coding this with python that took way too long.

Time:
67906 seconds

---
### Problem 259 - Reachable Numbers
26th October 2023

**python**

Features:
 - Binary trees

Notes:
Creates all binary planar trees with all possible five operations (including concatenation) in internal nodes
We do not allow for internal nodes to have concat when some child is not concat
Because of division, we have to check if a number is "close" to an integer
Make sure that when saving a key to the dictionary, we save the integer (so we dont double count)

Times:
476s (8 minutes)
---
### Problem 260 - Stone Game
04th January 2024

**python**

Features:
 - Brute Force
 - Game theory
 - Memoisation

Notes:
This is a simple brute force program and memoisation.
For each losing strategy, we can determine that all states that reach this point are winning strategies
So run increasingly in the amount of stones in a pile, when finding a losing strategy mark all coresponding winning strategies
Possible optimizations:
 - just run for a <= b <= c, would get a *6 improvement. 
 - Use C++, would get a 10* improvement
 - Cap the loop on k to the maximum value automatically, would get a *2 improvement

Time:
780 seconds


---
### Problem 266 - Pseudo Square Root
05th January 2024

**python**

Features:
 - Split in the middle
 - Binary search
 - Prime sieving

Notes:
Generates all primes, splits the set of primes in two and computes all the products of primes in each set (of size 21, so there are about 2M products)
Sort each set. For each product p of the first prime set, find largest product q of the second prime set that does not exceed an upper bound
This bound is cooked up so that $p\times q \leq \sqrt{product of primes}$
This search uses binary search.

Time:
14.7169032 seconds


---
### Problem 276 - Primitive Triangles
28th November 2023

**python**

Features:
 - Moebius inversion formula

Notes:
There is the following formula $F(n) - F(n-1) = \sum_{d|n} mu(n/d) G(d)$ according to OEIS A051493

Time:
19.13 seconds



---
### Problem 281 - Pizza Toppings
10th January 2024

**python**

Features:
 - Euler Totient function
 - Burnside's lemma
 - Combinatorics of set partitions

Notes:
Burnside lemma says that the number of orbits of a group action is given by a simple sum.
In this case, the set of pizza toppings $X_{m, n}$ has an action of the cyclic group $C_{mn}$, we wish to count $X_{m, n}/_{C_{mn}}$
Burnside's lemma predicts that $|X_{m, n}/_{C_{mn}}| * |C_{m n}| = \sum_{g\in C_{mn}} |X_{m, n}^g|$. $|X_{m, n}/_{C_{mn}}|$ is the number that we are after.

Counting $|X_{m, n}|$ is easy with a combinatorial argument. 
    Labelling all the different toppings we count $(mn)!$ topping distributions of $mn$ toppings,
    but permuting each subset of toppings that have the same flavour gives a class of size $n!$ topping distributions that we consider the same
    so $|X_{m, n}| = \frac{(mn)!}{(n!)^m}$
To count the size of the stabilizer, let $e$ be the rotation given by $\frac{2 \pi}{mn}$, a generator of $C_{mn}$, and $g = e^k$.
A pizza topping is stabilized by $g$ if and only if it is stabilized by $e^{gdc(k, mn)}$. Let $d = gdc(k, mn)$.
Because of the stabilizer property, there are $d$ groups of slices, each of size $t = mn/d$, that have the same topping.
Counting such toppings is equivalent to counting
   the number of topping distributions with $m$ different toppings on $d$ slices,
   where we want each topping to be in $d/m = n/t$ different slices. 
Thus $t$ has to be a divisor of $n$, in which case the number is $|X_{m, n/t}| = \frac{(mn/t)!}{((n/t)!)^m}$
We get the following formula for $f(m, n) = \sum_{t | n} \sum_{k = 1, \ldots , mn :  gcd(k, mn) = mn/t} |X_{m, n/t}|$
Finally, we note that the number of indices $k = 1, \ldots , mn$ for which $gcd(k, mn) = mn/t$ for a fixed $t$ is $\phi(t)$
   as these are given by $k = mn/t \times z$ where $z\perp t$ is an integer in $1, \ldots t$.

A note on finding the upper bound. We know that $f(m, 1) = m!$, so we do not need to explore any $m >= 20$

Time:
Runs in 3 ms



---
### Problem 285 - Pythagorean Odds
4th January 2024

**python**

Features:
 - Computational Geometry
 - Circle section area formula
 - Triangle area formula
 - Quadratic formula
 - Probability as areas

Notes:
Sampling a and b is sampling a point in the unit square
The probability is the area of this square intersected with an anular region
Compute numerically for each k the angle of the circular sections, minus a triangle, gives the desired area

Time:
4.320313692 seconds

---
### Problem 286 - Scoring Probabilities
4th January 2024

**python**

Features:
 - Dynamic programing
 - Binary search

Notes:
DP to fing the probability of hitting 20 shots for a given q
Binary search to find que desired q
Note that Shot(50) = 0.04 and Shot(100) << 0.02, so we only need to do binary search there
The function is decreasing in this part, so binary search will be adapted accordingly

Time:
0.11953878402 seconds

---
### Problem 287 - Quadtree Encoding (a Simple Compression Algorithm)
14th December 2023

**python**

Features:
 - Computational Geometry
 - Simulation
 - Brute force

Notes:
This just emulates the split for each quadrant
People seem to find is faster to run a C program than a python on the forums.

Time:
331 seconds



---
### Problem 291 - Panaitopol Primes
16th January 2024

**python**

Features:
 - Miller Rabin

Notes:
The panaitopol primes are precisely the ones of the form $n^2 + (n+1)^2$
I dont even know why, just found that fact on the internet
We search for $n$ until $~50M$, and use Miller Rabin


Time:
592 seconds

---
### Problem 300 - Protein Folding
3rd November 2023

**python**

Features:
 - Graph theory
 - Comuting all cases

Notes:
Generates all possible non-self intersecting paths
We are only interested in the pairs of cells that are adjacent, so we delete paths that repeat this feature
This takes care of rotations and reflections, as well as paths that look different but have the same connections
For each protein and path, we compute the number of bounds, and the average of the best is the answer
Possible optimizations: the number of bounds of a protein on a path is the
 - same as the number of bounds of the reverse protein in the reverse path, this cuts time in half
 - stop considering a protein when it has already gotten the maximal nubmer of bonds

Time: 255 seconds




---
### Problem 303 - Multiples with small digits
16th January 2016

**python**

Features:
 - Prediction of values from smaller cases

Notes:
We generate all the numbers with digits $0$, $1$, $2$.
For each such number, we see if it is a multiple of one of the numbers between $1$ and $10000$
We regularly shrink the list of missing numbers, so numbers that have a low 012 multiple are not hindering further computations.
On a second run where I use the fact that $\frac{f(9999)}{9999} = 1111333355557778$  (this can be guessed by the values of $999$, $99$ and $9$)


Time:
Runs in 2745.782 seconds without predicting the value of $9999$
Runs in 33.9 seconds with prediction

---
### Problem 304 - Primonacci
7th Dezember 2023

**python**

Features:
 - Miller Rabin
 - Super divide function

Notes:
For each power of prime that superdivides the module, we compute the remainder
This is done by computing the period of fibbs over each prime power, because there are no prime powers larger than 630_803, the period is of the order of milions
Primes generated by MillerRabin

Time:
11.77 seconds


---
### Problem 307 - Chip defects
04th June 2024

**python**

Features:
 - Rational structure
 - Combinatorial formula

Notes:
We compute the complementary probability, that is that all chips have at most two defects.
By separating all defect distributions according to the number of chips, we get a formula.
Specifically, if we compute the probability that exactly $m$ chips have one defect and $l$ chips have two defects, 
with $k = m + 2l$, we get that the answer is $1 - \frac{k! \sum_{l = 0}^{k/2} \binom{n}{l} \binom{n-l}{k-2l}2^{-l}}{n^k}$.



Time:
179.227 seconds


---
### Problem 332 - Spherical Triangles
21st December 2023

**python**

Features:
 - Spherical geometry
 - Area of a triangle
 - Computational geometry

Notes:
    For each integer vector in a 100x100x100 cube see if it has a ninteger distanc to the origin
    If so, save it on the corresponding slot
    For each slot, generate all triangles and compute the area
    Area is given by Girard's theorem, that says the area of a triangle is given by the sum of its angles
    We actually compute the angle between the normals, which gives the complementary angle

Time:
    1107.95 seconds


---
### Problem 325 - Stone Game II
8th November 2023

**sage**

Features:
 - Game theory
 - Integer points in a polyhedron

Notes:
    The set of losing positions are the integet points $(x, y)$ such that $x\neq y$ that are inside the cone $x/phi < y < x*phi$
    The desired sum can be extended to counting the number of integer points inside a 3 dimentional polytope
    We compute this polytope here, runs in very few time. Afterwards we need to use sage to compute the number of integer pts

Time:
5.084355 seconds

---
### Problem 348 - Sum of a Square and a Cube
5th Dezember 2023

**python**

Features:
 - Palindromes
 - Dictionary

Notes:
    Fixed an arbitrary limit and computed all the sums of squares and cubes up to this limit
    Memorised these sums in dictionaries to count occurrences
    Limit set to $10^9$ magically words

Time:
27.26 seconds


---
### Problem 349 - Langton's ant
4th June 2024

**python**

Features:
 - Simulation

Notes:
Simulates the ant progress until we spot a pattern that happens after 10k steps.
Modular arithmetic to compute the case for $10^{18}$

Time:
4 seconds

---
### Problem 371 - Licence Plates
23rd October 2023

**python**

Features:
 - Aproximation of a binomial to a poison distribution.
 - Markov chain

Notes:
    First assumption that there are infinitely many licence plates and all of them exist infinitely many times
    This problem can be modeled with a markov chain, on $1+500\times 2$ states, and we want to compute the exit time from the $500 \times 2$ transient component.
    This component happens to be upper triangular, so invertion is specially easy an ddoes not need Gaussian elimination.


Time:
2.21 ms

---
### Problem 425 - Prime Connection
7th Dezember 2023

**python**

Features:
 - BFS
 - Priority queue
 - Prime 

Notes:
    BFS on the graph constructed in the problem, where the BFS is done with a priority queue
    We want to visit the lowest neighbour that we havent visited yet
    We check all the neighbours that we have not visited, add them to queue
    Remember how high is the number where you came from (largest in the whole path)


Time:
59.75 seconds


---
### Problem 435 - Polynomials of Fibonacci Numbers
7th Dezember 2023

**python**

Features:
 - Super divides function
 - Fibbonacci periods

Notes:
    We compute each $F_n(x) mod p^e$ separately for each power divisor of $15!$
    Note that each power divisor of $15!$ will not be larger than $2500$, so the fibonacci period will not be larger than $2500^2$
    We use the fact that fibbs is periodic as well as the powers are periodic to compress the sum as much as possible, will be the size at most $2500^2$

Time:
0.1493 seconds


---
### Problem 443 - GCD sequence
15th February 2024

**python**

Features:
 - Prime factorisation
 - Sequence compression

Notes:
We note that the sequence has a lot of consecutive numbers.
We can find the size of each subsequence of consecutive numbers.
These runs depend on the primes dividing $g(n-1) - n$.
Specifically, for each such divisor prime $p$, the current run of consecutive numbers can only go on for $p - 1 - (n - 1)%p$ terms before a large step.
Looping over all primes that divide $g(n-1) - n$, we can find the size of this run and artificailly jump it.

Time:
Runs in 427 seconds, much of which is generating all primes up to $10^8$


---
### Problem 461 - Almost Pi
2023/12/14

**python**

Features:
 - Split-in-the-middle algorithm
 - Decimal package
 - Binary search

Notes:
Computes all possible sums of two terms that are below PI
Sorting this list of sums, for each term $t$ we find the numbers that are close to $\pi-t$ and check if these improve our current best
Make sure to use binary search for checking values.
In total there are $L\times 1.5$ integers to test in the function, and so the list will not have more than $n = 2.25\times L^2$ terms.
Sorting takes $n \log n = O(L^2 \log L)$ and binary search takes $O(\log n) = $O(\log L)$, so the whole algoritm takes $O(L^2 \log L)$ complexity.

Time:
5 minutes



---
### Problem 485 - Maximum number of divisors
15th February 2024

**python**

Features:
 - Union of intervals structure
 - Binary search
 - Divisors by sieving

Notes:
We start by computing the number of divisors of all numbers up to $10^8$.
We should not proceed with the naive attempt of computing the maximum of each sublist, this has about $10^{11}$ operations.
However, we sort the numbers according to the number of divisors, and starting with the one with most divisors, we keep track which sublists have this element.
This entails an object that is the union of intervals of size $10^5$.
Other possible solutions are Range minimum query and deque.
Most of the time is spent on the sieve of divisors, which can be sped up by using the multiplicativity property and I was a bit lazy to compute it

Time:
204 seconds

---
### Problem 531 - Chinese leftovers
12th Feb 2023

**python**

Features:
 - Chinese remainder theorem defined iteratively and using extended gcd
 - Precomputing euler phis and factorizations of all numbers between $10^6$ and $10^6+5000$

Time: 147s



---
### Problem 555 - McCarthy 91 Function
29th May 2024

**python**

Features:
 - Triangular formula
 - Recursion
 - Divisors iteration

Notes:
Recursive formula can be show to satisfy, for $n \leq m$, that $M_{m, k, s}(n) = n - s + (k-s)(q + 1)$ where $q = \lfloor\frac{m-n}{k-s} \rfloor$
With this we can show what the fixed points of $M_{m, k, s}$ are 
If $s-k|s$, they are precisely $m-2s+k-i$ for $i=0, \ldots, k-s-1$.
Otherwise there are no fixed points
Summing all these up gives us the formula $SF(m, k, s) = \frac{l(2(m-s)+l+1)}{2}$, where $l = k-s$ divides $s$
Further grouping the sum over all $s$ and using triangular forumla gets us, if we set $q = \lfloor\frac{m-n}{k-s} \rfloor$, that
$$S(m, p) = \sum_{l=1}^p \frac{1}{2} (q-1)(l(l+1) + 2lm - l^2q) $$
Further improvements can be done because this sum is a triangular sum with using $l = q*p+r$ and iterating over $a$ and $r$.

Time:
0.13 seconds



---
### Problem 571 - Super Pandigital Numbers
30th May 2024

**python**

Features:
 - Permutation iteration
 - Digits base

Notes:
We assume that the first 10 such numbers have exactly 12 digits base 12
This is the munumal amount of digits such a number may have
We iterate over all permutations of the 12 distinct digits base 12
The iteration preserves the order of the underlying numbers
For each permutation, convert to all bases < 12 and check if the condition is satisfied.
Clue from forums: check the pandigital in each basis in reverse order, fails earlier and runs faster

Time:
4715 seconds


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
 - There are 20 fibonacci numbers <= 10k and there are $50 + 2\times 20 = 90$ relevant steps in a $10k x 10k$ grid
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
 - Dynamic programming on a $2^{12}  \times  30$  grid
 - DP[n][word][b1, b2, b3, b4] is the number of words of length n that end in word, and have an occurrence of the desired strings or not, according to b1, ..., b4

Time:
0.536 seconds for $LIM = 30$


---
### Problem 705 - Total Inversion Count of Divided Sequences
27th May 2024

**python**

Features:
 - Recursion
 - Aristothenes sieve

Notes:
For a string $S$ of non-zero digits, let $N(S)$ be the number of divided sequeces obtained from $S$.
For a digit $a$, let $div(a)$ be the number of divisors of $a$, and let $1(r|a)$ be the indicator function of $r|a$, that is it is $1$ precisely when $a$ is a multiple of $r$, and is zero otherwise.
Define as well $L_r(S)$ to be the number of digits $r$ on all divided sequeces obtained from $S$.
Finally, define $F(S)$ to be our target number, the total inversions done on all divided sequeces obtained from $S$.
We have the following recursive formulas
$$N(Sa) = N(S) \cdot div(a)$$
$$L_r(Sa) =  L_r(S) \cdot div(a) + 1(r | a) \cdot N(S)$$
$$F(Sa) = F(S)\cdot div(a) + \sum_{b|a} \sum{c > b} L_c(S)$$


Time:
150 seconds, 8 of which is to compute the prime numbers



---
### Problem 706 - 3-Like Numbers
25th October 2023

**python**

Features:
 - Dynamic programming
 - Combinatorics on the number of integerst with digits satisfying certain properties

Notes:
Dinamical programing on the number of sequences with a given number (mod 3) of subsequences with a specified sum (mod 3) and sufixes

Time:
76.1 seconds

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

### Problem 731 - A Stoneham number
09th Feb 2023
**python**

Features:
 - We can trim the sum to $33$ terms, as any term afterwards will not contribute to the decimal places at hand
 - Let $a_j^i$ be the $j$-th digit after the decimal point of $3^{-i}$. This satisfies the formula $a_j^i = (10^[j-1}%3)//3^i$
 - Use powermod for fast exponentiation

Time: 0.0161s

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
### Problem 757 - Stealthy numbers
24th May 2022

**python**

Features:
 - Zeores of a degree two polynomial. If $(x-a)(x-b) = x^2 - F'x + N$ and $(x-c)(x-d) = x^2 - Fx + N$, these polynomials have integer solutions and $F + 1 = F'$
 - Integer solutions of quadratics means $F^2 - 4N$ is a square $x^2$ and $(F+1)^2 - 4N = y^2$
 - $x$ and $y$ satisfy $0 < x < y - 1$ and $x = y + 1 mod 2$, are integers
 - Given $x, y$ we have $4 N = (y^2 - x^2 - 1)^2 - x^2$
 - We can find all $N$ that satisfy an equation of this type by checking all $x, y < \sqrt{N}$
 - This may look $O(N)$ but for each $N^{1/4 + eps} < y < \sqrt{N}$ we just need to run x until a bound that only depends on epsilon, so complexity is $O(N^{1/4+1/2})$

Time:
100 seconds in UZH server


---
### Problem 772 - Balanceable k-bounded partitions
28th May 2022

**python**

Features:
 - Answer is lcd(1, ..., k) * 2. This can be computed by computing all the primes smaller than k
 - It is easy to observe that $2j$ should divide $f(k)$, because if $n = 2 j \times  m + r$, for $r < 2j$, the following partition $j + ... + j + r$ is not balanceable.
 - It turns out that all these partitions cover all $n < 2 lcd(1, ..., k)$
 - Algorithm can be sped up with fast primality test like miller rabbin, instead of sieving.

Time:
56s for $LIM = 10^8$


---
### Problem 776 - Digit Sum Division
18th October 2023

Features:
 - Combinatorics on the number of integerst with digits satisfying certain properties
 - Dynamic programming

Notes:
One uses two auxiliary functions that compute data recursively
Compute function that counts $\# {0 < n < 10^M | s(n) = k}$ and $\sum_{0 < n < 10^M} 1(s(n) = k)$


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
$$ \sum_{K\geq 1} f_K = \sum_i \left( \prod_{j < i} \frac{p_j-1}{p_j} \right) \frac{1}{(p_m)^2p_m}$$
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

$$\sum_{u=0}^{} \zeta(u)\left[ \binom{LIM + 1}{u + 1} - \binom{2u - 1}{u + 1} \right] $$

Here we are using $prod = [1, 9, 9\times 9, 9\times 9\times , 9\times 9\times 8\times 7, ...] representing the choices of digits that we have for each block
$$ \zeta(u) = \sum_{\lambda \vdash [u] } prod( \ell(\lambda )) $$

Time:
0.89s after optimization


---
### Problem 793 - Median of Products
25th October 2023

**python**

Features:
 - Binary search

Notes:
Through binary search: given a value K, we compute how many products are <= K
This function itself works by running n binary searches, so the complexity is nlog(nlog(n))

Time:
165s

---
### Problem 804 - Counting Binary Quadratic Representations
1st July 2022

**python**

Features:
 - Counting integer points inside an algebraic curve

Time: 
15s


---
### Problem 810 - XOR-Primes
**C++**

Features:
 - Prive sieve

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
### Problem 816 - Shortest distance among points
09th Feb 2023

**python**

Features:
 - Two programs were created: one with the typical shortest distance among points and a naive adaptation.
 - Typical program does binary search on the x coordinate and in the interface between the division it compares all points. Surprising classical fact is we only need to check distances between at most $7n$ points.
 - Naive adaptation splits the plane into $m^2$ tiles and we only need to check distances between points on the same or adjacent tiles.
 - Points **do start repeating** before $d < 4 10^6$, but this is below the bound requested

Time:
 123s for classical program
 34s for naive adaptation

-- 
### Problem 820 - Nth digit of reciprocals
10th Feb 2023

**python**

Features:
 - Use the same formula as problem 731 (Stoneham number) for the nth digit of areciprocal of x: $d_n(1/x) = (10^{n-1} % x)10 // x$
 - Use fasat exponentiation and powermod

Time:
78s

---
### Problem 822 - Square the Smallest
10th October 2023

**python**

Features:
 - Decimal package
 - Tiro's method and binary search

Notes:
We work over the double log of the numbers
By guessing an answer, we can compute easily how many steps it takes to get to this answer and check if we are above or below
Uses very high precision
A conde that doesn't work is also presented in C++

Time:
67s

--
## Problem 828 - Numbers Challenge
10th Feb 2023

**python**

Features:
 - A sequence of operations is a triple: a binary tree with n internal nodes, a list of n operations and a list of $n+1$ values.
 - Given list of values, generate all ~200 trees of size at most seven, for each size $n+1$ generate an arrangement (combination + permutation) of the values of size $n$ ( ~ $7!$ ) and a list of $n$ operations $=4^n$.
 - Worse case scenario this gives at most $7\times 10^{12}$ operations (rough)
 - Check if arrangement at hand minimizes sum before testing with all operation lists and trees

Time: 5000 seconds

---
### Problem 834 - Add and Divide
7th October 2023

**python**

Features:
 - Prime sieve
 - Divisors

Notes:
Uses the fact that $n+m$ has to be a divisor of $n*(n-1)/2$
Precomputes all the prime factorizations of numbers below $1234567$

Time:
40s


---
### Problem 839 - Beans in Bowls
31st May 2024

**python**

Features:
 - Binary search
 - Divide and conquer

Notes:
The order in which the operations are performed is irrelevant, as long as we always topple beans to the right when the left pile is higher
Divide and conquer method: we perform the toppling process on each half of the array independently
Then we perform a last avalanche from the left half to the right half
For that, we do a binary search to figure out what is the height in the middle after the avalanche
We can see if this height is enough or not in linear time, so complexity of job is $n \log n$

Time:
165.09 seconds


# Code written on the 2024/05/31


---
### Problem 845 - Prime Digit Sum
10th October 2023

**python**

Features:
 - Inclusion-exclusion

Notes:
Use F(M, a)= number of positive integers n < M with digit sum = a
This code is very efficient, using the inclusion-exclusion trick for powers of 10, plus iteration over all digits
Highly dependent on the bigInt structure of python
Make sure to use integer division from python
Includes partial code of C++ that is not able to deal with the task because of the lack of big int libraries

Time:
< .5s
Runs in 1s for 10**24, answer = 4992807761953432073250229
Runs in 2s for 10**30, asnwer = 5590371034358585932162729926235

---
### Problem 853 - Pisano Periods 1
17th November 2023

**python**

Features:
 - Prime sieve
 - Fibbonacci periods

Notes:
Computes pi(p) for every prime below 10**9, for those that divide 120 includes the respective powers
Use the fact that $pi(mn) = lcm(pi(m), pi(n))$ if $m, n$ are coprime
Includes C++ code that does not work

Time:
26s


---
### Problem 860 - Gold and Silver coin game
7th May 2024

**python**

Features:
 - Modular optimisation
 - Binomial coefficients
 - Hackenbush calculus
 - Combinatorics

Notes:
A major optimisation of this code is that we only want the computation to be done modulo $989898989$, this saves us big int computation time.
There are only four types of piles, and the number of each type of pile must satisfy two equations.
One is because there are in total $9898$ piles.
The other is because the game is only fair if the sum of scores of all piles is zero (Hackenbush theory).
The score of GG is $4$, SG is $1$, GS is $-1$ and SS is $-4$.
For each possible configuration we also multiply by the appropriate multinomial.
Precomputing the binomials is the most efficient chice and happens in less than one second.

Time:
10 seconds

---
### Problem 862 - Larger Digit Permutation
22nd February 2024

**python**

Features:
 - Partition generation
 - Combinatorics

Notes:
Each $k$-digit integer corresponds to a partition of $k$, by grouping similar digits.
For instance to 312313312 corresponds to the partition $(4, 3, 2)$.
We will place the zeroes in a special position, so we define the partition signature of a number as the pair of the partition of the non-zero digits, together with the number of zeroes.
For instance to 312313002 corresponds to the signature $(2, (3, 2, 2))$.
For each signature we can compute the size of the permutation set of any given number with this signature.
    If this signature $(a_0, (a_1, \ldots, a_j))$ is of a $k$ digit number, this number is $\binom{k}{a_0, \ldots, a_j} - \binom{k-1}{a_0-1, a_1, \ldots, a_j}$.
For each signature we can compute the number of integers with the specific signature, divided by the size of the cycles.
    If this signature $(a_0, (a_1, \ldots, a_j))$ is of a $k$ digit number, this number is $\binom{k}{b_1, \ldots, b_j}$, where $b_l$ is the number of distinct $l$ in $(a_1, \ldots, a_j)$.
The final answer is 
$\sum_{(a_0, (a_1, \ldots, a_j))} \left( \binom{k}{a_0, \ldots, a_j} - \binom{k-1}{a_0-1, a_1, \ldots, a_j} \right) \times \binom{k}{b_1, \ldots, b_j}$


Time:
2ms

---
### Problem 866 - Tidying up B
14th May 2024

**python**

Features:
 - Dynamic programming
 - Markov chain

Notes:
Looking at the process backwards we see that the last step always contributes with $n(2n - 1)$ to the final value.
Furthermore, conditioning on the event that the last piece $L_{n, n}$ that was found has index $i$, it merges two independent processes of size $i-1$ and $n-i$.
This gives the recursive formula for the final score $P_n$ of the process to be
$$ P_n = \sum_{i=1}^n \mathbb{P}[L_{n, n} = i] n(2n-1) P_{i-1} P_{n-i}$$
Taking the expectation on both sides and using independence, as well as noticing common terms, we get
$$ P_n = (2n-1) \sum_{i=1}^n  \mathbb{E}[ P_{i-1} ]\mathbb{E}[ P_{n-i} ]$$


Time:
0 miliseconds


---
### Problem 868 - Belfry maths
22nd February 2024

**python**

Features:
 - Permutations
 - Recursion

Notes:
The order can be computed recursively, as the largest element moves in a predictable pattern, whereas the rest moves along the rule as if the other element were not there
Let $l$ be the length of the string, $p_1$ be the position of the string after removing the largest element, and $p_2$ the position in the string of the largest element.
If $l$ is even, the desired position is $l\times p_1 + l - 1 - p_2$, and if $l$ is odd, the desired position is $l\times p_1 + p_2$.

Time:
10 ms



---
### Problem 869 - Prime Guessing
16th May 2024

**python**

Features:
 - Recursion
 - Miller Rabin
 - Tree encoding of binary numbers

Notes:
Obtain the first $10^8$ primes using Miller Rabin.
We create a binary tree structure where each prime corresponds to a unique node, whose path to root corresponds to its binary expansion.
In this way, going through the game is going through the tree from the root until a randomly choosen prime.
The optimal strategy is to pich the side of the tree with more primes, which is what we compute in bt.score()

Time:
70 seconds

---
### Problem 872 - Recursive Tree
3rd May 2024

**python**

Features:
 - Recursion
 - Trees
 - Digits
 - Binary expansion

Notes:
Simple obesrvation after switching all labels from tree T_n from k to n-k, shows that a path from a number to the root is related to binary expansion.

Time:
2 ms


---
### Problem 874 - Maximal prime score
22nd May 2024

**python**

Features:
 - Knapsack
 - Sieve prime numbers

Notes:
First the map $p$ is increasing, so increasing the value of $a_i$ will increase the score.
This tells us that the optimal list has sum $maxsum - (maxsum \% k)$.
By flipping $b_i = 6999 - a_i$ we are trying to find a list $b_1, \cdots b_n$ that sums up to $maxsum \% k$ and minimizes $\sum_i prime(6999)-prime(6999-b_i)$.

We switch to a maximization problem by flipping the sign, which gives us a knapsack problem: we have a bag with $maxsum \% k$ size, and there are items with volume and weight $(i, prime(6999-i)-prime(6999))$ that can be fit into the bag.

Time:
1.08 seconds


---
### Problem 877 - XOR Equation A
8th May 2024

**python**

Features:
 - Binary expansion
 - Polynomial ring
 - Vieta jumping

Notes:
The mathematical details will not be found here, because I don't understand why this is true.
But we will get halfway there. First observation is that XOR sum and XOR product are simply the ring operations in $\mathbb{Z}_2[x]$.
In this way we are solving the equation $a^2 + x a  b + b^2 = 1 + x^2 $.
Observe that for any such solution $(a, b)$, we also have the solution $(xb + a, b)$, so by starting with the solution $(0, 3)$ we can generate a family of solutions.
By trial up to $N < 10000$ we can observe that these solutions are actually all solutions of this equation for small values.

Time:
0 ms


---
### Problem 881 - Divisor Graph Width
23rd May 2024

**python**

Features:
 - Divisor lattice
 - Partitions

Notes:
The number of elements in each level can be computed with the convolution product of lists.
The product of the first 16 primes already has a level with $\binom{16}{8} > 10000$ elements, so we only need to test numbers with fewer than 16 prime divisors.
We assume that the best partition does not have avy $p^8$ factor for simplicity, this seems to have worked.

Time:
0.2 seconds


---
### Problem 884 - Removing Cubes
24th May 2024

**python**

Features:
 - Recursion
 - Rounding error precision
 - Triangle formula $T(n) = n(n+1)/2$

Notes:
The solution revolves around the following recursion
$S(n) = S(c)q + T(q-1)c + qr + S(r)$
Where $c$ is the largest perfect cube $c\leq n$, and $n = c*q+r$ is the division algorithm quoficients.
We precompute the value of $S(n)$ for cubes and memorise these, achieving a complexity of $O(n^{2/3})$.
We need to be careful with rounding errors, as $floor(64**(1/3)) = 3$ in python.

Time:
1.352 seconds

# Uses recursive formula: if $n$ is an integer and $c$ is the largest $c \leq n$ perfect cube
# let $r = (n%c)$ and $q = n//c$
# then $S(n) = S(c)q + T(q-1)c + qr + S(r)$
# We precompute $S(c)$ for perfect cubes using the previous values of lower cubes
# Careful with rounding errors when computing largest perfect cube below n

---
### Problem 885 - Sorted Digits
24th May 2024

**python**

Features:
 - Partitions
 - Combinatorics

Notes:
Generates all numbers of up to 18 digits using digits from 0 to 9 in a sorted manner
These are just partitions of lenght at most 18 with parts $\leq 9$, and there are about $\binom{18+9}{18} \sim 5 \cdot 10^6$
For each such number $d$, count how many numbers of at most 18 digits will be mapped to $d$ after reordering
This is a simple factorial product

Time:
28.26 seconds

---
### Problem xxx - PROBLEM NAME
dayth Month YYYY

**language**

Features:
 - Feature 1
 - Feature 2

Notes:
Note 1

Time:
x seconds


