n = int(input())  # 참여하는 사람 수
dices: list[list[int]] = []
for i in range(n):
    dices.append(list(map(int, input().split())))


def get_score(dice):
    """
    규칙 1. 같은 눈 3개: 10_000 + (같은 눈) * 1_000
    규칙 2. 같은 눈 2개: 1_000 + (같은눈) * 100
    규칙 3. 모두 다른 눈: (가장 큰 눈) * 100
    """
    n = len(dice)  # 3
    is_same: list[bool] = []
    for i in range(n-1):
        for j in range(i+1, n):
            is_same.append(dice[i] == dice[j])
    true_idx = -1
    true_cnt = 0
    for idx, iss in enumerate(is_same):
        if iss is True:
            true_cnt += 1
            true_idx = idx
    if true_cnt == 3:
        return 10_000 + dice[0] * 1_000
    elif true_cnt == 1:
        return 1_000 + dice[true_idx] * 100
    elif true_cnt == 0:
        return max(dice) * 100
    else:
        raise Exception('What?!')


scores = [get_score(dice) for dice in dices]
print(max(scores))
