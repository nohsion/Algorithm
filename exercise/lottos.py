def lotto_rank(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count == 4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else:
        return 6

    
def solution(lottos, win_nums):
    answer = []
    
    zero_count = 0
    count = 0
    for i in range(6):
        if lottos[i] == 0:
            zero_count += 1
        for j in range(6):
            if lottos[i] == win_nums[j]:
                count += 1
                
    max_count = count + zero_count
    
    answer.append(lotto_rank(max_count))
    answer.append(lotto_rank(count))
    
    return answer
