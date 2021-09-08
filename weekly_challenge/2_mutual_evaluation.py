def solution(scores):
    answer = ''
    
    scores2 = [[0] * len(scores) for _ in range(len(scores))]
    check = []
    
    for i in range(len(scores)):
        for j in range(len(scores)):
            scores2[i][j] = scores[j][i]
    
    for i in range(len(scores2)):
        tmp = scores2[i][i]
        count = 0
        # [i][i] 값이 유일최고 or 유일 최저라면 그 점수 제외한 평균 구하기
        for j in range(len(scores2)):
            if tmp == scores2[i][j]:
                count += 1
        if count == 1 and (tmp == max(scores2[i]) or tmp == min(scores2[i])):
            print(f'{i}번 학생은 유일최고 or 유일 최저입니다.')
            check.append(True)
        else:
            check.append(False)
    
    means = []
    for i in range(len(scores2)):
        mean = 0
        if check[i]:
            mean = (sum(scores2[i]) - scores2[i][i]) / (len(scores2) - 1)
        else:
            mean = sum(scores2[i]) / len(scores2)
        means.append(mean)
    
    for mean in means:
        if mean >= 90:
            answer += 'A'
        elif mean >= 80:
            answer += 'B'
        elif mean >= 70:
            answer += 'C'
        elif mean >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer
