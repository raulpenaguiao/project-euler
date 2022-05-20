# project-euler
This is where I will leave the code related to project euler



### Problem 122 - Efficient exponentiation

Features:
 - An exponentiation sequence is an *additive* sequence
 - BFS over all possible additive sequences that satisfy some lax inequalities
 - Runs in less than 20 seconds for < 190
 - Runs in 8 min < in UZH computers for m = 200

Bugs:
 - Memory goes bust for m > 190 in a laptop!

### Problem126 - Cuboid layers

Features:
 - Formula for layer of cuboid computed with tuple f
 - Priority queue to cycle over all tuples
 - Search on the space of tuples is tree-like, so there is no repeated computations
 - Queue search limited in scope for protection
 - Priority is set by the value of f, so when we reach a tuple that has some specific value, all tuples with lower values have already been visited

Time:
 - 27.75s to run for n = 1000





