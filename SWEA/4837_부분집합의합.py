# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZEGAQUa-sgDFAVs

def dfs(n, sm, cnt):
    global ans
    # 가지치기: 가장 마지막에 고민 & 가장 위에 처리
    if sm > K or cnt > CNT:  # 합이나 카운트가 이미 정답을 넘어간 경우
        return

    # 종료조건
    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return
    # 사용 O
    dfs(n+1, sm+lst[n], cnt+1)
    # 사용 X
    dfs(n+1, sm, cnt)


T = int(input())
for test_case in range(1, T + 1):
    CNT, K = map(int, input().split())
    N = 12
    lst = [_ for _ in range(1, N+1)] # 1~12를 원소로 하는 집합 A
    ans = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")