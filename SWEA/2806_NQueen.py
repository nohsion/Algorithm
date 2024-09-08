def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    for j in range(N):
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0:
            # 방문표시 체크
            v1[j] = 1
            v2[n+j] = 1
            v3[n-j] = 1
            dfs(n+1)
            # 방문표시 해제
            v1[j] = 0
            v2[n+j] = 0
            v3[n-j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    v1 = [0]*N  # 위쪽
    v2 = [0]*(N*2) # 오른쪽위 대각 (i+j)
    v3 = [0]*(N*2) # 왼쪽위 대각 (i-j)

    ans = 0
    dfs(0)
    print(f"#{test_case} {ans}")