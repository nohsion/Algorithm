# 필수과목은 반드시 이수해야 하며, 순서가 정해져 있습니다.
# 필수과목이 CBA 라면, 반드시 이수해야 하며 순서대로 들어야 합니다.
# 수업설계가 잘된 것인지, 잘못된 것인지 판단해주세요.
from collections import deque

required_list = list(map(str, input()))
n = int(input())
plan = [input() for _ in range(n)]


for i, p in enumerate(plan):  # p = CBDAGE
    required = deque(required_list)
    for x in p:  # x = C
        if not required:
            break
        if x in required:
            if x == required[0]:
                required.popleft()
            else:
                break
    if required:
        print(f"#{i+1} NO")
    else:
        print(f"#{i + 1} YES")

