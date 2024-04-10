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

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 피자집 M개 선택하는 dfs 함수 (조합)
def dfs(L, s):
    global res
    if L == m:
        d_sum = 0  # 도시 피자배달거리
        for i in range(len(hs)):
            hs_x, hs_y = hs[i][0], hs[i][1]
            dis = 2147000000
            for j in cb:
                pz_x, pz_y = pz[j][0], pz[j][1]
                dis = min(dis, abs(hs_x-pz_x) + abs(hs_y-pz_y))
            d_sum += dis
        if d_sum < res:
            res = d_sum
        return
    for i in range(s, len(pz)):
        cb[L] = i  # 조합 경우에 pz 인덱스를 넣어줌
        dfs(L+1, i+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    hs, pz, cb = [], [], [0]*m  # 집 좌표, 피자 좌표, 피자 조합 경우
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                hs.append((i, j))
            elif graph[i][j] == 2:
                pz.append((i, j))
    res = 2147000000  # M개의 피자집 선택 경우 중 최소 피자배달거리
    dfs(0, 0)
    print(res)
