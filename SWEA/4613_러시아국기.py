def count(color, arr_idx):
    sm = 0
    for n in arr[arr_idx]:
        if n != color:
            sm += 1
    return sm

def dfs(n, cnt, color_idx):
    global ans
    if n == N-1:
        if all(n > 0 for n in cnts): # B가 한번은 선택 되어야 함.
            ans = min(ans, cnt)
        return
    for i in range(color_idx, 3): # 현재 선택한 것 이후로만 가능 (순서 W -> B -> R)
        cnts[i] += 1
        dfs(n+1, cnt + count(colors[i], n), i)
        cnts[i] -= 1

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 0행: w 칠하기 / N-1행: r 칠하기
    init_cnt = count('W', 0) + count('R', N-1)

    ans = N * M
    colors = ['W', 'B', 'R']
    cnts = [1, 0, 1]
    dfs(1, init_cnt, 0)

    print(f"#{test_case} {ans}")