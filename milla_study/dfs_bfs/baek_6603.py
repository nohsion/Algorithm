# https://www.acmicpc.net/problem/6603
"""
1 2 3 4 5
(상태트리) - 각 요소를 사용하냐 사용하지 않냐
       1
   2       2
 3   3   3   3
4 4 4 4 4 4 4 4
"""
def dfs(x):
    if x == k:
        cnt = len([i for i in range(k) if visited[i] == 1])
        if cnt == 6:
            for i in range(k):
                if visited[i] == 1:
                    print(S[i], end=' ')
            print()
        return

    visited[x] = 1
    dfs(x+1)
    visited[x] = 0
    dfs(x+1)


if __name__ == '__main__':
    while True:
        a = list(map(int, input().split()))
        k = a[0]  # 집합 S의 크기 k
        if k == 0:
            break
        S = a[1:]  # 로또 6개를 고를 집합 S
        visited = [0] * (k+1)
        dfs(0)
        print()
