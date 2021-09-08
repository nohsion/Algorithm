n, m = map(int, input().split())  # n * m 맵
x, y, direction = map(int, input().split())  # 1 1 0 -> (1,1)에서 북쪽(0)을 바라보는 캐릭터

# 방문한 위치 저장하기 위한 2차원 array (게임 맵과 크기가 동일)
d = [[0] * m for _ in range(n)]
d[x][y] = 1

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

# 서 남 동 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def manual():
    tmp_x ,tmp_y = x, y
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > n or nx < 0 or ny > m or ny < 0 or d[nx][ny] == 1 or game_map[nx][ny] == 1:
            continue
        x, y = nx, ny
    if tmp_x == x and tmp_y == y:



# 캐릭터가 방문한 칸의 수 세기
count = 0
for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
            count += 1

print(count)
