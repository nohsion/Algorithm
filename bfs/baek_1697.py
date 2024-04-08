# https://www.acmicpc.net/problem/1697
# N에서 K 위치로 가는 가장 빠른 시간을 구하세요.
# 이동범위: x-1, x+1, x*2
"""
최단 시간 -> BFS
1. ch = [0] * 100_000  // 이동할때마다 시간 체크 변수
2. 종료조건: 현위치 == k
3. 이동범위 큐에 삽입. (0 <= nx <= 100_000)
"""
from collections import deque

LARGEST = 100_000


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        q = queue.popleft()
        # 종료 조건:
        if q == k:
            return

        for nx in (q-1, q+1, q*2):
            # 아직 방문하지 않았고, 범위 내라면
            if 0 <= nx <= LARGEST and ch[nx] == 0:
                ch[nx] = ch[q] + 1
                queue.append(nx)


if __name__ == '__main__':
    n, k = map(int, input().split())
    ch = [0] * (LARGEST + 1)
    bfs(n)
    print(ch[k])
