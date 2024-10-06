# DFS, BFS 순으로 방문 경로 출력
from collections import deque

def dfs(c):
    ans_dfs.append(c)
    for n in sorted(adj[c]):
        if v[n] == 0: # 미방문 탐색
            v[n] = 1   # 되돌아가지 않으니 원상복구 안해도 됨.
            dfs(n)

def bfs(s):
    q = deque()
    v[s] = 1
    q.append(s)
    while q:
        c = q.popleft()
        ans_bfs.append(c)
        for n in sorted(adj[c]):
            if v[n] == 0: # 미방문 탐색
                v[n] = 1
                q.append(n)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

ans_dfs, ans_bfs = [], []
# DFS
v = [0]*(N+1)
v[V] = 1
dfs(V)

# BFS
v = [0]*(N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)