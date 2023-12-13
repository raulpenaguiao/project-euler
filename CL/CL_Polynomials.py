class Polynomial:
    def __init__(self, *args, **kwargs):
        if not "type" in kwargs:
            self.coeffs = []
            self.degree = -1#the zero polynomial
        elif kwargs["type"] == "mon":
            self.coeffs = [0 for _ in range(kwargs["degree"])]
            self.coeffs += [1]
            self.degree = kwargs["degree"]
        elif kwargs["type"] == "coeffs":
            self.coeffs = kwargs["coeffs"][:]
            self.degree = len(kwargs["coeffs"])-1
        elif kwargs["type"] == "falling_factorial":
            p = Polynomial(type = "mon", degree = 0)
            for i in range(kwargs["degree"]):
                p *= Polynomial(type = "coeffs", coeffs = [-i, 1])
            self.degree = p.degree
            self.coeffs = p.coeffs[:]
        else:
            raise Exception("Polynomial not defined")
    
    
    def __mul__(self, other):
        if self.degree < 0 or other.degree < 0:
            return Polynomial()
        c = [0 for _ in range(self.degree + other.degree + 1)]
        for i in range(self.degree+1):
            for j in range(other.degree+1):
                c[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial(type = "coeffs", coeffs = c)

    def __add__(self, other):
        if self.degree >= other.degree:
            ans = Polynomial(type = "coeffs", coeffs = self.coeffs[:])
            for i in range(other.degree + 1):
                ans.coeffs[i] += other.coeffs[i]
            ans.reshapeDegree()
            return ans
        else:
            return other + self
    

    def scale(self, scale):
        ans = Polynomial(type = "coeffs", coeffs = self.coeffs)
        for i in range(self.degree + 1):
            ans.coeffs[i] *= scale
        return ans
    def __sub__(self, other):
        return self + other.scale(-1)
    def reshapeDegree(self):
        d = len(self.coeffs)-1
        while(self.coeffs[d] == 0):
            d -= 1
        self.degree = d
        self.coeffs = self.coeffs[:d+1]
    def __repr__(self):
        #find first non-zero coeff
        f = 0
        while(self.coeffs[f] == 0):
            f += 1
        if self.coeffs[f] == 1:
            if f == 0:
                ans = "1"
            elif f == 1:
                ans = "x"
            else:
                ans = "x^" + str(f)
        else:
            if f == 0:
                ans = str(self.coeffs[f])
            elif f == 1:
                ans = str(self.coeffs[f]) + "*x"
            else:
                ans = str(self.coeffs[f]) + "*x^" + str(f)
        for i in range(f + 1, self.degree+1):
            if self.coeffs[i] > 0:
                if self.coeffs[i] == 1:
                    if i == 1:
                        ans +=  " +x"
                    else:
                        ans +=  " +x^" + str(i)
                else:
                    if i == 1:
                        ans +=  " +" + str(self.coeffs[i]) + "*x"
                    else:
                        ans +=  " +" + str(self.coeffs[i]) + "*x^" + str(i)
            elif self.coeffs[i] < 0:
                if i == 1:
                    ans += " " +  str(self.coeffs[i]) + "*x"
                else:
                    ans += " " +  str(self.coeffs[i]) + "*x^" + str(i)
        return ans
    def __str__(self):
        return self.__repr__()
    def eval(self, value):
        ans = 0
        pow = 1
        for i in range(self.degree+1):
            ans += self.coeffs[i]*pow
            pow *= value
        return ans