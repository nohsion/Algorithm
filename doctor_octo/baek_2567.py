# https://www.acmicpc.net/problem/2567
# point: 둘레 구하기
# 1) 1일때, 주위 4방향 0의 개수 카운팅
# 2) 0 -> 1, 1 -> 0 으로 바뀔때 카운팅 (일반행렬 + 전치행렬)


# 둘레 구하기 (1) - for문 경계값에 주의해야 한다.
def get_length1(arr):
    cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N+1 and 0<=nj<N+1 and arr[ni][nj] == 0:
                        cnt += 1
    return cnt

# 둘레 구하기 (2)
def get_length2(arr):
    cnt = 0
    for lt in arr:
        for i in range(1, N+1):
            if lt[i-1] != lt[i]:
                cnt += 1
    return cnt

N = 100
M = int(input())
lst = [tuple(map(int, input().split())) for _ in range(M)] # (si, sj) 리스트
arr = [[0]*(N+2) for _ in range(N+2)]

# [1] 표시
for si, sj in lst:
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1

# [2] 둘레 구하기 - 일반행렬 + 전치행렬
arr_t = list(zip(*arr))
ans = get_length2(arr) + get_length2(arr_t)

# ans = get_length1(arr)

print(ans)