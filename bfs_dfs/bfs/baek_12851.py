# https://www.acmicpc.net/problem/12851
"""
1. 최단시간: BFS
2. 초기값
    - 위치: N
    - 시간체크변수: ch = [0] * (100_000+1)
3. 체크조건: 현재값 == K -> res += 1
4. 이동범위: [x-1, x+1, x*2] / 범위 내 (0<=x<=100_000)
"""
from collections import deque
LARGEST = 100_000


def bfs(x):
    global res, min_time
    queue = deque()
    queue.append(x)
    while queue:
        q = queue.popleft()
        if q == k:
            min_time = ch[q]
            res += 1
            continue

        for nx in (q-1, q+1, q*2):
            # 범위 내에 있고, 방문하지 않았거나 "동일 탐색횟수를 가졌다면" 진행
            if 0<= nx <= LARGEST and (ch[nx] == 0 or ch[nx] == ch[q]+1):
                ch[nx] = ch[q] + 1
                queue.append(nx)


if __name__ == '__main__':
    n, k = map(int, input().split())
    ch = [0] * (LARGEST + 1)  # 시간 체크변수
    res = 0
    min_time = -1
    bfs(n)

    print(min_time)
    print(res)
