T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 'Possible'
    cnt = 0
    for t in sorted(lst):
        cnt += 1
        if (t//M)*K < cnt:  # 현재까지 붕어빵 개수보다 사람수가 많다면, 불가능
            ans = 'Impossible'
            break

    print(f"#{test_case} {ans}")