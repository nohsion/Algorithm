# https://www.acmicpc.net/problem/1697
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        q = queue.popleft()
        if q == k:
            return visited[q]
        for nx in (q-1, q+1, q*2):
            if 0 <= nx <= largest and visited[nx] == 0:
                visited[nx] = visited[q] + 1
                queue.append(nx)


if __name__ == '__main__':
    # 수빈이의 위치 n, 동생이 있는 위치 k
    n, k = map(int, input().split())
    largest = 100_000
    visited = [0] * (largest + 1)  # 방문 처리
    print(bfs(n))
