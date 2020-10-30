import queue
from collections import defaultdict
def bfs(s):
    global out
    q = queue.Queue()
    q.put(s)
    V[s] = True
    while not q.empty():
        u = q.get()
        out += [u]
        for v in G[u]:
            indeg[v] -= 1
            if indeg[v] == 0 and not V[v]:
                V[v] = True
                q.put(v)

def topologicalSort():
    for u in G.keys():
        for v in G[u]:
            indeg[v] += 1
    for u in range(N):
        if indeg[u] == 0 and not V[u]:
            bfs(u)
        
N, M = map(int, input().split())
out = []
V = [False] * N
indeg = [0] * N
G = defaultdict(list)
for i in range(M):
    s, t = map(int, input().split())
    G[s] += [t]
topologicalSort()

for x in out:
    print(x)
    