import time
start = time.time()
from math import exp

ans = 0

def hei(x, y):
    return  ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")