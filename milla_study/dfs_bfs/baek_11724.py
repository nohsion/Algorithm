# https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(50_000)


def dfs(x):
    global visited
    visited[x] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[x][i] == 1:
            dfs(i)


if __name__ == '__main__':
    # 정점 개수 n, 간선 개수 m
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0] * (n+1) for _ in range(n+1)]  # 그래프
    visited = [0] * (n+1)  # 방문 처리
    for _ in range(m):
        gx, gy = map(int, sys.stdin.readline().split())
        graph[gx][gy] = 1
        graph[gy][gx] = 1  # 처음에 얘를 빼도 되는 줄 알고 뺐다가, 틀렸음.

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1

    print(cnt)
