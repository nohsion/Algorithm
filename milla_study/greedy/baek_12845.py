# https://www.acmicpc.net/problem/12845
# 가장 큰 레벨의 카드를 기준으로 (각 카드 레벨) + (가장 큰 레벨) 하면 되겠다.
n = int(input())
cards = list(map(int, input().split()))
largest = max(cards)
result = 0
for c in cards:
    result += c + largest
result -= largest * 2  # 가장 큰 카드가 두 번 더해지니 마지막에 빼준다.
print(result)
