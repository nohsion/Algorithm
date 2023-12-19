# 거스름돈을 가장 적은 수의 동전으로 교환해주자.
"""
        0
  1     2     5
1 2 5 1 2 5 1 2 5
"""


def dfs(i, x_sum):
    global res
    if x_sum > m or i > res:
        return
    if x_sum == m:
        if i < res:
            res = i
        return
    for c in coins:
        dfs(i+1, x_sum + c)


if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    res = 2147000
    dfs(0, 0)
    print(res)

