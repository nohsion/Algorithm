# 철수의 트럭은 C 킬로그램 넘게 태울 수 없다. C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 가장 무거운 무게를 구하세요.
# 1<=C<=100,000,000, 1<=N<=30
"""
    81
  58   58
42 42 42 42
"""


def dfs(i, x_sum):
    global res
    if x_sum > c:
        return
    if i == n:
        if x_sum > res:
            res = x_sum
        return
    dfs(i+1, x_sum + weight[i])
    dfs(i+1, x_sum)


if __name__ == '__main__':
    c, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    res = -1
    dfs(0, 0)
    print(res)
