def binary_num(num, n):
    result = ''
    for i in range(n):
        result = str(num % 2) + result
        num = int(num / 2)
    
    return result


def solution(n, arr1, arr2):
    answer = []
    arr = []
    bin_arr = []
    
    # OR arr1, arr2 
    for i in range(n):
        tmp = arr1[i] | arr2[i]
        arr.append(tmp)
        bin_arr.append(binary_num(arr[i], n))
    
    for bin in bin_arr:
        tmp = ''
        for b in bin:
            if b == '0':
                tmp += ' '
            if b == '1':
                tmp += '#'
        answer.append(tmp)
    
    return answer
