# n, m은 4 6 8 12 20 중 하나
n, m = map(int, input().split())

cnt = [0] * (n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

max = 0
for value in cnt:
    if value > max:
        max = value

print([i for i in range(len(cnt)) if cnt[i] == max])