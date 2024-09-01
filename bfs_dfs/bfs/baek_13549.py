# https://www.acmicpc.net/problem/13549
"""
최단 시간 - BFS
1. 초기값: 위치 N
2. 종료조건: 현재위치 == k
3. 이동범위: 1초 - [x-1, x+1] / 0초 - [x*2]. 단, 범위 내 (0<=nx<=100_000)
4. 시간담을변수: ch=[0]*(100_000+1)
"""
from collections import deque

LARGEST = 100_000


def bfs(x):
    queue = deque()
    queue.append(x)
    ch[x] = 0
    while queue:
        q = queue.popleft()
        if q == k:
            return
        # 곱하기, 빼기, 더하기 순서로 확인해야 함.. 아니면 틀린다. (충격)
        for nx in (q*2, q-1, q+1):
            if 0 <= nx <= LARGEST and ch[nx] == -1:
                if nx in ([q*2]):
                    ch[nx] = ch[q]  # 0초 후
                    queue.appendleft(nx)  # 큐에 먼저 넣어줘야 함.
                else:
                    ch[nx] = ch[q] + 1  # 1초 후
                    queue.append(nx)


if __name__ == '__main__':
    n, k = map(int, input().split())
    ch = [-1] * (LARGEST + 1)
    bfs(n)
    print(ch[k])
