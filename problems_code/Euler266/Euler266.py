import time
start = time.time()
from ...CL.CL_Primes import Primes
primes = Primes(190)
print(primes)
print(len(primes))
ans = 0




print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")