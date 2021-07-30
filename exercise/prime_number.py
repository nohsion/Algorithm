def solution(nums):
    answer = 0

    n = len(nums)
    tmp = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = nums[i] + nums[j] + nums[k]
                
                result = True
                for x in range(2, tmp):
                    if tmp % x == 0:
                        result = False
                        break
                if result:
                    answer += 1
    
    return answer
