# https://www.acmicpc.net/problem/2644
from collections import deque


def bfs(s, e):
    # [1] q, v 초기화
    q = deque()
    v = [0]*(N+1)
    # [2] 초기데이터 삽입
    q.append(s)
    v[s] = 0

    while q:
        c = q.popleft()
        if c == e:
            return v[c]
        # 인접, 미방문
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return -1


N = int(input())    # 총 사람 수
one, two = map(int, input().split())
M = int(input())    # 관계 수
adj = [[] for _ in range(N+1)]  # 인접행렬
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

res = bfs(one, two)
print(res)
