def solution(price, money, count):
    answer = -1
    
    tmp = price
    sum_price = 0
    for c in range(1, count+1):
        tmp = price * c
        sum_price += tmp
        print(tmp, sum_price)
    
    answer = sum_price - money

    if answer < 0:
        return 0

    return answer
