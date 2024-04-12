# https://www.acmicpc.net/problem/1182

def dfs(L, sm, cnt):
    global ans
    if L == N:
        if sm == S and cnt > 0:
            ans += 1
        return
    dfs(L+1, sm+a[L], cnt+1)
    dfs(L + 1, sm, cnt)


N, S = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)
