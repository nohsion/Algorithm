# 1~N까지 적힌 구슬이 있습니다. 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력하세요.


def dfs(L):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        cnt += 1
        print()
        return
    for i in range(1, n+1):
        res[L] = i
        dfs(L+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)
