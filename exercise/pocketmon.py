def solution(nums):
    answer = 0
    
    n = len(nums)
    m = int(len(nums)/2)
    
    picked = []

    for i in range(n):
        if nums[i] not in picked:
            picked.append(nums[i])
        if len(picked) == m:
            answer = m
            return answer
    
    answer = len(picked)        
    
    return answer
