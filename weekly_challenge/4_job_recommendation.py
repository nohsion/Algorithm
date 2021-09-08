def solution(table, languages, preference):
    answer = ''
    scores = [] # SI CONTENTS HARDWARE PORTAL GAME
    scores2 = [[0] * 5 for _ in range(len(languages))]
    jobs = [] # SI CONTENTS HARDWARE PORTAL GAME
    for i in range(5):
        tmp = table[i].split(' ')
        jobs.append(tmp[0])
        
    for i in range(len(languages)):
        for j in range(len(table)):
            tmp = table[j].split(' ')
            try:
                score = 6 - tmp.index(languages[i])
                scores2[i][j] = score * preference[i]
            except:
                pass
    
    for i in range(5):
        score = 0
        for j in range(len(languages)):
            score += scores2[j][i]
        scores.append(score)
    
    max_score = -1
    max_score_index = [-1]
    for i in range(5):
        if max_score < scores[i]:
            max_score = scores[i]
            max_score_index.clear()
            max_score_index.append(i)
        elif max_score == scores[i]:
            max_score_index.append(i)
    print(max_score_index)
    
    result = []
    for i in range(len(max_score_index)):
        result.append(jobs[max_score_index[i]])
    result.sort()
    
    return result[0]
