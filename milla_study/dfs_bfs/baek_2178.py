# https://www.acmicpc.net/problem/2178
from collections import deque


def bfs(x, y, move_cnt):
    global res
    queue = deque()
    queue.append((x, y, move_cnt + 1))
    graph[x][y] = 0  # 방문처리
    while queue:
        qx, qy, q_cnt = queue.popleft()
        if qx == n-1 and qy == m-1:
            if q_cnt < res:
                res = q_cnt
            continue
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny, q_cnt + 1))
                graph[nx][ny] = 0  # 방문처리


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    # 세로 N, 가로 M (N*M 배열)
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    res = 2147000000
    bfs(0, 0, 0)
    print(res)
