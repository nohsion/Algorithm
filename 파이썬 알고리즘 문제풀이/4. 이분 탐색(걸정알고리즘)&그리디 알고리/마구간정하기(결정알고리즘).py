# n개의 마구간이 수직선상에 위치하는데, 현수는 c마리의 말을 최대한 멀리 떨어져 있게 하고싶다.
# 이때, 가장 가까운 두 말의 최대 거리를 구하세요.
n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

# 1, 2, 4, 8, 9
# mid가 가장 가까운 두 말의 최대거리라고 가정해보자. (결정 알고리즘의 핵심 아이디어)
x.sort()
p1, p2 = x[0], x[-1]
res = 0
while p1 <= p2:
    mid = (p1 + p2) // 2
    base, cnt = x[0], 1
    for i in range(1, n):
        tmp = x[i] - base
        # print(f"base={base}, x[i]={x[i]}, tmp={tmp}, mid={mid}")
        if tmp >= mid:
            base = x[i]
            cnt += 1
    if cnt < c:
        p2 = mid - 1
    else:
        p1 = mid + 1
        if mid > res:
            res = mid
print(res)
