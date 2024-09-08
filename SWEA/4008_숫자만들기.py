def dfs(n, num):
    global mx, mn
    if n == N-1:
        mx = max(mx, num)
        mn = min(mn, num)
        return
    for ni in range(4):
        if op[ni] > 0:
            op[ni] -= 1
            if ni == 0: # +
                dfs(n + 1, num + lst[n+1])
            elif ni == 1: # -
                dfs(n + 1, num - lst[n+1])
            elif ni == 2:  # *
                dfs(n + 1, num * lst[n+1])
            elif ni == 3:  # / --> 음수일때 // 처리하면 연산결과가 달라지므로, int(n1/n2)로 해야 함
                dfs(n + 1, int(num / lst[n+1]))
            op[ni] += 1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    op = list(map(int, input().split()))    # 연산자 (+,-,*,/)의 개수
    lst = list(map(int, input().split()))   # 피연산자: N개

    mx, mn = -100_000_000, 100_000_000
    dfs(0, lst[0])
    ans = mx - mn
    print(f"#{test_case} {ans}")