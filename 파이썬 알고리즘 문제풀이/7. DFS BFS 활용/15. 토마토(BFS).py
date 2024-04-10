# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
"""
최소 일수 - BFS
day = [[0]*m for _ in range(n)]  # 일수 카운트
- 2중 for문: 1이고, 아직 방문하지 않았다면, 큐에 먼저 넣어줘야 함.
    if graph[i][j] == 1 and day[i][j] == 0:

BFS
- 동서남북
    - 영역 내에 있고, 0이어야 하고, 아직 방문하지 않아야 함.
    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and graph[nx][ny] == 0 and day[nx][ny] == 0:
        - 단, 한번 갈때마다 일수 정보를 넣어줘야 함.
        day[nx][ny] = day[x][y] + 1
        queue.append((nx,ny))
day 이중 리스트에서 모든값이 1 또는 -1이어야 하고, 가장 큰 값을 찾으면 됨.
만약, 0이 있으면, print(-1)
"""
import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    m, n = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    day = [[0] * m for _ in range(n)]  # 일수 카운트
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and graph[nx][ny] == 0 and day[nx][ny] == 0:
                graph[nx][ny] = 1  # 토마토 익음
                day[nx][ny] = day[x][y] + 1  # 하루가 지남
                queue.append((nx, ny))

    # 토마토가 모두 익었는지 확인
    max_day = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                print(-1)
                sys.exit()
            else:
                if day[i][j] > max_day:
                    max_day = day[i][j]
    print(max_day)
