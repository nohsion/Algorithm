# https://www.acmicpc.net/problem/15686

def chicken_dist(lst):
    sm = 0
    for home in hs:
        h_x, h_y = home
        mn = 2147000000
        for c in lst:
            c_x, c_y = c
            mn = min(mn, abs(h_x-c_x)+abs(h_y-c_y))
        sm += mn
    return sm


def dfs(L, s, lst):
    global ans
    if L == M:
        ch_dis = chicken_dist(lst)
        ans = min(ans, ch_dis)
        return
    for j in range(s, len(ch)):
        dfs(L+1, j+1, lst + [ch[j]])


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
hs = []  # 집 위치 리스트
ch = []  # 치킨집 위치 리스트
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            hs.append((i, j))
        elif graph[i][j] == 2:
            ch.append((i, j))

ans = 2147000000  # 도시 치킨거리 최솟값
# 치킨집 M개 선택 (조합)
dfs(0, 0, [])
print(ans)
