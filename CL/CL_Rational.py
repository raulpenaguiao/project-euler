
import math

def gcd(a, b):
    if a < 0:
        return gcd(b, -a)
    if b == 0:
        return a
    return gcd(b, a%b)


class Rational:
    def __init__(self, a = 0, b = 1):
        self.numerator = a
        self.denominator = b
        self.reduced = False


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        self.reduce()
        return str(self.numerator) + "/" + str(self.denominator)


    def __lt__(self, obj):
        self.reduce()
        obj.reduce()
        return self.numerator * obj.denominator < self.denominator * obj.numerator


    def __gt__(self, obj):
        self.reduce()
        obj.reduce()
        return self.numerator * obj.denominator > self.denominator * obj.numerator


    def __le__(self, obj):
        self.reduce()
        obj.reduce()
        return self.numerator * obj.denominator <= self.denominator * obj.numerator


    def __ge__(self, obj):
        self.reduce()
        obj.reduce()
        return self.numerator * obj.denominator >= self.denominator * obj.numerator


    def __eq__(self, obj):
        self.reduce()
        obj.reduce()
        return self.numerator * obj.denominator == self.denominator * obj.numerator
    

    def reduce(self):
        if self.reduced:
            return
        d = gcd(self.numerator, self.denominator)
        if not d == 0:
            self.numerator //= d
            self.denominator //= d
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1
        self.reduced = True
    
    def add(self, rat):
        self.reduced = False
        self.numerator = self.numerator*rat.denominator+self.denominator*rat.numerator
        self.denominator = self.denominator * rat.denominator
        self.reduce()
    

    @staticmethod
    def Plus(r1, r2):
        ans = Rational()
        ans.add(r1)
        ans.add(r2)
        ans.reduce()
        return ans

    def __add__(self, rat):
        return Rational.Plus(self, rat)

    def multiply(self, rat):
        self.numerator = self.numerator*rat.numerator
        self.denominator = self.denominator*rat.denominator
        self.reduce()

    @staticmethod
    def Times(r1, r2):
        ans = Rational(1)
        ans.multiply(r1)
        ans.multiply(r2)
        ans.reduce()
        return ans
    
    
    def __sub__(self, rat):
        return Rational.Plus(self, Rational.Times(rat, Rational(-1)))
    
    
    def __mul__(self, rat):
        return Rational.Times(self, rat)
    
    def Reverse(r1):
        ans = Rational(r1.denominator, r1.numerator)
        ans.reduce()
        return ans
    
    def __truediv__(self, rat):
        return Rational.Times(self, Rational.Reverse(rat))

    def toFloat(r):
        return r.numerator/r.denominator
    

    def SquareRoot(self, PREC = 10**(-6)):
        a = math.sqrt(self.numerator)
        a = math.floor(a+PREC)
        if abs(a*a - self.numerator) > PREC:
            self = Rational()
            return False
        b = math.sqrt(self.denominator)
        b = math.floor(b+PREC)
        if abs(b*b - self.denominator) > PREC:
            self = Rational()
            return False
        self.numerator = a
        self.denominator = b
        return True