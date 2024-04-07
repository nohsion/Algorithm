# 파이썬 heapq는 최소힙이다. 최대힙으로 사용하려면 약간의 변형이 필요하다.
# 마이너스 부호를 붙여서 push 해보자.
from heapq import heappop, heappush

heap = []
while True:
    x = int(input())
    if x == -1:
        break
    if x == 0:
        if heap:
            print(-heappop(heap))
        else:
            print(-1)
        continue
    heappush(heap, -x)
