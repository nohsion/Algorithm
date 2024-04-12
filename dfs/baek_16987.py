# https://www.acmicpc.net/problem/16987

def dfs(L, cnt):
    global ans
    if cnt + (N-L)*2 <= ans:    # 최대한으로 깨져도 정답 갱신이 안 된다면
        return
    if L == N:
        ans = max(ans, cnt)
        return
    if lst[L][0] <= 0:      # 내 계란이 깨진 경우 -> 다음 계란으로 이동
        dfs(L+1, cnt)
    else:                   # 내 계란이 깨지지 않은 경우
        flag = False        # 한번도 안 부딪혔다면.. 그래도 다음 계란 가야 함
        for j in range(N):
            if L == j or lst[j][0] <= 0:
                continue
            flag = True
            # 계란 박치기
            lst[L][0] -= lst[j][1]
            lst[j][0] -= lst[L][1]
            dfs(L+1, cnt + int(lst[L][0] <= 0) + int(lst[j][0] <= 0))
            # 계란 박치기 원상복구
            lst[L][0] += lst[j][1]
            lst[j][0] += lst[L][1]
        if flag is False:
            dfs(L+1, cnt)


N = int(input())  # 계란 수
lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0)
print(ans)
