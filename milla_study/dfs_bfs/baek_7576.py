# https://www.acmicpc.net/problem/7576
# 1: 익은 토마토, 2: 안익은 토마토, -1: 토마토 없는 칸
import sys
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        # 토마토가 있을 때만(1) 동서남북 이동
        if graph[x][y] > 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue
                # 인접 토마토가 0이라면
                if graph[nx][ny] == 0:
                    # 인접 토마토는 익음 처리와 동시에 카운트 해주기
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    # 그래프(토마토 창고) N*M
    m, n = map(int, input().split())
    graph = []  # 그래프
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    bfs()

    res = -1
    for g in graph:
        for x in g:
            if x == 0:
                print(-1)
                sys.exit()
        res = max(res, max(g))
    print(res-1)
