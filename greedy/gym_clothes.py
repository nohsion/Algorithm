def solution(n, lost, reserve):
    answer = n - len(lost)
    new_lost = list(lost)
    new_reserve = list(reserve)
    
    for l in lost:
        for r in reserve:
            print(l, r)
            if l == r:
                new_lost.remove(l)
                new_reserve.remove(r)
                answer += 1
                break
    
    for l in new_lost:
        for r in new_reserve:
            if l-1 == r or l+1 == r:
                new_reserve.remove(r)
                answer += 1
                break

    return answer
