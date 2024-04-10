def rotate_zip():
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    for a in arr:
        print(*a)
    print()

    ## zip
    # 시계 방향 90 (= 반시계 방향 270)
    arr_90 = list(map(list, zip(*arr[::-1])))
    for a in arr_90:
        print(*a)
    print()

    # 시계 방향 180 (= 반시계 방향 180)
    arr_180 = [a[::-1] for a in arr[::-1]]
    for a in arr_180:
        print(*a)
    print()

    # 시계 방향 270 (= 반시계 방향 90)
    arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
    for a in arr_270:
        print(*a)
    print()


def rotate_idx_square():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = 3
    for a in arr:
        print(*a)
    print()

    # 시계 방향 90
    arr_90 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_90[j][n-i-1] = arr[i][j]
    for a in arr_90:
        print(*a)
    print()

    # 시계 방향 180
    arr_180 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_180[n-i-1][n-j-1] = arr[i][j]
    for a in arr_180:
        print(*a)
    print()

    # 시계 방향 270
    arr_270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_270[n-j-1][i] = arr[i][j]
    for a in arr_270:
        print(*a)
    print()


def rotate_idx_rect():
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    n = len(arr)
    m = len(arr[0])
    for a in arr:
        print(*a)
    print()

    # 시계 방향 90
    arr_90 = [[0] * n for _ in range(m)]  # 배열 가로, 세로 길이 뒤바뀜
    for i in range(n):
        for j in range(m):
            arr_90[j][n-i-1] = arr[i][j]
    for a in arr_90:
        print(*a)
    print()

    # 시계 방향 180
    arr_180 = [[0] * m for _ in range(n)]
    for i in range(n):  # 세로
        for j in range(m):  # 가로
            arr_180[n-i-1][m-j-1] = arr[i][j]
    for a in arr_180:
        print(*a)
    print()

    # 시계 방향 270
    arr_270 = [[0] * n for _ in range(m)]  # 배열 가로, 세로 길이 뒤바뀜
    for i in range(n):
        for j in range(m):
            arr_270[m-j-1][i] = arr[i][j]
    for a in arr_270:
        print(*a)
    print()


def rotate_partial():
    # 7X7 배열
    arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
    new_arr = [[0] * 7 for _ in range(7)]
    sy, sx = 2, 2
    length = 3

    # 배열의 특정 부분(정사각형)을 회전시킴
    def rotate_90(sy, sx, length):
        # 정사각형을 시계방향으로 90도 회전
        for y in range(sy, sy + length):
            for x in range(sx, sx + length):
                # 1단계 : (0,0)으로 옮겨주는 변환을 진행함
                oy, ox = y - sy, x - sx
                # 2단계 : 90도 회전했을때의 좌표를 구함
                ry, rx = ox, length - oy - 1
                # 3단계 : 다시 (sy,sx)를 더해줌
                new_arr[sy + ry][sx + rx] = arr[y][x]

        # new_arr 값을 현재 board에 옮겨줌
        for y in range(sy, sy + length):
            for x in range(sx, sx + length):
                arr[y][x] = new_arr[y][x]
                # print(arr[y][x])

    rotate_90(sy, sx, length)
    for a in arr:
        print(*a)


if __name__ == '__main__':
    print("1. zip() 활용해서 회전 - 정사각형 & 직사각형")
    rotate_zip()
    print("--------------------------------------------------")

    print("2. 인덱스 활용해서 회전 - 정사각형")
    rotate_idx_square()
    print("--------------------------------------------------")

    print("3. 인덱스 활용해서 회전 - 직사각형")
    rotate_idx_rect()
    print("--------------------------------------------------")

    print("4. 부분 회전 - 2차원 배열")
    rotate_partial()
    print("--------------------------------------------------")

