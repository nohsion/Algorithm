# https://www.acmicpc.net/problem/1697
# N에서 K 위치로 가는 가장 빠른 시간을 구하세요.
# 이동범위: x-1, x+1, x*2
from collections import deque

MIN = 0
MAX = 200_000

def bfs(s, e):
    # [1] q, v 생성
    q = deque()
    v = [0]*(MAX+1)
    # [2] 초기데이터 삽입
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        # 종료조건 확인
        if c == e:
            return v[c] - 1

        for n in (c-1, c+1, c*2):
            if MIN<=n<=MAX and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return -1


n, k = map(int, input().split())
ans = bfs(n, k)
print(ans)
