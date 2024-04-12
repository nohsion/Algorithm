# https://www.acmicpc.net/problem/15652

def dfs(L, s, lst):
    if L == M:
        ans.append(lst)
        return
    for i in range(s, N+1):
        dfs(L+1, i, lst+[i])


N, M = map(int, input().split())
ans = []
dfs(0, 1, [])
for lst in ans:
    print(*lst)
