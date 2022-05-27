import time
import math

start_time = time.time()

prime = 10** 9 + 7
LIM = 2022
prod = [1, 9]

for i in range(9, 0, -1):
    prod+= [prod[-1] * i]
#print(" - ".join([str(a) for a in prod]))

binomial = [[0 for _ in range(LIM + 3)] for _ in range(LIM+3)]
binomial[0][0] = 1
for i in range(1, LIM+3):
    binomial[i][0] = 1
    for j in range(1, i+1):
        binomial[i][j] = binomial[i-1][j] + binomial[i-1][j-1]
        binomial[i][j] %= prime

set_parts = [[0 for _ in range(12)] for _ in range(LIM + 2)]
#set_parts[u][l] is the number of set partitions of a set of size u into l parts
#it satisfies the recurring formula
#set_parts[u][l] = l * set_parts[u-1][l] + set_parts[u][l-1]
#initial conditions 
#for u>=1, set_parts[u][1] = 1
#for u= 0 and l > 0, set_parts[u][l] = 0
#set_parts[0][0] = 1

set_parts[0][0] = 1
for u in range(1, LIM+1):
    set_parts[u][1] = 1

for l in range(2, 12):
    for u in range(LIM+1):
        set_parts[u][l] = l*set_parts[u-1][l] + set_parts[u-1][l-1]
        set_parts[u][l] %= prime



#This array sets the contribution of the blocks of at most half the size
#If you are counting the number of ints with k digits, a large set of which are specified to be the same
#Then there are partition_comput[k-l] many such integers
partition_comput = [ 0 for _ in range(LIM + 2)]
tot = 0
for u in range(LIM + 2):
    tot = 0
    for i in range(10):
        tot += prod[i+1] * set_parts[u][i]
        tot %= prime
    partition_comput[u] = tot

tot = 0
for u in range(0, (LIM - 1)//2+1):
    tot += partition_comput[u] * (binomial[LIM + 1][u+1] - binomial[2*u + 1][u+1] )
    tot %= prime
    #print("u = ", u, " and parts = ", partition_comput[u])
    #print("binomial = ", (binomial[LIM + 1][u] - binomial[2*u + 1][u] ))

    """
    for u in range(min(l, LIM - l + 1)):
        tot += binomial[l+u][u] * partition_comput[u]
        tot %= prime
        #print("l = ", l, " and u = ", u)
        #print(" binom = ", binomial[l+u][u], " and part counter = ", partition_comput[u])
        """

print(tot)
print(" --- %s seconds --- "%(time.time() - start_time))
