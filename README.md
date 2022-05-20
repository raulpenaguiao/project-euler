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



