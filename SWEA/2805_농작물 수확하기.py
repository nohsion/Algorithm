T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = N//2
    arr = [list(map(int, input())) for _ in range(N)]

    sm = 0
    # for i in range(N):
    #     if i <= M:
    #         for j in range(M-i, M+i+1):
    #             sm += arr[i][j]
    #     else:
    #         for j in range(i-M, N-(i-M)):
    #             sm += arr[i][j]

    s = e = M
    for i in range(N):
        sm += sum(arr[i][s:e+1])
        if i < M:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f"#{test_case} {sm}")