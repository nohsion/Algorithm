T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ch = [0]*201    # 복도번호

    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:   # 함정.. 정렬 안 되어 있으면 순서 바꿔줘야 함
            s, e = e, s
        cs = (s+1) // 2
        ce = (e+1) // 2
        for i in range(cs, ce + 1):
            ch[i] += 1

    ans = max(ch)
    print(f"#{test_case} {ans}")
