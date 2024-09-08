def dfs(ci, cj, num: int, cnt: int):
    if cnt == 7:
        ans.add(num)
        return
    # 네방향, 범위내
    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N:
            dfs(ni, nj, num*10 + arr[ni][nj], cnt+1)

T = int(input())
for test_case in range(1, T + 1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = set()
    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j], 1)

    print(f"#{test_case} {len(ans)}")
