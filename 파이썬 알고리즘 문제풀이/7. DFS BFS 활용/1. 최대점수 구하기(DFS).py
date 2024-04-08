# 얻는 점수와 푸는데 걸리는 시간이 주어질 때,
# N개의 문제에서, 제한시간 M 안에 최대점수를 구하세요.
"""
(상태트리)
- 모든 경우의 수: 문제를 푸냐 안푸냐, 모두 선택해본다.
- 백트래킹: 단, 제한 시간이 넘어가면 return
              init
        5               5
   10      10      10      10
25   25   25 25   25 25   25 25
"""


# 레벨, score 총합, time 총합
def dfs(L, s_sum, t_sum):
    global res
    # 시간 초과
    if t_sum > m:
        return
    # 모든 문제(leaf node) 도달했다면 종료
    if L == n:
        # 점수 총합 업데이트
        if s_sum > res:
            res = s_sum
        return

    ch[L] = 1  # 사용 O
    dfs(L+1, s_sum+a[L][0], t_sum+a[L][1])
    ch[L] = 0  # 사용 X
    dfs(L + 1, s_sum, t_sum)


if __name__ == '__main__':
    # 문제 개수 n, 제한 시간 m
    n, m = map(int, input().split())
    # 문제 (score, time) 리스트
    a = [tuple(map(int, input().split())) for _ in range(n)]
    # 체크 리스트
    ch = [0] * n
    # 최대 점수
    res = 0
    dfs(0, 0, 0)
    print(res)
