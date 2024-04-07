# 길이가 모두 다른 k개의 랜선을 n개로 만들 수 있는 랜선의 최대 길이를 구하세요.
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

res = 0
p1, p2 = 1, max(lines)
while p1 <= p2:
    mid = (p1 + p2) // 2
    cnt = sum([l // mid for l in lines])
    if cnt >= n:
        res = mid
        p1 = mid + 1
    elif cnt < n:
        p2 = mid - 1

print(res)
