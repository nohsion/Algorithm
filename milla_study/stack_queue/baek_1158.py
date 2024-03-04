# https://www.acmicpc.net/problem/1158
# [1,2,3,4,5,6,7]
# 1 2 [3] 4 5 6 7
# 4 5 [6] 7 1 2
# 7 1 [2] 4 5 ...
# [7] 1
from collections import deque

n, k = map(int, input().split())
queue = deque([_ for _ in range(1, n+1)])
res = []
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())  # k번째인 경우 정답 리스트에 추가

print(f"<{', '.join(map(str, res))}>")
