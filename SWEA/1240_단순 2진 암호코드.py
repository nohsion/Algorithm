rule = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}


def get_code(tlst):
    cnt = prev = 0
    tans = []
    for n in tlst:
        if prev == n:
            cnt += 1
        else:
            tans.append(cnt)
            cnt = 1
            prev = n
    tans.append(cnt)

    return rule.get(''.join(map(str, tans)), -1)

def solve():
    lst = []
    for alst in arr:
        if all(n == 0 for n in alst):
            continue

        start_idx = 0
        # 암호코드의 뒤가 1로 끝나니까 뒤에서부터 읽어야 함.
        for idx in range(M-1, 7, -1):
            if alst[idx] != 1: # 마지막 수가 1이어야만 암호코드이다.
                continue
            if idx-55 >= 0:
                start_idx = idx-55
                break
        for idx in range(start_idx, M, 7):
            tlst = alst[idx:idx+7]
            num = get_code(tlst)
            lst.append(num)
            if len(lst) == 8:   # 8개의 암호코드가 완성됐다면 종료
                return lst
    return lst


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    lst = solve()

    sm = 0
    for idx, n in enumerate(lst):
        if idx%2 == 0:
            sm += n*3
        else:
            sm += n
    ans = 0
    if sm % 10 == 0:
        ans = sum(lst)

    print(f"#{test_case} {ans}")