# https://www.acmicpc.net/problem/14503

d = [(-1,0), (0,1), (1,0), (0,-1)] # 북 동 남 서

def empty(ci, cj):
    # 4방향 / 범위내, 벽X, 미방문 판별
    for di, dj in d:
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 1 and v[ni][nj] == 0:
            return True
    return False

def dfs(ci, cj, dr):
    # 청소
    v[ci][cj] = 1
    if empty(ci, cj):           # 4칸중 청소되지 않은 빈칸 있는지 판단
        nr = (dr-1)%4           # 반시계 90도 회전
        di, dj = d[nr]
        ni, nj = ci+di, cj+dj   # 바라보는 방향 앞쪽 칸
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 1 and v[ni][nj] == 0:
            dfs(ni, nj, nr)
        else:
            dfs(ci, cj, nr)
    else:
        di, dj = d[dr]
        ni, nj = ci-di, cj-dj   # 바라보는 방향 뒤쪽 칸 (후진 1칸)
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 1:
            dfs(ni, nj, dr)
        else:       # 후진할 수 없다면 작동 중지!
            return  # 이게 맞나?

N, M = map(int, input().split())
si, sj, sd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
dfs(si, sj, sd)

ans = 0
for lst in v:
    ans += sum(lst)
print(ans)