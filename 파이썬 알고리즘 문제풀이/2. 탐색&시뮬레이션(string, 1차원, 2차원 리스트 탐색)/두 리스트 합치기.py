n = int(input())
arr1 = list(map(int, input().split()))  # [1,3,5]
m = int(input())
arr2 = list(map(int, input().split()))  # [2,3,6,7,9]

# 1. 두 리스트가 이미 정렬이 되어 있는데, sort 쓰면 nlogn -> 비효율적!
# for i in sorted(arr1 + arr2):
#     print(i, end=' ')

# 2. n 시간복잡도(두 원소의 크기)로 해결 가능
res = []
p1, p2 = 0, 0  # 투포인터: p1은 arr1을 가리키고, p2는 arr2를 가리킨다.
while p1 < n and p2 < m:
    if arr1[p1] < arr2[p2]:
        res.append(arr1[p1])
        p1 += 1
    else:
        res.append(arr2[p2])
        p2 += 1

for i in res + arr1[p1:] + arr2[p2:]:
    print(i, end=' ')
