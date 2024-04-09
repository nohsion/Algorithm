# 7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요.
# 출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 통로이다.
# 격자판의 움직임은 상하좌우로만 움직인다.
"""
최단거리를 구하는 게 아니고, 탐색 방법(히스토리)의 수를 구해야 하기 때문에 DFS
1. 종료조건
- 범위 바깥 (cut)
- 도착지점 x==N-1 and y==N-1
"""
import sys

sys.setrecursionlimit(10_000)

def dfs(x, y, d_sum):
    global cnt
    if x == N-1 and y == N-1:
        if cnt == -1:
            cnt = 1
        else:
            cnt += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=N-1 and 0<=ny<=N-1 and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, d_sum + 1)
            visited[nx][ny] = 0  # back했으면, visited 취소 시켜줘야 함.


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    N = 7
    graph = []  # 7*7 격자판 그래프
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    visited = [[0] * N for _ in range(N)]
    cnt = -1
    visited[0][0] = 1
    dfs(0, 0, 0)
    print(cnt)
