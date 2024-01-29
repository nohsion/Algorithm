# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
"""
1 2 3
        0            D(0)
  1     2     3      D(1)
1 2 3 1 2 3 1 2 3    D(2)
"""
def dfs(L):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
        return
    for i in range(1, n+1):
        if ch[i] == 1:
            continue
        ch[i] = 1
        res[L] = i
        dfs(L+1)
        ch[i] = 0  # Back 할때, ch를 0으로 풀어줘야 한다! DFS 다음에 오는 것이, 끝나고 돌아가는 부분이다.


if __name__ == '__main__':
    n, m = map(int, input().split())  # 3 2
    res = [0] * m  # [0, 0]
    ch = [0] * (n+1)  # [0, 0, 0, 0]
    cnt = 0
    dfs(0)
    print(cnt)
