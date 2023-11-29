# n명의 지원자의 키와 몸무게가 주어질 때, 다른 모든 지원자와 비교하여
# 키와 몸무게 중 적어도 하나는 크거나 무거운 사람만 뽑기로 하였다.
# 이때, 선수로 뽑히는 최대 인원을 구하세요.
n = int(input())
players = [tuple(map(int, input().split())) for _ in range(n)]

players.sort(key=lambda x: (-x[0], -x[1]))
cnt, base_w = 1, players[0][1]
for h, w in players:
    if w > base_w:
        cnt += 1
        base_w = w
print(cnt)
