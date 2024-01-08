# N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 YES, 아니면 NO를 출력하세요.
"""
[1, 3, 5, 6, 7, 10]
       1
   3       3
 5   5   5   5
6 6 6 6 6 6 6 6

          D(0,0)
   D(1,1)        D(1,0)
D(2,4) D(2,1) D(2,3) D(2,0)
...
"""
import sys


def dfs(L, x_sum):
    if L == n:
        if x_sum * 2 == total:
            print('YES')
            sys.exit(0)
        return
    dfs(L + 1, x_sum + a[L])
    dfs(L + 1, x_sum)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    dfs(0, 0)
    print('NO')
