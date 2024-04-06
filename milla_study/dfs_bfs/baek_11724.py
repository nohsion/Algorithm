# https://www.acmicpc.net/problem/11724
import sys
from collections import deque
sys.setrecursionlimit(50_000)


def bfs(x):
    global visited
    queue = deque([x])
    visited[x] = 1
    while queue:
        q = queue.popleft()
        for i in range(1, n+1):
            if visited[i] == 0 and graph[q][i] == 1:
                visited[i] = 1
                queue.append(i)


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
            bfs(i)
            cnt += 1

    print(cnt)
