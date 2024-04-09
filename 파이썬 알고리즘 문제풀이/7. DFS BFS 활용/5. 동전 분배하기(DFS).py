# N개의 동전을 A, B, C 세 명에게 나누어 주려고 합니다.
# 세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
# 단 세 사람의 총액은 서로 달라야 합니다.
"""
                    init                D(0)
                        7
        a               b           c
  8     8     8                         D(1)
a b c a b c a b c
"""


def dfs(L, a_sum, b_sum, c_sum):
    global res
    if L == n:
        # 단 세 사람의 총액은 모두 달라야 함
        if a_sum != b_sum and b_sum != c_sum and c_sum != a_sum:
            diff = max(a_sum, b_sum, c_sum) - min(a_sum, b_sum, c_sum)
            if diff < res:
                res = diff
        return
    dfs(L+1, a_sum+coin[L], b_sum, c_sum)
    dfs(L+1, a_sum, b_sum+coin[L], c_sum)
    dfs(L+1, a_sum, b_sum, c_sum+coin[L])


if __name__ == '__main__':
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    res = 2147000000
    dfs(0, 0, 0, 0)
    print(res)


