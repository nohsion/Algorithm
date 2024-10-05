# https://www.acmicpc.net/problem/8320

N = int(input())
ans = N
for i in range(2, N):
    n = N//i - (i-1)
    if n <= 0:
        break
    ans += n
print(ans)