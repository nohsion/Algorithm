# https://www.acmicpc.net/problem/10163

N = int(input())
M = 1001
lst = [()] + [tuple(map(int, input().split())) for _ in range(N)] # (sj, si, w, h) 리스트
arr = [[0]*(M+2) for _ in range(M+2)]

# [1] 색종이 표시
for idx in range(1, N+1):
    sj, si, w, h = lst[idx]
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = idx

# [2] 색종이별 카운트
# 2-1. 색종이 수(N)만큼 arr 순회 (N이 커지면 매우 오래 걸린다..)
# for idx in range(1, N+1):
#     cnt = 0
#     for lt in arr:
#         for x in lt:
#             if x == idx:
#                 cnt += 1
#     print(cnt)

# 2-2. cnts: 빈도수 배열 사용해서, arr는 한번만 순회한다.
cnts = [0]*(N+1)
for lt in arr:
    for x in lt:
        cnts[x] += 1
print(*cnts[1:], sep='\n')