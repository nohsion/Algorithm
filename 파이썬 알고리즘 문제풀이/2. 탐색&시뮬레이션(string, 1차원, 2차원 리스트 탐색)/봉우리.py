n = int(input())
maps = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
maps.insert(0, [0] * (n+2))
maps.append([0] * (n+2))

# 1. 내 풀이
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        target = maps[i][j]
        u = maps[i-1][j]  # 상
        d = maps[i+1][j]  # 하
        l = maps[i][j-1]  # 좌
        r = maps[i][j+1]  # 우
        if target > u and target > d and target > l and target > r:
            cnt += 1
print(cnt)


# 2. 모범 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(maps[i][j] > maps[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
