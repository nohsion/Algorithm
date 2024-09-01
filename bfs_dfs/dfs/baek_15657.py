# https://www.acmicpc.net/problem/15657

def dfs(L, s, lst):
    if L == M:
        ans.append(lst)
        return
    for j in range(s, N):
        dfs(L+1, j, lst+[a[j]])


N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []
dfs(0, 0, [])
for lst in ans:
    print(*lst)
