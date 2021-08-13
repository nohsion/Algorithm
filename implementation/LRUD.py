# N x N 크기의 정사각형 공간에서 상, 하, 좌, 우 방향으로 이동
# 공간을 벗어나는 움직임은 무시됩니다.

n = int(input())
plans = input().split()

x, y = 1, 1  # 각 위치를 (x, y)라고 하자.
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    i = move_types.index(plan)
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)