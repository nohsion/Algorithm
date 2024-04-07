# 철수의 트럭은 C 킬로그램 넘게 태울 수 없다. C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 가장 무거운 무게를 구하세요.
# 1<=C<=100,000,000, 1<=N<=30
"""
    81
  58   58
42 42 42 42

                   D(0,0,81)
      D(1,81,139)              D(1,0,139)
D(2,139,181) D(2,81,181) D(2,58,181) D(2,0,181)
"""


def dfs(i, w_sum, t_sum):
    global res
    if w_sum > c or w_sum + (total - t_sum) < res:  # 현재 값에서 나머지를 다 더해도 안되면 지금 끝내자..
        return
    if i == n:
        if res < w_sum < c:
            res = w_sum
        return
    dfs(i + 1, w_sum + weight[i], t_sum + weight[i])
    dfs(i + 1, w_sum, t_sum + weight[i])


if __name__ == '__main__':
    c, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    total = sum(weight)
    res = 0
    dfs(0, 0, 0)
    print(res)
