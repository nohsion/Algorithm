# https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(si, sj):
    global v, N, arr
    # [1] q 초기화
    q = deque()
    # [2] 초기데이터
    q.append((si, sj))
    v[si][sj] = 1

    cnt = 1
    while q:
        ci, cj = q.popleft()
        # 네방향, 벽X, 미방문, 1이면
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*N for _ in range(N)]  # v 방문데이터 초기화

danji_cnt, home_cnt = 0, []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0:
            home_cnt.append(bfs(i, j))
            danji_cnt += 1
print(danji_cnt)
for hc in sorted(home_cnt):
    print(hc)
