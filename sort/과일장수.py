# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    answer = 0
    for idx, s in enumerate(sorted(score, reverse=True)):
        if idx % m == m-1:
            answer += (m * s)
    return answer
