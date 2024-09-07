# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq

def dfs(n, sm):
    global ans
    # 가지치기
    if sm >= ans:
        return
    # 종료조건
    if n >= N:
        ans = min(ans, sm)
        return

    # 0: 1일 이용권
    dfs(n+1, sm + lst[n]*costs[0])

    # 1: 1달 이용권
    dfs(n+1, sm + costs[1])

    # 2: 3달 이용권
    dfs(n+3, sm + costs[2])

    # 3: 1년 이용권
    dfs(n+12, sm + costs[3])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    costs = list(map(int, input().split()))  # 1일, 1달, 3달, 1년 이용권 가격
    lst = list(map(int, input().split()))
    N = 12

    ans = costs[3]
    dfs(0, 0)
    print(f"#{test_case} {ans}")
