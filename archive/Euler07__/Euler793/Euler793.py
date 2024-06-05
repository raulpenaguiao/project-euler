#Code created on 2023/10/25
#Through binary search: given a value K, we compute how many products are <= K
#This function itself works by running n binary searches, so the complexity is nlog(nlog(n))
#Code runs in 165s

import time
import math
start = time.time()


N = 1000003 # ans = 475808650131120
#N = 100003 # ans = 473282744219190
#N = 10003 # ans = 467284136913168
#N = 103 # ans = 492700616748525
#N = 4 # ans = 6459987568476
#N = 3 # ans = 3878983057768

S = [290797 for _ in range(N)]
for i in range(1, N):
    S[i] = (S[i-1]**2)%50515093

#Observe the list
"""
for i in range(N):
    print(S[i])
"""


S.sort()
#Experimentally tested there are no repetitions
"""
for i in range(N-1):
    if(S[i+1] == S[i]):
        print("Repetition found")
"""

"""
#Naive method
totalList = []
for i in range(1, N):
    totalList += [S[i]*S[j] for j in range(i)]
totalList.sort()
#print(len(totalList))
mid = len(totalList)//2
mid2 = (len(totalList)-1)//2
#print(mid, " :: ", totalList[mid],  " >> " , mid2, " :: ", totalList[mid2])
ans = (totalList[mid] + totalList[mid2])/2
print("Median = ", ans, " ||  (naive method)")
"""



"""
for i in range(len(totalList)):
    print(totalList[i])
"""

#We call totalList to the list flatten [[S[i]*S[j] for j in range(i, N)] for i in range(N)]
#   This list has N*(N+1)//2 elements, and our answer is (totalList[ N*(N+1)//4] + totalList[(N*(N+1)//2-1)//2])/2
#We will do binary search on a set of lists called ordered lists, or OL
#Given a value K, the corresponding OL l(K) is a list l of length N, such that l[i] is the maximal index j 
#   with S[i]*S[j] <= K OR j <= i
#By some binary search on K, we try to find K such that for l = l(K) we have pos(l) := sum_i l[i] - i = sum_i l[i] - (N+1)*N//2 is minimal above p
#   Equivalently, we will minimize sum_i l[i] above p + (N+1)*N//2
#THEOREM: This will give us the value K of totalList[p]


#Gets as input a value K, and outputs the index i tht is maximal such that S[i] <= K
#If no such index exists, outputs -1
def bin_search_pos(K):
    top = N
    bot = -1
    while(top - bot > 1):
        mid = (top + bot)//2
        if(S[mid] > K):
            top = mid
        else:
            bot = mid
    return bot

#Outputs l(K), the list of maximal indices j<=N-1 for each i such that S[i]*S[j] <= K OR j >= i
#We can safely ignore the last entry because we know l[N-1] = N-1
def l(K):
    ans = [bin_search_pos(K/S[i]) for i in range(N-1)]
    for i in range(N-1):
        if (ans[i] < i):
            ans[i] = i
    return ans


def pos_in_square(K):
    l1 = l(K)
    l2 = l(K-0.5)
    print("There are ", sum(l1) - sum(l2), " many elements ", K, " in the list.")
    for i in range(N-1):
        if(not(l1[i] == l2[i])):
            print("Row: ", i, " column from ", l2[i], " to ", l1[i] - 1)

def bin_search_OL(pos):
    top = S[N-2]*S[N-1]
    top_list = l(top) #should be [N-1, N-1, ..., N-1]
    top_score = sum(top_list) #should be N*(N-1)
    bot = S[1]*S[0]-1
    bot_list = l(bot) #should be [0, 1, 2, 3, 4, ..., N-1]
    bot_score = sum(bot_list) #should be 1 + N*(N-1)//2
    target = ((N-2)*(N-1))//2 + pos + 1
    #print("Posmid : ", pos)
    #print("TOP: ", top, " :: :: ", top_score)
    #print(top_list)
    #print("BOT: ", bot, " :: :: ", bot_score)
    #print(bot_list)
    #print(pos, " ::: ", target)
    while(top - bot > 1):
        mid = (top + bot)//2
        mid_list = l(mid)
        mid_score = sum(mid_list)
        #print(mid, " :: :: ", mid_score)
        #print(mid_list)
        if(mid_score >= target):
            top = mid
            #top_list = mid_list
            #top_score = mid_score
        else:
            bot = mid
            #bot_list = mid_list
            #bot_score = mid_score
    return top

if(N == 2):
    ans = S[0]*S[N-1]
else:
    els = N*(N-1)//2
    mid = els//2
    mid2 = (els-1)//2
    posmid = bin_search_OL(mid)
    posmid2 = bin_search_OL(mid2)
    #print(mid, " -- ", posmid, " >> ", mid2, " -- ", posmid2)
    #pos_in_square(posmid)
    ans = (posmid + posmid2)/2

print("Median = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")