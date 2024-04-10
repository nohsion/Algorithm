# 마을 뒷산의 형태를 나타낸 지도는 N*N 구역으로 나뉘어져 있으며, 각 구역에는 높이가 함께 나타나 있습니다.
# 어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다.
# 등산로의 출발지는 전체 영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 출발지와 목적지는 유일합니다.
# 지도가 주어지면 출발지에서 도착지로 갈 수 있는 등산경로가 몇 가지인지 구하는 프로그램을 작성하세요.
"""
DFS
출발지: 가장 낮은 곳
목적지: 가장 높은 곳
<이동조건 - 동서남북>
1. 범위 내에 있고
2. 현재보다 높고
3. 방문하지 않아야 함.
<종료조건>
목적지에 도착하면 종료
"""


def dfs(x, y):
    global cnt
    if (x, y) == max_xy:
        cnt += 1
        return
    val = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] > val and visited[nx][ny] == 0:
            visited[nx][ny] = 1  # 방문 체크
            dfs(nx, ny)
            visited[nx][ny] = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[0] * n for _ in range(n)]  # 방문 체크
    maximum, max_xy = -1, (0, 0)
    minimum, min_xy = 2147000000, (0, 0)
    for i in range(n):
        for j in range(n):
            if graph[i][j] > maximum:
                maximum = graph[i][j]
                max_xy = (i, j)
            if graph[i][j] < minimum:
                minimum = graph[i][j]
                min_xy = (i, j)
    cnt = 0
    visited[min_xy[0]][min_xy[1]] = 1
    dfs(min_xy[0], min_xy[1])
    print(cnt)
