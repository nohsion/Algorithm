# 방향그래프에서 1번~N번 정점으로 가는 모든 경로의 수를 출력하세요.
"""
1 -> 2 -> 3 -> 4 -> 5
"""
def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(1, n+1):
        # 아직 방문하지 않았는데 연결되어 있다면
        if graph[x][i] == 1 and ch[i] == 0:
            ch[i] = 1
            dfs(i)
            ch[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)  # 체크 변수는 1차원으로 하면 됨
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i][j] = 1
    cnt = 0
    ch[1] = 1  # 초기화 중요
    dfs(1)
    print(cnt)
