def solution(s):
    answer = ''
    
    q = int(len(s)/2)
    r = len(s)%2
    
    if r == 0:
        answer = s[q-1:q+1]
    else:
        answer = s[q:q+1]
        
    return answer
