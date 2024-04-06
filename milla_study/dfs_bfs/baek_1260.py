# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(x):
    dfs_visited[x] = 1
    print(x, end=' ')
    # 방문 기록이 없고, 그래프가 연결되어 있다면
    for i in range(1, n+1):
        if dfs_visited[i] == 0 and graph[x][i] == 1:
            dfs(i)


def bfs(x):
    queue = deque([x])
    bfs_visited[x] = 1  # 첫 노드 방문 처리
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        # 방문 기록이 없고, 그래프가 연결되어 있다면
        for i in range(n+1):
            if bfs_visited[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                bfs_visited[i] = 1


if __name__ == '__main__':
    # 정점 개수 n, 간선 개수 m, 탐색 시작할 정점 번호 v
    n, m, v = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    # 그래프 연결 여부 표시
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    # 방문기록 리스트
    dfs_visited = [0] * (n + 1)
    bfs_visited = [0] * (n + 1)

    dfs(v)
    print()
    bfs(v)
