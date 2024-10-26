N = int(input())

dp = [0]*(N+1)
# 초기값은 0으로 이미 설정해있으니, 필요 없음

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])