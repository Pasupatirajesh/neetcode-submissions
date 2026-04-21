class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i]  = 1
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
        
    def union(self, x, y):
        
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x== root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        else:
            self.par[root_y] = root_x
            self.rank[root_x] +=1
        return True
 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = UnionFind(n)
        for x, y in edges:
            if not dsu.union(x, y):
                return [x, y]
        return edges[-1]
