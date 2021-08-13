# '큰 수의 법칙': 주어진 배열(크기 n)에서 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 단, 특정한 인덱스를 K번 초과하여 더할 수 없다.

n, m, k = map(int, input().split())  # 5 8 3
data = list(map(int, input().split()))  # 2 4 5 4 6
data.sort(reverse=True)
first = data[0]
second = data[1]

# 가장 큰 수가 더해지는 횟수
count_f = (m // (k+1)) * k
count_f += m % (k+1)    # m이 k+1로 나눠떨어지지 않을 때

answer = count_f * first
answer += (m - count_f) * second

print(answer)