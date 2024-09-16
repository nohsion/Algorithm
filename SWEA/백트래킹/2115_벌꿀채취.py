def dfs(n, cnt, sm, ci, cj):
    global mx
    if cnt > C: # 가지치기: 합친 꿀의 양이 C보다 큰 경우
        return
    if n==M:
        mx = max(mx, sm)
        return
    honey = arr[ci][cj+n]
    # 포함 O
    dfs(n+1, cnt+honey, sm+honey**2, ci, cj)
    # 포함 X
    dfs(n+1, cnt, sm, ci, cj)


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = mx = sm1 = 0
    # 메모이제이션 방식
    mem = [[0]*N for _ in range(N)]
    # [0] 각 위치의 가능한 최대값을 미리 저장
    # 동일한 위치(ci,cj)에서 dfs를 호출해서 중복연산 방지
    for i in range(N):
        for j in range(N-M+1):
            mx = 0
            dfs(0, 0, 0, i, j)
            mem[i][j] = mx
    # [1] 가능한 모든 시작위치 (일꾼1, 일꾼2)
    for i1 in range(N):
        for j1 in range(N-M+1):
            for i2 in range(i1, N):
                sj = j1+M if i1==i2 else 0
                for j2 in range(sj, N-M+1):
                    ans = max(ans, mem[i1][j1]+mem[i2][j2])

    # 백트래킹 방식
    # # [1] 가능한 모든 시작위치 (일꾼1, 일꾼2)
    # for i1 in range(N):
    #     for j1 in range(N-M+1):
    #         mx = 0
    #         dfs(0, 0, 0, i1, j1)
    #         sm1 = mx
    #         for i2 in range(i1, N):
    #             sj = j1+M if i1==i2 else 0
    #             for j2 in range(sj, N-M+1):
    #                 mx = 0
    #                 dfs(0, 0, 0, i2, j2)
    #                 ans = max(ans, sm1+mx)

    print(f"#{test_case} {ans}")