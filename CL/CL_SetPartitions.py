import CL_Sets as CS
import CL_Polynomials as CP

class Set_Partition:
    def __init__(self, *args, **kwargs):
        self.ground_set = kwargs["ground_set"]
        if "blocks" in kwargs:
            self.blocks = kwargs["blocks"]
        else:
            self.blocks = [self.ground_set]

    def Choose(self):
        ans = CP.Polynomial(type = "mon", degree = 0)
        for b in self.blocks:
            ans *= CP.Polynomial(type = "falling_factorial", degree = b.size)
        return ans

    
    def __repr__(self):
        return " | ".join([str(b) for b in self.blocks])

def GenerateSetPartitions(ground_set):
    if ground_set.IsEmpty():
        return [Set_Partition(ground_set = ground_set)]
    el = ground_set.PickElement()
    els = CS.Set(elements = [el]).Complement(ground_set)
    ans = [Set_Partition(ground_set = ground_set)]
    for subset in els.Subsets():
        if not subset.IsEmpty():
            for set_partition in GenerateSetPartitions(subset):
                ans.append(Set_Partition(ground_set = ground_set, blocks = set_partition.blocks + [subset.Complement(ground_set)]))
    return ans
        
        
