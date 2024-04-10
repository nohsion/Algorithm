# 사다리 표현은 2차원 평면은 0으로 채워지고, 사다리는 1로 표현합니다.
# 현수는 특정 도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고 싶습니다. 특정 도착지점은 2로 표기됩니다.
# 10*10의 사다리 지도가 주어질 때, 출발지 열 번호를 출력하세요.
"""
사다리 타기: 밑으로 가다가 옆으로 꺾임. (순서: 동서남으로 하면 됨. 북은 X)
단, 동서남 중에 하나를 갔으면 다른 곳은 가면 안됨..!! (우선순위 중 하나로) - back한 후에 진행하지 않기.
0~9번까지 모두 진행해야 하기 때문에, visited를 매번 초기화해주자. graph는 건들면 안됨
- 동서남 탐색
    - 영역 내에 있고, 1이고, 방문하지 않아야 함.
    if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] == 1 and visited[nx][ny] == 0:
- 종료조건
    - if x == n-1: 맨 아래층에 오면 끝
    - if graph[x][y] == 2
"""


def dfs(x, y):
    global arrived
    if x == N-1:
        if graph[x][y] == 2:
            arrived = True
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        # 영역 내에 있고, 0보다 크고, 방문하지 않아야 함
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and graph[nx][ny] > 0 and visited[nx][ny] == 0:
            # print(f"graph[{nx}][{ny}]={graph[nx][ny]}")
            visited[nx][ny] = 1
            dfs(nx, ny)
            break  # (중요!) 동서남 순서로 하나를 선택했으면, 되돌아와서 다른 데를 가면 안 됨.


dx = [0, 0, 1]
dy = [1, -1, 0]
N = 10


if __name__ == '__main__':
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    arrived = False
    for i in range(N):
        if graph[0][i] == 1:
            visited = [[0] * N for _ in range(N)]
            dfs(0, i)
            if arrived is True:
                print(i)
                break
