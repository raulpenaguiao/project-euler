#Code written on the 2024/01/12
# 
# It does not do what we want it to do. It should work but I assume there is some major bug or something...
#Runs in 50 seconds


import time
start = time.time()
from ...CL.CL_Arithmetics import gcd
from ...CL.CL_Primes import Divisors, Primes
from ...CL.CL_Rational import Rational
ans = 0

verbose = False

def Assert(func, test, res, comment = "", verbose = False):
    if verbose:
        print("Testing function ", func, " on value ", test, "expecting result ",  res, comment)
    if not func(test) == res:
        print("Testing function ", func, " on value ", test, "expecting result ",  res, " failed", comment)

def Prod(lst):
    if lst == []:
        return 1
    return lst[0]*Prod(lst[1:])

def CartesianProduct(mat):
    if mat == []:
        return [[]]
    ans = []
    for ind in mat[0]:
        for pind in CartesianProduct(mat[1:]):
            ans.append([ind] + pind)
    return ans

def DeletedCopies(lst):
    if lst == []:
        return []
    lst.sort()
    ans = [lst[0]]
    l = len(lst)
    for i in range(1, l):
        if not ans[-1] == lst[i]:
            ans.append(lst[i])
    return ans
def FindInList(lst, item):
    l = len(lst)
    for i in range(l):
        if lst[i] == item:
            return i
def SolveMatrixIntMatrix(mat, b, det):
    if det == 0:
        #See if equation is indeterminate
        if mat[0][0]*b[1] == mat[1][0]*b[0]:
            return "Indeterminate matrix"
        else:
            return "Impossible equation"
    #Now we know we are solving a real equation
    return [Rational(mat[1][1]*b[0] - mat[0][1]*b[1], det), Rational(-mat[1][0]*b[0]+mat[0][0]*b[1], det)]
def Det2b2(mat):
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

#print(SolveMatrixIntMatrix([[1, 1], [2, 1]], [3, 4]))
#print(SolveMatrixIntMatrix([[1, 1], [2, 2]], [3, 4]))
#print(SolveMatrixIntMatrix([[1, 1], [2, 2]], [2, 4]))

n = [5248, 1312, 2624, 5760, 3936]
m = [640, 1888, 3776, 3776, 5664]

sn = sum(n)
sm = sum(m)



