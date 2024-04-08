# 만약 추의 무게가 {1, 5, 7}이면 S=13이고, 그릇에 담을 수 있는 물의 무게는 {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13}이고,
# 1부터 S사이의 무게에서 9와 10에 대응하는 무게의 물을 담을 수 없다.
"""
(상태트리)
- n을 선택하냐 마냐
    - 선택 O, 양수이냐 음수이냐 (+n or -n)
    - 선택 X, 항상 (+0)
-> 따라서, 3진 트리 (+n, -n, 0)
"""


# 레벨, 추 무게 합
def dfs(L, w_sum):
    if L == k:
        if w_sum > 0:  # 음수는 굳이 안넣어도 됨. 겹치니까
            res.add(w_sum)
        return
    dfs(L+1, w_sum+chu[L])  # 선택 O (+n)
    dfs(L+1, w_sum-chu[L])  # 선택 O (-n)
    dfs(L+1, w_sum)  # 선택 X


if __name__ == '__main__':
    k = int(input())  # 3 <= k <= 13
    chu = list(map(int, input().split()))
    res = set()
    dfs(0, 0)
    print(sum(chu) - len(res))
