def solution(answers):
    answer = []
    
    first = [1,2,3,4,5] # 5
    second = [2,1,2,3,2,4,2,5] # 8
    third = [3,3,1,1,2,2,4,4,5,5] # 10
    
    nr_answer = [0,0,0]
    
    for i in range(len(answers)):
        f_i = i % 5
        s_i = i % 8
        t_i = i % 10
        if first[f_i] == answers[i]:
            nr_answer[0] += 1
        if second[s_i] == answers[i]:
            nr_answer[1] += 1
        if third[t_i] == answers[i]:
            nr_answer[2] += 1
    
    max = nr_answer[0]
    max_index = [1]
    for i in range(1, len(nr_answer)):
        if max < nr_answer[i]:
            max = nr_answer[i]
            max_index.clear()
            max_index.append(i+1)
        elif max == nr_answer[i]:
            max_index.append(i+1)
    
    return max_index
