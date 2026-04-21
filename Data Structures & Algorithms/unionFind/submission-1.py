class UnionFind:
    
    def __init__(self, n: int):
        self.par ={}
        self.rank = {}
        self.count = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
        

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.par[self.par[x]]
        return self.par[x]


        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        else:
            self.par[root_y] = root_x
            self.rank[root_x]+=1
        
        self.count-=1
        return True

        

    def getNumComponents(self) -> int:
        return self.count

