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
        
def kruskal(V, e):
    # V=ノードの数，e=(s, t, w)のエッジのリスト
    e = sorted(e, key=lambda x: x[2])
    S = DisjointSet(V)
    K = []
    for s, t, w in e:
        # if S.findSet(s) != S.findSet(t):
        if not S.same(s, t):
            S.unite(s, t)
            K.append((s, t, w))
    return K

if __name__ == '__main__':
    V, E = map(int, input().split())
    # s, t, w
    e = [tuple(map(int, input().split())) for i in range(E)]
    K = kruskal(V, e)
    ans = 0
    for s, t, w in K:
        ans += w
    print(ans)
    