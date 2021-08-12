# 거스름돈: 500, 100, 50, 10원
# 거슬러줘야할 돈이 N원일 때, 동전의 최소 개수를 구하라. (N은 10의 배수)
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)


