def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    characters = "-_."
    for x in new_id:
        if x in characters or x.isalnum() or x.isdigit():
            answer += x
            continue
    
    # 3단계
    dot_flag = False
    tmp = ''
    for i in answer:
        if i == '.':
            if not dot_flag:
                tmp += '.'
                dot_flag = True
        else:
            tmp += i
            dot_flag = False
    answer = tmp
    
    # 4단계
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5단계
    if answer == '':
        answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        last = answer[-1]
        while len(answer) < 3:
            answer += last
    
    return answer
