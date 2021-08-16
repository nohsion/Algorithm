#  8 x 8 좌표 평면인 왕실 정원에서 나이트가 이동합니다.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동 / 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 나이트의 위치 (c2: 행 2, 열 c)가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 구하시오

data = input()
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

column = data[0]
row = int(data[1])
i = columns.index(column)
# (column, row)
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

count = 0
for k in range(8):
    n_column = i + steps[k][0]
    n_row = row + steps[k][1]
    if n_column > 7 or n_column < 0 or n_row > 8 or n_row < 1:
        continue
    count += 1
    co, ro = n_column, n_row
    print(co, ro)

print(count)