# https://www.acmicpc.net/problem/2563
# point: 넓이(면적) = 2차원 arr에서의 1의 개수

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)] # (si, sj) 리스트
arr = [[0]*101 for _ in range(101)]

# [1] 표시
for si, sj in lst:
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1

# [2] 넓이 계산 (1 카운팅)
ans = sum([sum(lt) for lt in arr])
print(ans)