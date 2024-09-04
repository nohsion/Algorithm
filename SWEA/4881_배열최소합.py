# https://swexpertacademy.com/main/learn/course/subjectDetail.do?subjectId=AWOVIc7KqfQDFAWg#

def dfs(ci, sm, jlst):
    global ans
    # 가지치기
    if sm > ans:
        return

    # 종료조건
    if ci == N:
        ans = min(ans, sm)
        return

    for nj in range(N):
        if nj in jlst:
            continue
        dfs(ci+1, sm+arr[ci][nj], jlst+[nj])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 9999
    dfs(0, 0, [])
    print(f"#{test_case} {ans}")
