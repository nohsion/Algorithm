# https://www.acmicpc.net/problem/2875
# 여학생이 남학생의 두배보다 많거나 같으면 인턴으로 뺀다.
# 그렇지 않으면 남학생을 뺀다.

n, m, k = map(int, input().split())
cnt = 0
while cnt < k:
    if n >= m * 2:
        n -= 1
    else:
        m -= 1
    cnt += 1
print(min(n // 2, m))
