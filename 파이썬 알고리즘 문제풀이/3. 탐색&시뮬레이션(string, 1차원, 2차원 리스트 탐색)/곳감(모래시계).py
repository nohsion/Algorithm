n = int(input())  # n은 항상 홀수라고 가정
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
command = [list(map(int, input().split())) for _ in range(m)]
# 2 0 3 이면, 2번째 행을 왼쪽으로 3만큼 이동

# 1. 내 풀이
# for c in command:
#     row_num: int = c[0] - 1
#     is_right: bool = bool(c[1])
#     cnt: int = c[2]
#     row = matrix[row_num]  # 내용물을 이동시킬 행
#     snapshot = [r for r in row]
#     for i in range(n):
#         idx = (i - cnt) % n if is_right else (i + cnt) % n
#         row[i] = snapshot[idx]
#     matrix[row_num] = row
#
# is_down = True
# gams = 0
# p1, p2 = 0, n
# for i in range(n):
#     if p1 == n // 2:
#         is_down = False
#     for j in range(p1, p2):
#         gams += matrix[i][j]
#     if is_down:
#         p1 += 1
#         p2 -= 1
#     else:
#         p1 -= 1
#         p2 += 1
# print(gams)

# 2. 모범 풀이
for c in command:
    h, t, k = c[0], c[1], c[2]
    row = matrix[h - 1]
    if t == 0:
        for _ in range(k):
            # 중요: pop(0)한 다음에 뒤에다가 붙이면, 왼쪽으로 한번의 회전이 일어난 것과 같음.
            row.append(row.pop(0))
    else:
        for _ in range(k):
            # 중요: pop()한 다음에 앞에다가 붙이면, 오른쪽으로 한번의 회전이 일어난 것과 같음.
            row.insert(0, row.pop())

res = 0
p1, p2 = 0, n - 1
for i in range(n):
    for j in range(p1, p2 + 1):
        res += matrix[i][j]
    if i < n // 2:
        p1 += 1
        p2 -= 1
    else:
        p1 -= 1
        p2 += 1
print(res)
