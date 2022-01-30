n, m = map(int, input().split())

ice_teul = [[0] * m for _ in range(n)] # 얼음틀 0으로 초기화

for i in range(n):
  ice_teul[i] = list(map(int, input()))

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  
  if ice_teul[x][y] == 0:
    ice_teul[x][y] = 2 # 방문처리
    dfs(x-1, y) # 상
    dfs(x+1, y) # 하
    dfs(x, y-1) # 좌
    dfs(x, y+1) # 우
    return True
  else:
    return False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j):
      result += 1

print(result)
