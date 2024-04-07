# 1~N까지 번호가 적힌 구슬이 있습니다. 이중 M개를 뽑는 방법의 수를 출력하세요. (조합)
"""
(상태트리) - 단, 순열과 조금 모양이 다름.
                        D(0,1) <- D(L,s) :Level, Start
         1               2               3               4
       D(1,2)          D(1,3)           D(1,4)          D(1,5)
   2      3      4
D(2,3) D(2,4) D(2,5)
"""


def dfs(L, s):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
        return
    for i in range(s, n+1):
        res[L] = i
        dfs(L+1, i+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0, 1)
    print(cnt)
