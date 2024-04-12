# https://www.acmicpc.net/problem/15651

def dfs(L, lst):
    global ans
    if L == m:
        ans.append(lst)
        return
    for i in range(1, n+1):
        dfs(L+1, lst+[i])


n, m = map(int, input().split())
ans = []
dfs(0, [])
for a in ans:
    print(*a)
