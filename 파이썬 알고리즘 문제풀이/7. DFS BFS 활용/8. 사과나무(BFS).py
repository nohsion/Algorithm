# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다.
# N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때
# 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
"""
마름모 탐색 - BFS로 풀어보기
BFS(L, x, y)
cnt = 0
center = (n//2, n//2)
- 동서남북으로 점차 넓혀나감
    - dx=[0,0,1,-1]
    - dy=[1,-1,0,0]
    - 조건
        - 범위 내여야 함 0 <= nx(ny) <= n-1
        - 아직 방문하지 않아야 함. visited 체크해주기
- 종료조건
    - L == center:
        - 더이상 뻗지않고 종료
    - 현재 요소(x,y)
        - (x == 0 or x == n-1) and y!=center 또는
        - (y == 0 or y == n-1) and x!=center
"""
from collections import deque


def bfs(L, x, y):
    global cnt
    queue = deque()
    queue.append((L, x, y))
    cnt += graph[x][y]  # 사과 수확
    visited[x][y] = 1  # 방문처리
    while queue:
        qL, qx, qy = queue.popleft()
        if qL == center:
            return
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            # 범위 내에 있고, 방문하지 않았다면
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0:
                if ((nx == 0 or nx == n-1) and ny != center) or ((ny == 0 or ny == n-1) and nx != center):
                    continue
                cnt += graph[nx][ny]  # 사과수확
                visited[nx][ny] = 1  # 방문처리
                queue.append((qL+1, nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    n = int(input())
    center = n // 2  # 중앙값
    graph = []  # 그래프 (사과밭)
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    bfs(0, center, center)
    print(cnt)
