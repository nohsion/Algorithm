def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    # 동명이인이 있을 때
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
            
    # 동명이인이 없을 때
    answer = participant[len(participant)-1]
                
            
    return answer
