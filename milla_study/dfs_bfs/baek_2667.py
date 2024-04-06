# https://www.acmicpc.net/problem/2667


def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


if __name__ == '__main__':
    n = int(input())
    graph = []  # 그래프
    for i in range(n):
        graph.append(list(map(int, input())))

    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    home_cnt = []  # 각 단지내 집의 개수
    cnt = 0  # 한 단지 내에 집이 몇 개인지 셀 변수
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                home_cnt.append(cnt)
                cnt = 0

    print(len(home_cnt))
    for h in sorted(home_cnt):
        print(h)
