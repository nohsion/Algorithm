# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다.
# N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때
# 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
"""

1. 첫 row 부터 실행하는데, center(n//2)에서 부터 다음 row 부터 점점 확장
- 확장범위: 0 -> 1 -> 2 -> 1 -> 0
- 즉, dx는 i <= center 이면 +=1, i > center 이면 -=1
- for i in range(n):
    if i < center:
        dx += 1
    else:
        dx -= 1
2. center에서 범위(+-dx)만큼 사과를 수확한다.
- for j in range(center-dx, center+dx+1):
    cnt += graph[i][j]
"""


if __name__ == '__main__':
    n = int(input())
    center = n // 2  # 중앙값
    graph = []  # 그래프 (사과밭)
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    cnt, dx = 0, 0
    for i in range(n):
        for j in range(center-dx, center+dx+1):
            print(f"graph[{i}][{j}] = {graph[i][j]}")
            cnt += graph[i][j]
        if i < center:
            dx += 1
        else:
            dx -= 1
    print(cnt)
