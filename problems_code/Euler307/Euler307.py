import time
start = time.time()
ans = 0


from ...CL.CL_Rational import Rational


def p(k, n):
    #Probability to find at least three defects in a specific chip.
    return Rational(1)-Rational((n-1)**k, n**k)-Rational(k*(n-1)**(k-1), n**k) -Rational(k*(k-1)*(n-1)**(k-2), 2 * n**k) 


print("Answer = ", p(3, 7).toFloat())
end = time.time()
print("Time elapsed ", end - start, " seconds")