# 많은 비가 내려서 높이가 4 이하인 모든 지점이 물에 잠겼다고 하자.
# 물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다.
# 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.
# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하라.
"""
- 비의 양: 그래프 최소 높이~최대 높이까지 하나씩 해보고 그중 안전영역 개수 최대를 출력하면 됨.
지역이 비의 양보다 작거나 같으면 0으로 표시해둔다. (물에 잠긴 것)
단, 원래 그래프로 돌아가야 하기 때문에 복사해서 쓰자.
    res = 0  # 최종 안전영역 최대값
    for rain in (min_rain, max_rain+1):
        # 비의 양 바뀔때마다 그래프, 카운트, 방문리스트 초기화
        safe_cnt = 0
        graph = [a[:] for a in g]
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] <= rain:
                    graph[i][j] = 0
        # 여기서부터 탐색하면 됨. BFS

- 동서남북 탐색
    - 영역 내에 있고, 인접지점이 0보다 커야하고, 방문하지 않아야 함.
    if 0<=nx<=n-1 and 0<=ny<=n-1 and graph[nx][ny] > 0 and visited[nx][ny] == 0:
        visited[i][j] = 1  # 방문 체크.
        queue.append((nx,ny))
"""
from collections import deque


def bfs(ix, iy):
    queue = deque()
    queue.append((ix, iy))
    visited[ix][iy] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] > 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1  # 방문 체크.
                queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    n = int(input())
    g = []
    rain = set()
    min_rain, max_rain = 2147000, 0
    for _ in range(n):
        row = list(map(int, input().split()))
        rain.update(set(row))
        g.append(row)

    res = 0  # 최종 안전영역 최대값
    cnt = []
    for rain in sorted(rain):
        # 비의 양 바뀔때마다 그래프, 카운트, 방문체크 초기화
        safe_cnt = 0
        graph = [a[:] for a in g]
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] <= rain:
                    graph[i][j] = 0  # 비에 잠긴걸 표시
        # 여기서부터 탐색하면 됨.
        for i in range(n):
            for j in range(n):
                if graph[i][j] > 0 and visited[i][j] == 0:
                    bfs(i, j)
                    safe_cnt += 1
        cnt.append(safe_cnt)
    print(max(cnt))
