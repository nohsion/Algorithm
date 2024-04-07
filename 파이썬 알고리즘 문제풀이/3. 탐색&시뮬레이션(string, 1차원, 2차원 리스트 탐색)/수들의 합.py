n, m = map(int, input().split())
a = list(map(int, input().split()))

# 1. 시간복잡도 실패 (삼중 for문)
# cnt = 0
# for i in range(n):
#     for j in range(n-i):
#         a_sum = 0
#         for k in range(i+1):
#             a_sum += a[j+k]
#         if a_sum == m:
#             cnt += 1
# print(cnt)


#2. 투포인터로 연속된 값을 더한다. (어려움) lt, rt
cnt = 0
lt, rt = 0, 1  # 항상 lt ~ rt-1까지의 범위로 본다.
tot = a[0]
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break  # 여기서 break로 모든 경우의 수가 해결되는데, 생각해내기가 어려움. 외우자.
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
