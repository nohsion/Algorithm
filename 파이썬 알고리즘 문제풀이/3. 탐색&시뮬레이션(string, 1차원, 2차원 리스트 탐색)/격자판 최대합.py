# n*n 격자판에서 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력하기
n = int(input())
# [[10,13,10,12,15],[12,39,30,23,11], ...]
matrix: list[list[int]] = [list(map(int, input().split())) for _ in range(n)]

# 행, 열
largest = 0
for i in range(n):
    sum_row, sum_col = 0, 0
    for j in range(n):
        sum_row += matrix[i][j]  # 00 01 02 03 04
        sum_col += matrix[j][i]  # 00 10 20 30 40
    if sum_row > largest:
        largest = sum_row
    if sum_col > largest:
        largest = sum_col

# 대각선 (우하향, 좌하향)
sum_r, sum_l = 0, 0
for i in range(n):
    sum_r += matrix[i][i]
    sum_l += matrix[i][-1-i]
if sum_r > largest:
    largest = sum_r
if sum_l > largest:
    largest = sum_l
print(largest)
