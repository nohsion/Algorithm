# T원의 지폐를 동전으로 바꿔 주려고 한다.
# 이때, 동전 교환 방법은 여러 가지가 있을 수 있다.
# 예) 20원의 지폐를 10원 짜리, 5원 짜리, 1원 짜리 동전이 각각 2개, 3개, 5개씩 있을 때 처리
# 모든 동전 교환 방법의 가지 수를 출력하세요.
"""
각 동전을 몇개씩 쓸지 0~n개 사용 가능
                                       init
      5(0)                  5(1)                  5(2)                5(3)
10(0) 10(1) 10(2)     10(0) 10(1) 10(2)     10(0) 10(1) 10(2)   10(0) 10(1) 10(2)
1(0)...
"""
LARGEST = 10_000


def dfs(L, p_sum):
    global cnt
    # cut-edge
    # 1. 현재까지의 합계(p_sum)이 타겟 t보다 크면 종료
    if p_sum > t:
        return
    # (안함) 2. 현재까지의 합계(p_sum)에서 남은 합계를 더해봐도 타겟 t가 되지 않으면 종료

    if L == k:
        if p_sum == t:
            cnt += 1
        return
    p, n = coin[L]
    for i in range(n+1):
        dfs(L+1, p_sum + p*i)


if __name__ == '__main__':
    t = int(input())  # 지폐 금액 t
    k = int(input())  # 동전 가지 수 k
    # [(동전금액 p, 동전개수 n)]
    coin = [tuple(map(int, input().split())) for _ in range(k)]

    cnt = 0
    dfs(0, 0)
    print(cnt)


