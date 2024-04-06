# https://www.acmicpc.net/problem/2667
from collections import deque


def bfs(x, y):
    global cnt
    # 첫번째 노드도 카운트 및 방문표시 해야 한다.
    queue = deque([(x, y)])
    cnt += 1
    graph[x][y] = 0
    while queue:
        (qx, qy) = queue.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                queue.append((nx, ny))
                graph[nx][ny] = 0


if __name__ == '__main__':
    n = int(input())
    graph = []  # 그래프
    for i in range(n):
        graph.append(list(map(int, input())))

    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    home_cnt = []  # 각 단지내 집의 개수
    cnt = 0  # 한 단지 내에 집이 몇 개인지 셀 변수
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                home_cnt.append(cnt)
                cnt = 0

    print(len(home_cnt))
    for h in sorted(home_cnt):
        print(h)
