import CL_Polynomials as CP
import CL_SetPartitions as CSP
import CL_Sets as CS

class Graph:
    def __init__(self, *args, **kwargs):
        l = len(kwargs["vertices"])
        self.vertices = [i for i in range(l)]
        self.edges = []
        for e in kwargs["edges"]:
            if not len(e) == 2:
                print(kwargs["vertices"],  " ::: ",  kwargs["edges"])
                raise Exception("Malformed edges")
            try:
                self.edges.append(tuple([kwargs["vertices"].index(e[0]), kwargs["vertices"].index(e[1])]))
            except:
                print(kwargs["vertices"],  " ::: ",  kwargs["edges"])
                raise Exception("edges contain non-vertices")
        self.edges = DeleteCopiesAndLoops(self.edges)
    
    def IsEmpty(self):
        #Checks if a graph has no edges
        return self.edges == []

    def delete(self, edge):
        if not edge in self.edges:
            raise Exception("no edge in the graph")
        nedges = [e for e in self.edges if not e == edge]
        return Graph(vertices = self.vertices, edges = nedges)

    def contract(self, edge):
        nverts = [v for v in self.vertices if not v in edge] + [edge]
        nedges = []
        for e in self.edges:
            if (e[0] == edge[0] and e[1] == edge[1]) or (e[1] == edge[0] and e[0] == edge[1]):
                pass
            elif e[0] in edge:
                nedges.append([edge, e[1]])
            elif e[1] in edge:
                nedges.append([e[0], edge])
            else:
                nedges.append(e)
        return Graph(vertices = nverts, edges = nedges)

    def isIndependent(self, A):
        l = A.lst()
        for i in range(A.size):
            for j in range(i):
                if (tuple([l[i], l[j]]) in self.edges or tuple([l[j], l[i]]) in self.edges):
                    return False
        return True


    def StableSP(self, sp):
        for b in sp.blocks:
            l = b.size
            if not self.isIndependent(b):
                return False
        return True

    def chromatic_polynomial(self):
        ans = CP.Polynomial()
        if self.IsEmpty():
            return CP.Polynomial(type = "mon", degree = len(self.vertices))
        for sp in CSP.GenerateSetPartitions(CS.Set(elements = self.vertices)):
            if self.StableSP(sp):
                ans += CP.Polynomial(type = "falling_factorial", degree = len(sp.blocks))
        return ans
    
    def __repr__(self):
        return str([self.vertices] + [self.edges])



def DeleteCopiesAndLoops(lst):
    if lst == []:
        return []
    slst = sorted(lst)
    #Find first non-loop
    i = 0
    ln = len(slst)
    while(i < ln and slst[i][0] == slst[i][1]):
        i += 1
    if i == ln:
        return []
    ans = [slst[i]]
    i += 1
    while(i < ln):
        if not slst[i] == slst[i-1] and not slst[i][0] == slst[i][1]:
            ans.append(slst[i])
        i += 1
    return ans