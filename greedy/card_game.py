# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임 (n * m 카드가 놓여져 있음)
# 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다

n, m = map(int, input().split())
cards = [[0] * m for _ in range(n)]
tmp = []
for i in range(n):
    data = list(map(int, input().split()))
    tmp.append(min(data))

print(max(tmp))