def AllSolutions(M):
    possBase = [[] for _ in range(5)]
    for index in range(5):
        frac = M.Reverse()*Rational(n[index], m[index])
        frac.reduce()
        print(frac.denominator, m[index]//frac.denominator)
        for bindex in range(frac.denominator, 1 + m[index], frac.denominator):
            aindex = frac*Rational(bindex)
            aindex.reduce()
            possBase[index].append([aindex.numerator, bindex])
    return [len(k) for k in possBase]


#d = gcd(1476*640, 1475*5248)
#print(d)
#print(1475*5248//d, 1476*640//d)
print(AllSolutions(Rational(1476, 1475)))



primes = Primes(max(sum(n),sum(m)))

mmax = max(m)
nmax = max(n)

imin = 0
jmin = 0
dmin = m[imin]*n[jmin]

for i in range(5):#Find most efficient pair of fractions to start analysing
    for j in range(i):
        d = gcd(m[i]*n[j], m[j]*n[i])
        if d < dmin:
            imin = i
            jmin = j
            dmin = d

counter = 0
counter1 = 0
counter2 = 0
bot = n[imin]*m[jmin]//dmin
top = n[jmin]*m[imin]//dmin
possRationalsM = []
dvs = Divisors(dmin, primes)
for k in dvs:
    print(k)
    for ai in Divisors(bot*k, primes):
        for aj in Divisors(top*k, primes):
            bj = bot*k//ai
            bi = top*k//aj
            mFound = False
            M = Rational(ai*m[imin], bi*n[imin])
            if M >= Rational(1) and M in possRationalsM:
                continue
            poss = []
            #Find all the possible collection of fractions that have the same ratio
            thereIsAZero = False
            for l in range(5): #get the list of the most reduced fractions for the remaning entries
                if l == imin:
                    poss.append([[ai, bi], 1])
                    continue
                if l == jmin:
                    poss.append([[aj, bj], 1])
                    continue
                #We now determine that al/bl has to be of the form ((ai/bi)/(ni/mi)) * (nl/ml)
                num = ai*n[l]*m[imin]
                den = bi*m[l]*n[imin]
                d = gcd(num, den)
                num //= d
                den //= d
                maxmultiples = min(n[l]//num, m[l]//den)
                if maxmultiples == 0:#is it not possible to find a fraction for entry l? then loop out
                    thereIsAZero = True
                    break
                poss.append([[num, den] , maxmultiples])
            #Check that indeed there are possiblities for each index
            if M == Rational(1475,1476):
                print(poss)
            if thereIsAZero:#did we loop out
                continue
            #now in poss I have a bunch of possible rationals to test where all the ratios are the same
            #only thing left to check is what are the suitable multiples so that the sum ratio is the inverse
            
            asum = sum([i[0][0] for i in poss])
            bsum = sum([i[0][1] for i in poss])
            num = sn*bi*n[imin]
            den = sm*ai*m[imin]
            d = gcd(num, den)
            num //= d
            den //= d
            maxmultiples = min(sn//num, sm//den)
            for s in range(maxmultiples):#We will try sum(a) = s*num and sum(b) = s*den
                A = s*num - ai - aj
                B = s*den - bi - bj
                smallestRatio = min([poss[i][1] for i in range(5) if not(i == imin or i == jmin)])
                ksR = [i for i in range(5) if (not(i == imin or i == jmin) and poss[i][1] == smallestRatio)][0]
                i1, i2 = [i for i in range(5) if not(i == imin or i == jmin or i == ksR)]
                mat = [[poss[i1][0][0], poss[i2][0][0]], [poss[i1][0][1], poss[i2][0][1]]]
                det = Det2b2(mat)
                if not det == 0:
                    for i in range(1, smallestRatio+1):
                        b = [A - i*poss[ksR][0][0], B - i*poss[ksR][0][1]]
                        smim = SolveMatrixIntMatrix(mat, b, det)
                        if smim[0].isInteger() and smim[1].isInteger() and Rational(0) < smim[0] and Rational(0) < smim[1]:
                            if smim[0] <= Rational(poss[i1][1]) and smim[1] <= Rational(poss[i2][1]):
                                possRationalsM.append(M)
                            mFound = True
                            break
                else:
                    #In this case the matrix equation is not determined
                    #find i so that SolveMatrixIntMatrix(mat, b, det) has an indeterminate solution (instead of being impossible)
                    #if i is not integer, or does not lie in between 0 and smallestRatio, then we dont care about this case
                    numI = A * mat[0][0] - B * mat[1][0]
                    denI = poss[ksR][0][0] * mat[1][0]  - poss[ksR][0][1] * mat[0][0]
                    shouldBeConsidered = False
                    if denI == 0:
                        if numI == 0:
                            shouldBeConsidered = True
                    elif numI%denI == 0:
                        I = numI//denI
                        if 0 < I and I <= smallestRatio:
                            shouldBeConsidered = True
                    if shouldBeConsidered:
                        for p0 in range(1, poss[ksR][1]+1):
                            Ab = A - p0*poss[ksR][0][0]
                            Bb = B - p0*poss[ksR][0][1]
                            for p1 in range(1, poss[i1][1]+1):
                                AB = Ab - p1*poss[i1][0][0]
                                BB = Bb - p1*poss[i1][0][1]
                                if AB%poss[i2][0][0] == 0 and BB%poss[i2][0][1] == 0:
                                    x = AB//poss[i2][0][0]
                                    if x > 0 and x <= poss[i2][1] and x == BB//poss[i2][0][1]:
                                        mFound = True
                                        print("Rational found")
                                        break
                            if mFound:
                                break
                if mFound:
                    break
            if mFound:
                break

possRationalsM = DeletedCopies(possRationalsM)
possRationalsM.sort()
print("There are ", len(possRationalsM), " possible rationals")




print("counter is ", counter)
print("counter1 is ", counter1)
print("counter2 is ", counter2)
print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")