n = int(input())  # n은 항상 홀수라고 가정
farm = [list(map(int, input().split())) for _ in range(n)]

is_grow: bool = True
p1 = p2 = n // 2  # 투 포인터
apples = 0
for i in range(n):
    for j in range(p1, p2+1):
        apples += farm[i][j]
    if p1 == 0 and p2 == n-1:
        is_grow = False
    if is_grow:
        p1 -= 1
        p2 += 1
    else:
        p1 += 1
        p2 -= 1
print(apples)
