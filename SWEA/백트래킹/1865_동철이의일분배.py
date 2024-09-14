# 백트래킹 풀이 방식
# def dfs(n, prod):
#     global ans
#     # 가지치기
#     if prod <= ans:
#         return
#     if n == N:
#         ans = max(ans, prod)
#         return
#     for i in range(N):
#         if v[i] == 0:
#             v[i] = 1
#             dfs(n+1, prod*arr[n][i]*0.01)
#             v[i] = 0

# 메모이제이션 풀이 방식
def dfs(n, bits):
    if n == N:
        return 1
    if mem[bits] == 0:  # 호출된적 없음 -> 계산후 최대값 저장해놓기
        mx = 0
        for i in range(N):
            if bits & (1<<i) == 0:  # 미방문
                mx = max(mx, dfs(n+1, bits+(1<<i))*arr[n][i]*0.01)
        mem[bits] = mx
    return mem[bits]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # dfs 풀이방식
    # v = [0]*N
    # ans = 0
    # dfs(0, 1)

    # 메모이제이션 풀이방식
    mem = [0]*(2**N)
    ans = dfs(0, 0)

    print(f"#{test_case} {round(ans*100, 6):.6f}")