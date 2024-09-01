# https://www.acmicpc.net/problem/15650

def dfs(L, lst):
    global ans
    if L == m:
        ans.append([a[idx] for idx in lst])
        return
    if not lst:
        last_idx = -1
    else:
        last_idx = lst[-1]
    for i in range(last_idx+1, n):
        dfs(L+1, lst+[i])


n, m = map(int, input().split())
a = [_ for _ in range(1, n+1)]
ans = []
dfs(0, [])
for r in ans:
    print(*r)
