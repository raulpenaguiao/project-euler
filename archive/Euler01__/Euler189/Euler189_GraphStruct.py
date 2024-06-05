#Code written on the 14/11/2023
#Computes all the independent sets I. For each, computes the number of connected components of the remaning graph cc(G\I)
#The number of colourings is sum_I 2**cc(G\I)
#Runs for 0.0005s for N = 1, there are 3 colours, 2 independent sets, 1 vertex and 0 edges
#Runs for 0.0005s for N = 2, there are 24 colours, 9 independent sets, 4 vertices and 3 edges
#Runs for 0.002s for N = 3, there are 528 colours, 95 independent sets, 9 vertices and 9 edges
#Runs for 0.090s for N = 4, there are 31968 colours, 2385 independent sets, 16 vertices and 18 edges
#Runs for 8.9s for N = 5, there are 5332224 colours, 142991 independent sets, 25 vertices and 30 edges
#Runs for 2297s for N = 6, there are 2450774016 colours, 20495195 independent sets, 36 vertices and 45 edges
#Runs for s for N = 7, there are 3104112826368 colours (according to OEIS)



import time
import math
import queue
start = time.time()
ans = 0


class Set:
    def __init__(self, elements = []):
        self.set = {e:True for e in elements}
    

    def __iter__(self):
        return self.set.__iter__()


    def toList(self):
        return [el for el in self.set.keys()]
    

    def __str__(self):
        return self.toList().__str__()
    

    def __repr__(self):
        return self.__str__()


    def union(self, set):
        ans = Set(self.set.keys())
        for a in set:
            ans.set[a] = True
        return ans
    

    def Has(self, el):
        return el in self.set
    

    def addElement(self, el):
        self.set[el] = True
    

    def setMinus(self, set):
        ans = Set(self.set.keys())
        for a in set:
            ans.remElement(a)
        return ans
    

    def Intersection(self, set):
        ans = Set()
        for a in set:
            if self.Has(a):
                ans.addElement(a)
        return ans
    

    def remElement(self, el):
        if el in self.set:
            del self.set[el]


class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.edges = {v:Set() for v in vertices}
        for e in edges:
            self.edges[e[0]].addElement(e[1])
            self.edges[e[1]].addElement(e[0])


    def removeEdge(self, e):
        self.edges[e[0]].remElement(e[1])
        self.edges[e[1]].remElement(e[0])
    

    def ListIndependentSets(self):
        ans = []
        q = queue.Queue()
        q.put([Set(), self.vertices])
        while not q.empty():
            S, vert = q.get()
            print("Evaluating set ", S)
            ans.append(S)
            for i in range(len(vert)):
                v = vert[i]
                q.put([S.union(Set([v])), Set(vert[i+1:]).setMinus(self.edges[v]).toList()])
        return ans
    

    def Subgraph(self, I):
        new_edges = []
        for v in I:
            for w in self.edges[v].Intersection(I):
                new_edges.append([v, w])
        return Graph(vertices=I, edges=new_edges)
    

    def ConectedComponents(self):
        parent = {v:v for v in self.vertices}
        cc = {v:Set([v]) for v in self.vertices}
        #print(parent)
        for v in self.edges:
            for w in self.edges[v]:
                #print("Edge : ", v, w)
                a = v
                while not(parent[a] == a):
                    a = parent[a]
                b = w
                while not(parent[b] == b):
                    b = parent[b]
                parent[v] = a
                parent[w] = a
                if not(a == b):
                    parent[b] = a
                    for v in cc[b]:
                        cc[a].addElement(v)
                #print(parent)
        comps = 0
        for v in self.vertices:
            if parent[v] == v:
                comps += 1
        return comps

#G = Graph(vertices = [1, 2, 3, 4], edges = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]])
vertices = []
edges = []
for i in range(N):
    for j in range(N-i):
        vertices.append(tuple([i, j, N-1-i-j]))
        if j + i < N - 1:
            vertices.append(tuple([i, j, N-2-i-j]))

for i in range(len(vertices)):
    v = vertices[i]
    for j in range(i):
        w = vertices[j]
        if(abs(v[0]-w[0])+abs(v[1]-w[1])+abs(v[2]-w[2]) == 1):
            edges.append([v, w])

G = Graph(vertices=vertices, edges=edges)
indep_sets = G.ListIndependentSets()
print("N = ", N, ", vertices = ", len(vertices), " has ", len(edges), " edges.")
print("Number of independent sets: ", len(indep_sets))

for I in indep_sets:
    remainingVertices = Set(G.vertices).setMinus(I).toList()
    ans += 2**G.Subgraph(remainingVertices).ConectedComponents()

print("Answer = ", ans)
end = time.time()
print("Time elapsed ", end - start, " seconds")