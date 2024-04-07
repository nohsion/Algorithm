# 침몰하는 타이타닉에서 구명보트를 타고 탈출해야 합니다.
# 보트는 2명 이하로만 탑승 가능하고, 탑승 제한 M kg 이하입니다.
# 전체 N명의 몸무게가 주어졌을 때, 구명보트의 최소 개수를 구하세요.
from collections import deque

n, m = map(int, input().split())
weight = list(map(int, input().split()))

# 내 답안
# weight.sort(reverse=True)
# cnt = 0
# while len(weight) > 0:
#     base_w = weight[0]
#     for i in range(1, len(weight)):
#         w = weight[i]
#         if base_w + w <= m:
#             weight.remove(w)
#             break
#     weight.remove(base_w)
#     cnt += 1
# print(cnt)


# 모범 답안 (queue, 시간 효율적)
weight.sort()
weight = deque(weight)
cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break
    if weight[0] + weight[-1] > m:
        weight.pop()
        cnt += 1
    else:
        weight.pop()
        weight.popleft()
        cnt += 1
print(cnt)