def postord(n):
    if n <= N:
        if lst[n] == '+':
            return postord(ch1[n]) + postord(ch2[n])
        elif lst[n] == '-':
            return postord(ch1[n]) - postord(ch2[n])
        elif lst[n] == '*':
            return postord(ch1[n]) * postord(ch2[n])
        elif lst[n] == '/':
            return postord(ch1[n]) / postord(ch2[n])
        else:   # 숫자 (피연산자)
            return int(lst[n])
    else:
        return 0


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    # [1] 트리 저장
    for _ in range(N):
        tlst = input().split()
        idx = int(tlst[0])
        lst[idx] = tlst[1]
        if len(tlst) > 2:
            ch1[idx] = int(tlst[2])
            ch2[idx] = int(tlst[3])

    # [2] 트리 순회
    ans = int(postord(1))

    print(f"#{test_case} {ans}")
