# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def dfs(n, cnt, sm):
    global ans
    # 가지치기
    if cnt >= ans:
        return
    # 종료조건
    if n == N:
        ans = min(ans, cnt)
        return

    # 교체 O
    dfs(n+1, cnt+1, lst[n]-1)
    # 교체 X
    if sm > 0:
        dfs(n+1, cnt, sm-1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]

    ans = N+1
    dfs(2, 0, lst[1]-1)
    print(f"#{test_case} {ans}")