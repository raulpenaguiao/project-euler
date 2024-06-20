#I have conjectures and computationally verified that all ambiguous best aproximations satisfy ad - bc = 1
#In fact it might be the case that this is true for any two consecutive best aproximations...


import time
start = time.time()
from ....CL.CL_Arithmetics import gcd
from ....CL.CL_Rational import Rational
ans = 0

def AddToDic(dic, key, item):
    if key in dic:
        dic[key] += [item]
    else:
        dic[key] = [item]

def NUM(LIM, interv):
    cic = {}
    rats = [Rational(), Rational(1, interv)]
    for i in range(interv + 1, LIM+1):
        for j in range(1, (i-1)//interv+1):
            if gcd(i, j) == 1:
                #Find smallest larger number
                rat = Rational(j, i)
                index = 0
                while(rats[index] < rat):
                    index += 1
                rat1 = rats[index]
                ratm = (rat1 + rat)/Rational(2)
                if ratm.denominator <= LIM:
                    AddToDic(cic, ratm.denominator, ratm.numerator)
                rat1 = rats[index - 1]
                ratm = (rat1 + rat)/Rational(2)
                if ratm.denominator <= LIM:
                    AddToDic(cic, ratm.denominator, ratm.numerator)
                rats = rats[:index] + [rat] + rats[index:]
    
    vals = [[] for _ in range(LIM+1)]
    for key in cic:
        vals[key] = cic[key]
    return vals


#print([[n, NUM(n)] for n in range(100, 1001, 50)])
print("Answer = ", NUM(400, 2)[::2])
print("Answer = ", NUM(400, 3)[::2])
print("Answer = ", NUM(400, 4)[::2])
print("Answer = ", NUM(400, 5)[::2])
end = time.time()
print("Time elapsed ", end - start, " seconds")