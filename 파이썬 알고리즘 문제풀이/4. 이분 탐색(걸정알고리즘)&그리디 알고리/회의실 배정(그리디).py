n = int(input())
se_range = [list(map(int, input().split())) for _ in range(n)]

se_range.sort(key=lambda x: x[1])  # 끝나는 시간으로 정렬하는 것이 중요
last_end, cnt = 0, 0
for se in se_range:
    if se[0] >= last_end:
        cnt += 1
        last_end = se[1]
print(cnt)
