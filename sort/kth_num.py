def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        list_ = array[i-1:j]
        list_.sort()
        answer.append(list_[k-1])
        
        
    
    return answer
