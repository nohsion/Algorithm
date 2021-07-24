def solution(s):
    answer = ''
    
    words = ['zero', 'one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    slices = list(s)
    
    tmp_str = ''
    for i in slices:
        tmp_str += i
        print(tmp_str)
        if tmp_str in words:
            x = words.index(tmp_str)
            answer += str(x)
            tmp_str = ''
            continue
        if tmp_str in numbers:
            x = numbers.index(tmp_str)
            answer += str(x)
            tmp_str = ''
            continue
    
    return int(answer)
