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


def bfs(s, e, d_cnt):
    global finished
    queue = deque()
    queue.append((s, e, d_cnt))
    visited[s][e] = 1  # 거리 카운팅은 하지 않지만, 방문체크는 해야 함.
    while queue:
        x, y, cnt = queue.popleft()
        if x == N-1 and y == N-1:
            finished = True
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 연결되어 있고, 방문하지 않아야 함
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt+1))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    N = 7
    graph = []  # 7*7 격자판 그래프
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    visited = [[0] * N for _ in range(N)]  # 방문여부 체크
    finished = False
    cnt = bfs(0, 0, 0)
    if finished:
        print(cnt)
    else:
        print(-1)
