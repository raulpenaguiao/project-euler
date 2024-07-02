import time
start = time.time()
ans = 0
from decimal import Decimal, getcontext
getcontext().prec = 32


def FindQuadricSolution(lin, const, initialGuess):
    #We use newton method for solving this equation
    ak = initialGuess
    print("solving ", lin, const, initialGuess)
    diff = Decimal(0)
    fval = Decimal(1)
    while(fval > Decimal(10)*(-10) ):
        ak += diff
        fval = ak*ak*ak*ak +lin * ak + const
        diff = fval/(Decimal(4)*ak*ak*ak+lin)
        print(ak)
    return ak



def FindNTerms(a0, a1, n):
    i = 1
    a_i = a1
    a_im1 = a0
    ans = [a0, a1]
    while(i < n):
        a = a_i
        lin = Decimal(4)*a*a*a
        a_i = FindQuadricSolution(-lin, lin*a_im1 - a*a*a*a, Decimal(2)*a-a_im1)
        a_im1 = a
        ans.append(a_i)
    return ans


#Find a1
a0 = Decimal(-1)
a1max = Decimal(-1 + 1/10)
a1min = Decimal(-1)
a1 = (a1max+a1min)/Decimal(2)
a50 = FindNTerms(a0, a1, 50)[-1]
while(abs(a50) < Decimal(10)**(-10)):
    if a50 > 0:
        a1max = a1
    else:
        a1min = a1
    a1 = (a1max+a1min)/Decimal(2)
    a50 = FindNTerms(a0, a1, 50)[-1]
print(FindNTerms(a0, a1, 50))



print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")