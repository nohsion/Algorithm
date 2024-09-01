# https://www.acmicpc.net/problem/15663

def dfs(L, lst):
    if L == M:
        ans.append([a[i] for i in lst])
        return
    prev = 0
    for j in range(N):
        if visited[j] == 0 and prev != a[j]:
            prev = a[j]
            visited[j] = 1
            dfs(L+1, lst+[j])
            visited[j] = 0


N, M = map(int, input().split())
a = list(map(int, input().split()))
visited = [0] * N
a.sort()
ans = []
dfs(0,[])
for lst in ans:
    print(*lst)
