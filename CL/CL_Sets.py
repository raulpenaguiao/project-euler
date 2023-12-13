class Set:
    def __init__(self, *args, **kwargs):
        if "elements" in kwargs:
            self.bag = {}
            self.size = 0
            for el in kwargs["elements"]:
                self.bag[el] = True
                self.size += 1
        else:
            print("EEROOOR ", kwargs)
    

    def Union(self, other):
        ans = Set(elements = self.bag)
        for el in other.bag:
            if not el in self.bag:
                ans.bag[el] = True
                ans.size += 1
        return ans
    
    
    def Subsets(self):
        ans = [Set(elements = [])]
        for el in self.bag:
            newans = []
            for st in ans:
                newans.append(st.Union(Set(elements = [el])))
            ans += newans
        return ans
    
    def lst(self):
        return [el for el in self.bag]

    def PickElement(self):
        for el in self.bag:
            return el
        raise Exception("The set is empty")
    
    def IsEmpty(self):
        for el in self.bag:
            return False
        return True
    
    def Complement(self, universe):
        return Set(elements = [el for el in universe.bag if not el in self.bag])

    def __repr__(self):
        ans = "{ "
        for el in self.bag:
            ans += "" + str(el) + ","
        ans = ans[:-1]
        ans += "}"
        return ans