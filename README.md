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
 - 10.5s to run until 10^12

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


