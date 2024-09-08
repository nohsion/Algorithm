def cook(lst):
    sm = 0
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            sm += arr[lst[i]][lst[j]]
    return sm

# n: 재료번호(idx)
def dfs(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == M:
            asum = cook(alst)
            bsum = cook(blst)
            ans = min(ans, abs(asum-bsum))
        return
    # a 선택
    dfs(n+1, alst + [n], blst)
    # b 선택
    dfs(n+1, alst, blst + [n])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = N//2
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 20_000 * (8*7)    # 20_000 * 8P2
    dfs(0, [], [])  # dfs에서 리스트 넘겨주는게 제일 편함.. (느리긴 하다)

    print(f"#{test_case} {ans}")