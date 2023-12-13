import math
import CL_Rational as RC



def toRational(lst):
    if lst == []:
        raise Exception("Empty list is not a continued fraction")
    l = len(lst)
    ans = RC.Rational(lst[-1])
    for i in range(l-2, -1, -1):
        ans = ans.Reverse()
        #print(ans, lst[i], i)
        ans.add(RC.Rational(lst[i]))
    return ans


#This function is not really optimized..
def ContinuedFractionsqrt(n):
    a = math.floor(math.sqrt(n))
    if a*a == n:
        return [a]
    ans = [a]
    while(ans[-1] < 2*a):
        if len(ans)%2 == 0:
            klb = 1
            kub = 2
            ub = toRational(ans + [kub])
            while(RC.Rational.Times(ub, ub) < RC.Rational(n)):
                kub *= 2
                ub = toRational(ans + [kub])
            while(kub - klb > 1):
                km = (kub + klb)//2
                mb = toRational(ans + [km])
                if(RC.Rational.Times(mb, mb) < RC.Rational(n)):
                    klb = km
                else:
                    kub = km
            ans += [klb]
        else:
            klb = 2
            kub = 1
            lb = toRational(ans + [klb])
            while(RC.Rational.Times(lb, lb) > RC.Rational(n)):
                klb *= 2
                lb = toRational(ans + [klb])
            while(klb - kub > 1):
                km = (kub + klb)//2
                mb = toRational(ans + [km])
                if(RC.Rational.Times(mb, mb) > RC.Rational(n)):
                    kub = km
                else:
                    klb = km
            ans += [kub]
    return [ans[0], ans[1:]]













