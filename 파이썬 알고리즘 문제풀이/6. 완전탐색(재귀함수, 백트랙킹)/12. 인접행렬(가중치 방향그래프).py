# 그래프 정보를 인접행렬로 표현하기
# 연결정보와 거리비용이 주어질 때, 인접행렬을 출력하세요.
# 정점의 수 N, 간선의 수 M.

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[0] * (n) for _ in range(n)]
    for _ in range(m):
        i, j, cost = map(int, input().split())
        graph[i-1][j-1] = cost

    for g in graph:
        print(*g)
