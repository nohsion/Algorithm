# https://www.acmicpc.net/problem/1966
from collections import deque

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())  # 4, 2
    queue = deque()
    for idx, val in enumerate(input().split()):
        queue.append((int(val), idx))
    res = 0
    while queue:
        max_q = max(map(lambda x: x[0], queue))
        if max_q > queue[0][0]:
            queue.append(queue.popleft())
        else:
            x = queue.popleft()
            res += 1
            if x[1] == m:
                print(res)
                break

