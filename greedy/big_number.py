# '큰 수의 법칙': 주어진 배열에서 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 단, 특정한 인덱스를 K번 초과하여 더할 수 없다.

n, m, k = map(int, input().split())  # 5 8 3
data = list(map(int, input().split()))  # 2 4 5 4 6
answer = 0

data.sort(reverse=True)  # 6 5 4 4 2

tmp_data = [data[0], data[1]]

count = 0
please = True
flag = False
while please:
    if not flag:
        for j in range(k):
            answer += tmp_data[0]
            print(answer, tmp_data[0])
            count += 1
            if count == m:
                please = False
            if j == k-1:
                flag = True
    if flag:
        answer += tmp_data[1]
        count += 1
        if count == m:
            please = False
        flag = False
        print(answer, tmp_data[1])

print(answer)
