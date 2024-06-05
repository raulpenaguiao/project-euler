#Code written on the 2024/01/16
#First compute the order of 10 module 23. It turns out 10 is a primitive root so the order is 22
#We will compute all possible sums of 23 of these 22 powers of 10, that add up to a multiple of 23
#For each such possible sum (encoded in a 22-tuple) we will distribute these powers of 10 according to 
#Runs in 


import time
start = time.time()
base = 10
num = 23
LIM = 11**12

powers = [base]
ord = 1
#Compute order of 10 mod 23
while( powers[-1] > 1):
    ord += 1
    powers.append((powers[-1]*base) % num)
powers = [1] + powers[:-1] #we don't want the last entry


#Precompute binomials up to lim. May be necessary
lim = 200
binom = [[0 for _ in range(lim+1)] for _ in range(lim+1)]
for i in range(lim + 1):
    binom[i][i] = 1
    binom[i][0] = 1
for n in range(1, lim + 1):
    for i in range(1, i):
        binom[n][i] = binom[n-1][i] + binom[n-1][i-1]


lim = 23

#We now compute the possible sums (22-tuples (x1, ..., x22) such that sum_i xi = 23 and sum_i 10**i xi = 0 mod 23)
#we do this recursively, specifically let f[a][b][c] be the list of all c-tuples such that sum_i xi = a and sum_i 10**i xi = b
f = [[[[] for _ in range(lim*lim+1)] for _ in range(lim+1)] for c in range(lim+1)]

#Initialize all
for c in range(lim+1):
    f[c][0][0].append([0 for _ in range(c)])

for a in range(1, lim):
    for b in range(lim+1):
        for c in range(lim*lim+1):
            for d in range(b+1):
                #Add the digit d at the end
                if c < d*a:
                    continue
                f[a][b][c] +=  f[a-1][b-d][c-d*a]
r = [f[lim-1][lim][lim*c] for c in range(1, lim)]
print(r)
print(sum(r))


print("Answer = ", len(ans))
end = time.time()
print("Time elapsed ", end - start, " seconds")