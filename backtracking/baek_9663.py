# https://www.acmicpc.net/problem/9663

def dfs(L):
    global ans
    if L == n:
        ans += 1
        return
    for j in range(n):
        if v1[j] == v2[L+j] == v3[L-j] == 0:
            v1[j] = v2[L+j] = v3[L-j] = 1
            dfs(L+1)
            v1[j] = v2[L + j] = v3[L - j] = 0


ans = 0
n = int(input())
visited = [0] * (n+1)
# 룩업 테이블
v1, v2, v3 = [0] * n, [0] * (2*n), [0] * (2*n)  # 위, 대각선 오른쪽 위, 대각선 왼쪽 위
dfs(0)
print(ans)
