# 휴가(삼성 SW역량평가 기출문제 : DFS활용)
# 현수는 오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 남은 N일 동안 최대한 많은 상담을 해서 최대한의 돈으로 휴가를 떠나려 한다.
# 각 상담마다 걸리는 시간 T, 받는 금액 P 주어질 때, 최대 수익을 구하세요.
"""
모든 경우의 수 해보기 - DFS
work = [(t, p), ...]
"""


def dfs(s, p_sum):
    global res
    # 벗어나면 종료
    if s > n:
        if s == n+1 and p_sum > res:
            res = p_sum
        return

    t, p = work[s]
    dfs(s+t, p_sum+p)  # 상담 O
    dfs(s+1, p_sum)  # 상담 X - 다음 날로 넘어감.


if __name__ == '__main__':
    n = int(input())
    # (t, p) = (상담 걸리는 일수, 받는 금액)
    work = [tuple(map(int, input().split())) for _ in range(n)]
    work.insert(0, (0, 0))
    res = 0
    dfs(1, 0)
    print(res)
