# 자연수가 입력되면 최소힙에 입력한다.
# 0이 입력되면 최솟값을 꺼내어 출력한다. 출력할 자료가 없으면 -1 출력
# -1이 입력되면 프로그램 종료한다.

from heapq import heappush, heappop

heap = []
while True:
    x = int(input())
    if x == -1:
        break
    if x == 0:
        if heap:
            print(heappop(heap))
        else:
            print(-1)
        continue
    heappush(heap, x)
