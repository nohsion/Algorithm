
def post(n):
    left = n*2
    right = n*2 + 1

    if n <= N:
        if lst[n] == 0:
            lst[n] = post(left) + post(right)
        return lst[n]
    return 0

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = [0]*(N+1)
    for _ in range(M):
        leaf, value = map(int, input().split())
        lst[leaf] = value

    ans = post(L)

    print(f"#{test_case} {ans}")
