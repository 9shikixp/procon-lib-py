'''
二部グラフ判定
'''

def dfs(v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
def solve():
    for i in range(1, N+1):
        if color[i] == 0:
            if not dfs(i, 1):
                print('No')
                return
    print('Yes')
N, M = map(int, input().split())
G = [ []for i in range(N+1)]
color = [0 for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
solve()
