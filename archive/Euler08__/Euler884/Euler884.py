# Code written on the 2024/05/24
# Uses recursive formula: if $n$ is an integer and $c$ is the largest $c <= n$ perfect cube
# let r = (n%c) and q = n//c
# then S(n) = S(c)*q + T(q-1)*c + q*r + S(r)
# We precompute S(c) for perfect cubes using the previous values of lower cubes
# Careful with rounding errors when computing largest perfect cube below n
# Runs in 1.352 seconds


import time
start = time.time()
from math import floor, ceil

def T(n):
    return n*(n+1)//2


def CubeRoot(n):
    c = n**(1/3)
    cf = floor(c)
    cc = ceil(c)
    if cc**3 > n:
        return cf
    return cc


def S_with_cubes_list(n, lst_cubes):
    if n <= 1:
        return 0
    c = CubeRoot(n)
    c3 = c**3
    swc_below = S_with_cubes_list(n-c3, lst_cubes)
    return lst_cubes[c] + swc_below + n-c3


def S_first_cubes(LIM):
    c = CubeRoot(LIM)
    lst_cubes = [0, 0]
    for i in range(2, c+1):
        cube_m1 = (i-1)**3
        cube = i**3
        r = cube%cube_m1
        q = cube//cube_m1
        nVal = lst_cubes[-1]*(cube//cube_m1) + (cube_m1) * T(q - 1)
        nVal += r * q + S_with_cubes_list(r, lst_cubes)
        lst_cubes.append(nVal)
    return lst_cubes



L = 10**17
print("Answer = ", S_with_cubes_list(L, S_first_cubes(L)))
end = time.time()
print("Time elapsed ", end - start, " seconds")