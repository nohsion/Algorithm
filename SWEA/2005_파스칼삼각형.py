T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 앞에 0으로 패딩 붙이기 -> 복잡한 문제이면, 이렇게 처리하는게 조건이 간단해짐
    arr = [[0]*(N+1) for i in range(N+1)]
    arr[1][1] = 1

    for i in range(2, N+1):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print(f"#{test_case}")
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(arr[i][j], end=' ')
        print()