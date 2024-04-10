# 각 격자칸에는 0은 빈칸, 1은 집, 2는 피자집으로 표현됩니다.
# 행번호는 1번부터 N번까지이고, 열 번호도 1부터 N까지입니다.
# 도시에는 각 집마다 "피자배달거리"가 았는데 각 집의 피자배달거리는 해당 집과 도시의 존재 하는 피자집들과의 거리 중 최소값을 해당 집의 "피자배달거리"라고 한다.
# 집과 피자집의 피자배달거리는 |x1-x2|+|y1-y2| 이다.
"""
pz = [(1,2),...]  # 피자 위치 리스트
hs = [(0,1),...]  # 집 위치 리스트
피자집 개수(P) 중에 M개를 선택해서, 각 조합의 경우마다 "피자배달거리"를 구하고, 최소값 출력.

조합 DFS - 4C2 이라 해보자.
                init                    D(0,0)
    (1)           (2)       (3)     (4) D(1)
(2) (3) (4)     (3) (4)     (4)         D(2)
"""
from collections import deque


# 피자배달거리 구하는 bfs 함수
def bfs_pizza_dis(hs_x, hs_y, pz_list):
    queue = deque()
    queue.append((hs_x, hs_y)) # 좌표 xy, 거리
    dis[hs_x][hs_y] = 0
    while queue:
        x, y = queue.popleft()
        if (x, y) in pz_list:
            return dis[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역 내에 있고, 방문하지 않았고, 0(빈칸)이라면
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and dis[nx][ny] == -1 and graph[nx][ny] != 1:
                dis[nx][ny] = dis[x][y] + 1
                queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 피자집 M개 선택하는 dfs 함수 (조합)
def dfs(L, s):
    if L == m:
        pz_list = []
        for i in range(pz_cnt):
            if ch[i] == 1:
                pz_list.append(pz[i])
        selected_pz.append(pz_list)
        return
    for i in range(s, pz_cnt):
        ch[i] = 1
        dfs(L+1, i+1)
        ch[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph, hs, pz = [], [], []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            if graph[i][j] == 1:
                hs.append((i, j))
            elif graph[i][j] == 2:
                pz.append((i, j))
    # 피자 M개 조합 선택
    pz_cnt = len(pz)
    ch = [0] * pz_cnt
    selected_pz = []
    dfs(0, 0)

    # 각 조합의 피자배달거리 계산
    min_hp = 2147000
    for sp in selected_pz:
        hs_to_pz = 0
        for h in hs:
            dis = [[-1] * n for _ in range(n)]  # 거리 저장
            hs_to_pz += bfs_pizza_dis(h[0], h[1], sp)
        if hs_to_pz < min_hp:
            min_hp = hs_to_pz
    print(min_hp)
