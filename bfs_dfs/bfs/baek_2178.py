# https://www.acmicpc.net/problem/2178
# NxM 미로에서, (1,1) -> (N,M) 으로 가는 최소의 칸 수를 구하시오.
# 미로에서 1은 이동 가능하고, 0은 이동할 수 없다.
from collections import deque


def bfs(si, sj):
    # [1] q=[] 큐, v 방문데이터 초기화
    q = deque()
    v = [[0]*M for _ in range(N)]
    # [2] 초기데이터 삽입
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        # [3] 현재값 확인, 종료조건
        ci, cj = q.popleft()
        if ci == N-1 and cj == M-1:
            return v[ci][cj]
        # [4] 네방향, 벽X, 미방문, 1(이동가능)이면
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return 0


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

res = bfs(0, 0)
print(res)
