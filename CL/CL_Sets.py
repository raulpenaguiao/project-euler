class Set:
    def __init__(self, *args, **kwargs):
        if "elements" in kwargs:
            self.bag = {}
            self.size = 0
            for el in kwargs["elements"]:
                self.append(el)
        else:
            print("EEROOOR ", kwargs)

    def Union(self, other):
        ans = Set(elements = self.bag)
        for el in other.bag:
            if not el in self.bag:
                ans.bag[el] = True
                ans.size += 1
        return ans
    

    def append(self, el):
        if not el in self.bag:
            self.size += 1
            self.bag[el] = True

    def Intersection(self, other):
        ls = []
        for el in self.bag:
            if el in other.bag:
                ls += [el]
        return Set(elements = ls)

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
        raise Exception("EMPTYSET: Cannot pick an element, the set is empty")
    

    def Select(self, cond):
        ans = [Set(elements = [])]
        for el in self.bag:
            if cond(el):
                ans.append(el)
        return ans


    def IsEmpty(self):
        for _ in self.bag:
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
    
    
    def Copy(self):
        return Set(elements = self.lst())