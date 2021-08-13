# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# N에서 1을 뺍니다. / N을 K로 나눕니다.
# 과정을 수행해야 하는 최소 횟수를 구하시오

n, k = map(int, input().split())  # 17 4

count = 0
while n > 0:
    if n == 1:
        break
    elif n % k == 0:
        # print("나누기", n)
        n = int(n / k)
        count += 1
    else:
        # print("1 빼기", n)
        n -= 1
        count += 1

print(count)