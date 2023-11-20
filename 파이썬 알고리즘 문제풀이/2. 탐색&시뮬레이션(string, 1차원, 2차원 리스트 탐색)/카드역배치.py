cards = [i for i in range(1, 21)]  # 카드는 1 ~ 20까지 존재
data: list[list[int]] = []  # [[5,10],[9,13], ...]
for _ in range(10):
    data.append(list(map(int, input().split())))

for d in data:
    s = d[0]
    e = d[1]
    for i in range((e-s+1)//2):
        tmp = cards[s-1+i]
        cards[s-1+i] = cards[e-1-i]
        cards[e-1-i] = tmp
        # 참고 swap for python
        # a,b = b,a

for c in cards:
    print(c, end=' ')