def dfs(ci, cj, concat: str):
    if len(concat) == 7:
        ans.add(concat)
        return
    # 네방향, 범위내
    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N:
            dfs(ni, nj, concat + str(arr[ni][nj]))

T = int(input())
for test_case in range(1, T + 1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = set()
    for i in range(N):
        for j in range(N):
            dfs(i, j, str(arr[i][j]))

    print(f"#{test_case} {len(ans)}")
