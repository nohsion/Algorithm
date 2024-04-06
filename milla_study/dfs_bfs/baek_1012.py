# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(50_000)


def dfs(x, y):
    if x < 0 or y < 0 or x > n-1 or y > m-1:
        return

    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    T = int(input())  # 테스트 케이스 개수 T
    for _ in range(T):
        # 가로 m, 세로 n, 배추 개수 k
        m, n, k = map(int, input().split())
        graph = [[0] * m for _ in range(n)]  # 그래프 (배추밭)
        # 그래프 배추 표시 (연결 여부)
        for _ in range(k):
            by, bx = map(int, input().split())
            graph[bx][by] = 1
        cnt = 0  # 배추가 연결되어 있는 뭉탱이 개수
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        print(cnt)
