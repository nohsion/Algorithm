# 그림1과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""
DFS
1. 종료조건 - 딱히 없음. 인접노드에 1이 없으면 끝나는 것
2. 방문체크 - graph[nx][ny] == 0 체크
"""

def dfs(x, y):
    global home_cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            home_cnt += 1
            dfs(nx, ny)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    danji_cnt, home_cnt = 0, 0
    home = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                danji_cnt += 1
                home.append(home_cnt)
                home_cnt = 0
    print(danji_cnt)
    for h in sorted(home):
        print(h)
