# 섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있으며, 0은 바다입니다.
# 섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.
"""
동서남북4 + 대각선4
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
"""
from collections import deque


def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내에 있고, 방문하지 않아야 함
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)


def bfs(ix, iy):
    queue = deque()
    queue.append((ix, iy))
    graph[ix][iy] = 0  # 방문 체크
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 방문하지 않아야 함
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


if __name__ == '__main__':
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # dfs(i, j)
                bfs(i, j)
                cnt += 1
    print(cnt)
