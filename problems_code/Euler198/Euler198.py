import time
start = time.time()
import CL_Arithmetics as CA
import CL_Rational as CR

ans = 0
rats = []
LIM = 100000
for i in range(1, LIM):
    for j in range(1, i):
        if CA.gcd(i, j) == 1:
            rats.append(CR.Rational(j, i*100))


print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")