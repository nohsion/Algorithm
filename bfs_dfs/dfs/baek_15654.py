# https://www.acmicpc.net/problem/15654


def dfs(L, lst):
    if L == M:
        ans.append(lst)
        return
    for x in a:
        if x not in lst:
            dfs(L+1, lst+[x])


N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)
