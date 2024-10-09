def solve(n, lst):
    # [1] 인접, 비어있는칸 카운트
    v = [[(0,0)]*(N+1) for _ in range(N+1)]
    mx_like = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] != 0:  # 이미 학생이 앉아있으면, continue
                continue
            like = empty = 0
            for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
                ni, nj = i+di, j+dj
                if 1<=ni<=N and 1<=nj<=N:   # 범위내
                    if arr[ni][nj] in lst:  # 인접칸에 좋아하는 애가 있다면
                        like += 1
                    if arr[ni][nj] == 0:    # 인접칸이 비어있다면
                        empty += 1
            v[i][j] = (like, empty)
            mx_like = max(mx_like, like)

    # [2] 자리 찾기
    mx_empty, mx_i, mx_j = -1, 0, 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            clike, cempty = v[i][j]
            if arr[i][j] == 0 and clike == mx_like:    # 해당칸이 비어 있고, 좋아하는애가 가장 많은 인접칸이라면 후보임.
                if cempty > mx_empty:
                    mx_empty, mx_i, mx_j = cempty, i, j
    return mx_i, mx_j


N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
likes = {}
for _ in range(N*N):
    tlst = list(map(int, input().split()))
    n, lst = tlst[0], tlst[1:5]
    likes[n] = lst
    ti, tj = solve(n, lst)
    arr[ti][tj] = n

# 만족도 총합 구하기
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        cnt, num = 0, arr[i][j]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):   # 인접한 곳에 좋아하는애 카운트
            ni, nj = i + di, j + dj
            if 1<=ni<=N and 1<=nj<=N and arr[ni][nj] in likes[num]:
                cnt += 1
        if cnt > 0:
            ans += 10**(cnt-1)
print(ans)