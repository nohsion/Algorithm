# 현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다.
# 현수의 위치와 송아지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
# 현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.
# 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성 하세요.
"""
최단거리 - BFS
1. 이동범위 for nx in (x+1, x-1, x+5)
2. 범위 1<=nx<=10_000
"""
from collections import deque

LARGEST = 10_000


def bfs(point):
    queue = deque()
    queue.append(point)
    ch[point] = 0
    while queue:
        x = queue.popleft()
        if x == e:
            return ch[e]
        for nx in (x+1, x-1, x+5):
            # 범위 내에 있고, 방문하지 않았다면
            if 1 <= nx <= LARGEST and ch[nx] == -1:
                ch[nx] = ch[x] + 1  # 점프 횟수 저장 및 방문 체크 (동시 처리)
                queue.append(nx)


if __name__ == '__main__':
    # 현수 위치 s, 송아지 위치 e
    s, e = map(int, input().split())
    ch = [-1] * (LARGEST + 1)  # 위치값에 점프 횟수를 저장하는 변수
    min_jump = bfs(s)
    print(min_jump)
