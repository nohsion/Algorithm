def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 1
        for j in range(2, i+1):
            if i%j == 0:
                count += 1
        if count%2 != 0:
            i *= -1
        answer += i
    
    return answer
