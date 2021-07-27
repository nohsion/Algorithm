def solution(n):
    answer = 0
    
    tmp = []
    while n > 0: 
        tmp.insert(0, n%3)
        n = int(n/3)
    
    x = 1
    for i in tmp:
        answer += i * x
        x *= 3
        
        
    return answer
