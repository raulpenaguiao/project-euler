import time
start = time.time()

lst = [0, 1, 1, 3]
LIM = 1000
for i in range(4, LIM+1):
    if i%2 == 0:
        lst += [ lst[i//2]]
    elif i%4 == 1:
        lst += [ 2* lst[i//2 + 1] - lst[i//4]]
    else:
        lst += [ 3* lst[i//2] - 2* lst[i//4]]


ans = sum(lst)
print(lst)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")