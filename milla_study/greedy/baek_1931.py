# https://www.acmicpc.net/problem/1931

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
cnt, last_end = 0, 0
for m in sorted(meetings, key=lambda x: (x[1], x[0])):
    if m[0] >= last_end:  # 이전 회의가 끝난 시간 이후에 시작하는 미팅만 카운트하면 된다.
        last_end = m[1]
        cnt += 1
print(cnt)
