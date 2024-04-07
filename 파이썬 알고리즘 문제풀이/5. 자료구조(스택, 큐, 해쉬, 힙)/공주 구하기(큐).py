# 1~N번의 왕자가 동그랗게 앉아있을 때, K를 외치는 사람은 원 밖으로 나오게 된다.
# 그리고 다음 왕자부터 다시 1부터 번호를 외친다.
# 마지막까지 남은 왕자의 번호를 출력하세요.
from collections import deque

n, k = map(int, input().split())
# [1,2,3,4,5,6,7,8]
# 1) 1 2 [3] 4 5 6 7 8
# 2) 4 5 [6] 7 8 1 2
# 3) 7 8 [1] 2 4 5
# 4) 2 4 [5] 7 8
# 5) 7 8 [2] 4
# 6) 4 7 [8]
# 7) [4] 7
queue = deque([i for i in range(1, n + 1)])
while len(queue) > 1:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    queue.popleft()
print(queue[0])
