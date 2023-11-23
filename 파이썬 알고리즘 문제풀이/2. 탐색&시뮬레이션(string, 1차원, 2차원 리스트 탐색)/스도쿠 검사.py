# 9X9 스도쿠 퍼즐이 정확히 풀었으면 YES, 틀렸으면 NO
puzzle = [list(map(int, input().split())) for _ in range(9)]


def check_row_col(puzzle: list[list[int]]):
    for i in range(9):
        row, col = [0] * 9, [0] * 9
        for j in range(9):
            row[puzzle[i][j]-1] = 1
            col[puzzle[j][i]-1] = 1
        if any(x == 0 for x in row + col):
            return False
    return True


# 내 풀이 (그룹탐색 3X3)
def check_board(puzzle: list[list[int]]):
    p1, p2, p3 = [0] * 9, [0] * 9, [0] * 9
    for i in range(9):
        for j in range(0, 3):
            p1[puzzle[i][j] - 1] = 1
        for j in range(3, 6):
            p2[puzzle[i][j] - 1] = 1
        for j in range(6, 9):
            p3[puzzle[i][j] - 1] = 1

        if i % 3 == 2:
            if any(x == 0 for x in p1 + p2 + p3):
                return False
            p1 = p2 = p3 = [0] * 9
    return True


# 모범 답안 (그룹탐색 3X3)
def check_board_mobum(puzzle: list[list[int]]):
    """
    아이디어: 9X9는 3X3짜리 크게 보면 9개의 그룹으로 나눌 수 있다.
    크게 9그룹으로 나누고, 세부적으로 각 요소별로 9개로 계산한다.

    [
        000     000     000
        000     000     000
        000     000     000

        000     000     000
        000     000     000
        000     000     000

        000     000     000
        000     000     000
        000     000     000
    ]
    """
    for i in range(3):
        for j in range(3):
            ch = [0] * 9
            for k in range(3):
                for s in range(3):
                    ch[puzzle[3*i+k][3*j+s]-1] = 1
            if any(x == 0 for x in ch):
                return False
    return True


if check_row_col(puzzle) and check_board_mobum(puzzle):
    print('YES')
else:
    print('NO')
