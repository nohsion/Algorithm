def is_same(ci, ni):
    # 맞닿은 극이 같은지 판단
    if ci < ni: # 뒤쪽 검사
        return arr[ci][2] == arr[ni][-2]
    if ni < ci: # 앞쪽 검사
        return arr[ni][2] == arr[ci][-2]
    return False

def rotate(n, dr):
    q = arr[n]
    if dr == 1:     # 시계방향 회전
        q.insert(0, q.pop())
    elif dr == -1:  # 반시계방향 회전
        q.append(q.pop(0))

def bfs(si, sd):
    v = [0]*(N+1)
    q = []

    v[si] = 1
    q.append((si, sd))

    while q:
        ci, cd = q.pop(0)
        ans_lst.append((ci, cd))
        for ni in (ci-1, ci+1):         # 앞뒤 확인
            if 1<=ni<=N and v[ni] == 0: # 범위내, 미방문
                if not is_same(ci, ni): # 맞닿은 극이 다르면, 반대방향으로 회전시킨다.
                    v[ni] = 1
                    q.append((ni, cd*(-1)))

N = 4
arr = [[0]*8]
for _ in range(N):
    arr.append(list(map(int, input())))
K = int(input()) # 회전 횟수

for _ in range(K):
    ans_lst = []  # 회전시킬 (idx, dr) 모아놓고, 마지막에 한번에 회전시킨다.
    idx, dr = map(int, input().split()) # 톱니바퀴 idx, 돌릴 방향 dr
    bfs(idx, dr)
    for idx, dr in ans_lst:
        rotate(idx, dr)

# 점수의 합
ans = 0
for i in range(1, 5):
    if arr[i][0] == 1:
        ans += 2**(i-1)
print(ans)