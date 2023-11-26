n, m = map(int, input().split())
a = list(map(int, input().split()))
# 1. 정렬
a.sort()

# 2. 이분탐색 (logN) 1,7,9,29,42,50 -- 10 찾기
p1, p2 = 0, n - 1
res = -1
while p1 <= p2:
    mid = (p1 + p2) // 2
    if a[mid] == m:
        res = mid
        break
    elif a[mid] > m:
        p2 = mid - 1
    else:
        p1 = mid + 1
if res == -1:
    print("못찾았습니다.")
else:
    print(res+1)
