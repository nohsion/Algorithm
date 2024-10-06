# 경로 상에 등장하는 정점의 개수의 최대값 -> 최대의 경로를 구하려면 DFS

def dfs(c):
    global ans
    ans = max(ans, max(v))
    for n in adj[c]:
        if v[n] == 0:
            v[n] = v[c] + 1
            dfs(n)
            v[n] = 0


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    v = [0]*(N+1)
    ans = 0
    for i in range(1, N+1): # 1~N
        if v[i] == 0:   # 미방문이면 dfs 탐색
            v[i] = 1
            dfs(i)
            v[i] = 0

    print(f"#{test_case} {ans}")