def dfs(n, sm, pi):
    global ans
    if n == N-1:
        sm += arr[pi][0]    # 도착지로 가는 비용 추가
        ans = min(ans, sm)
        return
    for ni in range(1, N):
        if v[ni] == 0:
            v[ni] = 1
            dfs(n+1, sm+arr[pi][ni], ni)
            v[ni] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v=[0]*(N+1)
    ans = 100*N
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")