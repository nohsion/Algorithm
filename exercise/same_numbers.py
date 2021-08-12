def solution(arr):
    answer = []
    
    for a in arr:
        if not answer:
            answer.append(a)

        if answer:
            if a != answer[-1]:
                answer.append(a)

    return answer
