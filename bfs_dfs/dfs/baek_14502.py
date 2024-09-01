# https://www.acmicpc.net/problem/14502
from collections import deque
from copy import deepcopy


def dfs(L, s, lst):
    if L == 3:
        wall.append(lst)
        return
    for j in range(s, Nv):
        dfs(L+1, j+1, lst + [v0[j]])

def bfs():
    q = deque()
    virus_cnt = 0
    for v in v2:
        q.append(v)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고, 방문하지 않았고, 빈칸이라면
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 0:
                g[nx][ny] = 2  # 바이러스 처리
                virus_cnt += 1
                q.append((nx, ny))
    return virus_cnt


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
v0 = []  # 빈칸 좌표 리스트
v2 = []  # 바이러스 좌표 리스트
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            v0.append((i, j))
        elif graph[i][j] == 2:
            v2.append((i, j))
Nv = len(v0)
wall = []  # 뽑힌 벽 리스트
# 1. 빈칸 중에 3개를 뽑아 벽으로 만드는 조합 정하기
dfs(0, 0, [])

# 2. 최대 안전영역 구하기
mx = 0
for w in wall:
    g = deepcopy(graph)
    for x, y in w:
        g[x][y] = 1
    virus_cnt = bfs()
    safe_cnt = Nv-len(w)-virus_cnt
    mx = max(mx, safe_cnt)
print(mx)
