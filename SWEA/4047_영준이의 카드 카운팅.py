def count_cards(card_dict):
    sm = {
        'S': 0,
        'D': 0,
        'H': 0,
        'C': 0,
    }
    for x in card_dict.keys():
        for idx, num in enumerate(card_dict[x]):
            if idx == 0:
                continue
            if num > 1:
                return {}
            if num == 0:
                sm[x] += 1
    return sm


T = int(input())
for test_case in range(1, T + 1):
    instr = input()
    lst = [instr[i:i+3] for i in range(0, len(instr), 3)]
    card_dict = {
        'S': [0] * 14,
        'D': [0] * 14,
        'H': [0] * 14,
        'C': [0] * 14,
    }
    ans = 0
    for card in lst:
        x = card[0]
        num = int(card[1:3])
        card_dict[x][num] += 1
    cnt_dict = count_cards(card_dict)
    if not cnt_dict:
        ans = 'ERROR'
    else:
        ans = ' '.join([str(val) for val in cnt_dict.values()])

    print(f"#{test_case} {ans}")