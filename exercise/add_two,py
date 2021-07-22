def solution(numbers):
    answer = []
    sum_nums = []
    
    numbers.sort()
    
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp = numbers[i] + numbers[j]
            sum_nums.append(tmp)
    
    # 리스트에서 중복 요소 제거 (new_list에 새로 저장)
    for num in sum_nums:
        if num not in answer:
            answer.append(num)
                
    answer.sort()    

    return answer
