# 총 n개의 노래를 m개의 DVD로 만드는데, 만들 수 있는 DVD 용량(분)의 최솟값을 구하세요.
n, m = map(int, input().split())
times = list(map(int, input().split()))

p1, p2 = max(times), sum(times)
res = 0
tmp_cnt = 0
while p1 <= p2:
    mid = (p1 + p2) // 2
    cnt, tmp = 1, 0
    for t in times:
        tmp += t
        if tmp > mid:
            tmp = t
            cnt += 1
        # print(f"기준={mid}, 현재={t}, 합계={tmp}, 개수={cnt}")
    tmp_cnt = cnt
    if cnt <= m:
        res = mid
        p2 = mid - 1
    else:
        p1 = mid + 1
print(res)
