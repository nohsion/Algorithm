T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*(i+1) for i in range(N)]
    arr[0][0] = 1

    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                arr[i][j] = arr[i-1][j]
            elif j == i:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print(f"#{test_case}")
    for lst in arr:
        print(*lst)