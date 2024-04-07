n = int(input())  # OX 시험문제 개수
scores = list(map(int, input().split()))  # OX 결과

res = 0
win_cnt = 0
for i in range(n):
    if scores[i] == 1:
        win_cnt += 1
        res += win_cnt
    else:
        win_cnt = 0

print(res)
