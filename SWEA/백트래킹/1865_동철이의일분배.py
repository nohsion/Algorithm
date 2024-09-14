def dfs(n, prod):
    global ans
    # 가지치기
    if prod <= ans:
        return
    if n == N:
        ans = max(ans, prod)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, prod*arr[n][i]*0.01)
            v[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0]*N
    ans = 0
    dfs(0, 1)
    print(f"#{test_case} {round(ans*100, 6):.6f}")