# https://www.acmicpc.net/problem/15656


def dfs(L, lst):
    if L == M:
        ans.append(lst)
        return
    for j in range(N):
        dfs(L+1, lst+[a[j]])


N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)
