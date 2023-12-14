# 철수의 트럭은 C 킬로그램 넘게 태울 수 없다. C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 가장 무거운 무게를 구하세요.
# 1<=C<=100,000,000, 1<=N<=30
"""
    81
  58   58
42 42 42 42
"""


def dfs(i, x_sum, t_sum):
    global res
    if x_sum > c:
        return
    # 중요: (수학적 계산) 현재 합계에 밑에 더할 애들을 더해봐도 현재 최대 합보다 작더라. 그러면 뭐하러 더하냐. cut! (Cut Edge)
    if x_sum + (total - t_sum) < res:
        return
    if i == n:
        if x_sum > res:
            res = x_sum
        return
    dfs(i+1, x_sum + weight[i], t_sum + weight[i])
    dfs(i+1, x_sum, t_sum + weight[i])


if __name__ == '__main__':
    c, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    res = -1
    total = sum(weight)
    dfs(0, 0, 0)
    print(res)
