# lst 리스트에서, N개 중 2개의 인덱스를 뽑는 조합
def comb(n, nlst):
    if n == 2:
        if sorted(nlst) not in comb_lst:
            comb_lst.append(nlst)
        return
    for i in range(N):
        if i not in nlst:
            comb(n+1, nlst + [i])


def dfs(n):
    global ans
    if n == CNT:
        ans = max(ans, int(''.join(map(str, lst))))
        return
    for i1, i2 in comb_lst: # NC2 조합 리스트 (인덱스)
        lst[i1], lst[i2] = lst[i2], lst[i1] # swap 처리

        chk = int(''.join(map(str, lst)))
        if (n, chk) not in v:
            dfs(n+1)
            v.append((n, chk))

        lst[i1], lst[i2] = lst[i2], lst[i1] # swap 되돌려놓기


T = int(input())
for test_case in range(1, T + 1):
    num, CNT = map(int, input().split())
    lst = [int(x) for x in str(num)]
    N = len(lst)

    comb_lst = [] # NC2: N개중 2개 선택하는 조합
    comb(0, [])

    v = []
    ans = 0
    dfs(0)

    print(f"#{test_case} {ans}")


