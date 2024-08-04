class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                # rootX becomes the parent of rootY
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                # rootY becomes the parent of rootX
                self.parent[rootX] = rootY
            else:
                # Arbitrarily make rootX the parent of rootY
                self.parent[rootY] = rootX
                # Increment the rank of the new root
                self.rank[rootX] += 1
