# https://www.acmicpc.net/problem/13913
# 이 해답은 틀렸음. 정답을 못찾겠음..
from collections import deque

LARGEST = 100_000


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        q = queue.popleft()
        if q == k:
            print(ch[q])
            return

        for nx in (q-1, q+1, q*2):
            if 0 <= nx <= LARGEST and ch[nx] == 0:
                ch[nx] = ch[q] + 1
                history[nx] = q
                queue.append(nx)


if __name__ == '__main__':
    n, k = map(int, input().split())
    ch = [0] * (LARGEST + 1)
    history = [0] * (LARGEST + 1)  # 해당위치로 오기전 이전위치를 알기 위한 리스트
    bfs(n)

    res = [k]
    tmp = k
    while tmp != n:
        res.append(history[tmp])
        tmp = history[tmp]
    print(*res[::-1])
