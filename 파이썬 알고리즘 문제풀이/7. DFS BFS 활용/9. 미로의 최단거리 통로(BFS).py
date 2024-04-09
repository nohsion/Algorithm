# 7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요.
# 경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다.
# 출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7) 좌표이다. 격자판의 1은 벽이고, 0은 도로이다.
# 움직임: 상하좌우
# 최단 경로의 거리(칸의 수)를 출력하고 도착할 수 없으면 -1 출력. 단, 출발지점(1,1) 칸은 세지 않는다.
"""
최단 거리 - BFS
1. 동서남북 이동 (dx, dy 활용)
    - 범위 내에 있고, 0 <= nx(ny) <= N-1
    - 연결되어 있어야 함. graph[nx][ny] == 0 (연결: 0, 벽: 1)
    - 방문하지 않았어야 함. visited[nx][ny] == 0
2. 해당 노드들은 큐에 삽입
    - cnt += 1 (거리 증가)
    - visited[nx][ny] = 1 (방문처리)
    - queue.append(nx, ny)
3. 종료조건
    - (nx, ny) == (n-1, n-1) 도착지점에 오면 종료
"""
from collections import deque


def bfs(s, e):
    global finished
    queue = deque()
    queue.append((s, e))
    dis[s][e] = 0  # 시작점: 거리 0 및 방문체크
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == N-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 연결되어 있고, 방문하지 않아야 함
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and graph[nx][ny] == 0 and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1
                queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    N = 7
    graph = []  # 7*7 격자판 그래프
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # visited = [[0] * N for _ in range(N)]  # 방문여부 체크
    dis = [[-1] * N for _ in range(N)]  # 거리 저장용
    bfs(0, 0)
    print(dis[N-1][N-1])
