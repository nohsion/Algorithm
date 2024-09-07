
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    h = [0]*(N+1)

    last = 0
    for n in lst:
        # [1] last 포인터 증가 및 힙 노드 추가
        last += 1
        h[last] = n
        # [2] 부모존재 & 부모보다 내가 더 작으면 swap (반복)
        c = last # 임시 포인터 변수
        while c//2 and h[c] < h[c//2]:
            h[c], h[c//2] = h[c//2], h[c]
            c //= 2
    ans = 0
    c = N
    while c//2:
        ans += h[c//2]
        c //= 2

    print(f"#{test_case} {ans}")
