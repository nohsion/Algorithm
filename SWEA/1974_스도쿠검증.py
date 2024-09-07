# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq

def check_row():
    for lst in arr:
        if len(set(lst)) != 9:
            return 0
    return 1

def check_col():
    transpose_arr = list(zip(*arr))
    for lst in transpose_arr:
        if len(set(lst)) != 9:
            return 0
    return 1


def check_block():
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            lst = []
            for idx in range(3):
                lst.extend(arr[i+idx][j:j+3])
            if len(set(lst)) != 9:
                return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 행
    row_result = check_row()
    # 열
    col_result = check_col()
    # 3x3 블럭
    block_result = check_block()
    if row_result == 1 and col_result == 1 and block_result == 1:
        ans = 1
    print(f"#{test_case} {ans}")
