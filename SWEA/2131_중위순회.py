def inord(n):
    if n <= N:
        inord(n*2)
        ans.append(lst[n])
        inord(n*2 + 1)


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0]*(N+1)
    for _ in range(N):
        tlst = input().split()
        lst[int(tlst[0])] = tlst[1]

    ans = []
    inord(1)
    print(f"#{test_case} {''.join(ans)}")