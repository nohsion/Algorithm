# https://www.acmicpc.net/problem/15649

def dfs(L, lst):
    if L == m:
        ans.append(lst[:])
        return
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(L+1, lst+[i])
            visited[i] = 0


ans = []
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
visited = [0] * (n+1)
dfs(0, [])
for a in ans:
    print(*a)
