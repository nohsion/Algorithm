def solution(board, moves):
    answer = 0
    
    result = []
    
    for move in moves:
        index = move - 1
        for i in range(len(board)):
            value = board[i][index]
            if value == 0:
                continue
            else:
                if result and result[-1] == value:
                    del result[-1]
                    board[i][index] = 0
                    answer += 2
                    break
                result.append(value)
                board[i][index] = 0
                break
    
    return answer
