class DisjointSet:
    def __init__(self, size):
        self.rank = [0 for i in range(size)]
        self.p = [0 for i in range(size)]
        for i in range(size):
            self.makeSet(i)
    
    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    
    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]
        

if __name__ == '__main__':
    n, q = map(int, input().split())
    ds = DisjointSet(n)    
    for i in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            ds.unite(x, y)
        else:
            if ds.same(x, y):
                print(1)
            else:
                print(0)
