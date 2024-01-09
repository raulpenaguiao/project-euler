import time
start = time.time()
from ...CL.CL_Primes import Primes, MillerRabin, EulerPhi

p = EulerPhi(1000)
print(p[1:40])
end = time.time()
print("Time elapsed ", end - start, " seconds")