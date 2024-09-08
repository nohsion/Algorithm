# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw

# 반드시 이진 tree가 가능하면 그것으로 해결한다. 아니면 n^n 꼴로 복잡도가 확 올라갈 수 있음.
# 이진 트리는 2^n
def dfs(n, sm):
    global ans
    # 가지치기
    if sm > ans:
        return
    # 종료조건
    if n == N:
        if sm >= B:
            ans = min(ans, sm)
        return

    # 해당직원 사용 O
    dfs(n+1, sm+lst[n])
    # 해당직원 사용 X
    dfs(n+1, sm)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = sum(lst)
    dfs(0, 0)

    print(f"#{test_case} {ans-B}")