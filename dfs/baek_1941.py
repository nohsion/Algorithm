# https://www.acmicpc.net/problem/1941

def dfs(L, tlst, s_cnt):
    global ans
    if L == 7:
        if s_cnt >= 4 and tlst not in lst_set:
            lst_set.append(tlst)
            ans += 1
        return
    for cx, cy in tlst:  # 모든 요소에서 DFS 실행 (중요!)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and v[nx][ny] == 0:
                v[nx][ny] = 1
                dfs(L+1, tlst | {(nx, ny)}, s_cnt+int(graph[nx][ny] == 'S'))
                v[nx][ny] = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = [list(input()) for _ in range(5)]
v = [[0] * 5 for _ in range(5)]
ans = 0
lst_set = []
for i in range(5):
    for j in range(5):
        v[i][j] = 1
        dfs(1, {(i, j)}, int(graph[i][j] == 'S'))
print(ans)
