# https://www.acmicpc.net/problem/14500

def dfs(L, sm, tlst):
    global ans
    # 가지치기: 나머지를 모두 가장 큰 값으로 더해도 ans보다 작으면 그만둔다.
    if sm + (4-L)*mx <= ans:
        return
    if L == 4:
        ans = max(ans, sm)
        return
    for cx, cy in tlst:
        for j in range(4):
            nx = cx + dx[j]
            ny = cy + dy[j]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and v[nx][ny] == 0:
                v[nx][ny] = 1
                dfs(L+1, sm + graph[nx][ny], tlst+[(nx, ny)])
                v[nx][ny] = 0

# 순서 중요 (동남 -> 서북 순으로)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0
mx = max(map(max, graph))

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, graph[i][j], [(i, j)])
print(ans)
