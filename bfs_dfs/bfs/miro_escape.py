from collections import deque

n, m = map(int, input().split())

miro = [[0]*m for _ in range(n)]
for i in range(n):
  miro[i] = list(map(int, input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
  queue = deque([start])
  
  while queue:
    x, y = queue.popleft()

    # 상,하,좌,우 살펴보기
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      # 영역 벗어나면 다음 꺼로
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 1이 아니면 다음 꺼로
      if miro[nx][ny] != 1:
        continue
      # 첫 스타트인 [0,0]는 제외
      if nx == 0 and ny == 0:
        continue
      # 1인 경우만
      if miro[nx][ny] == 1:
        miro[nx][ny] += miro[x][y]
        if nx == n-1 and ny == m-1:
          return miro[nx][ny]
        queue.append([nx, ny])


print(bfs([0, 0]))
