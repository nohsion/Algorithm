def count(arr):
    ret = 0
    for lst in arr:
        cnt = 0
        for j in lst:
            if j != 0:
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1)) # 0 패딩 붙인 2차원 리스트
    tarr = list(zip(*arr)) # 전치행렬에 0 패딩 붙인 2차원 리스트

    ans = count(arr) + count(tarr)
    print(f"#{test_case} {ans}")