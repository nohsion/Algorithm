# https://www.acmicpc.net/problem/11047
# 동전이 배수의 관계가 아니면 그리디 X. 모든 경우의 수 해봐야 함 (탐색)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
while k > 0 and coins:
    c = coins.pop()  # 현재 가장 비싼 동전
    if k < c:
        continue
    tmp = k % c
    cnt += k // c
    k = tmp

print(cnt)
