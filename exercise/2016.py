def solution(a, b):
    answer = ''
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    kind_31 = 31%7
    kind_29 = 29%7
    kind_30 = 30%7
    # 1.1은 금요일, 2.1은 월요일,,
    sum_days_1 = kind_31
    sum_days_2 = (sum_days_1 + kind_29) % 7
    sum_days_3 = (sum_days_2 + kind_31) % 7
    sum_days_4 = (sum_days_3 + kind_30) % 7
    sum_days_5 = (sum_days_4 + kind_31) % 7
    sum_days_6 = (sum_days_5 + kind_30) % 7
    sum_days_7 = (sum_days_6 + kind_31) % 7
    sum_days_8 = (sum_days_7 + kind_31) % 7
    sum_days_9 = (sum_days_8 + kind_30) % 7
    sum_days_10 = (sum_days_9 + kind_31) % 7
    sum_days_11 = (sum_days_10 + kind_30) % 7
    # sum_days_12 = (sum_days_11 + kind_31) % 7
    
    if a == 1:
        answer = days[(b-1)%7]
    elif a == 2:
        i = (sum_days_1 + (b-1)%7) %7
        answer = days[i]
    elif a == 3:
        i = (sum_days_2 + (b-1)%7) %7
        answer = days[i]
    elif a == 4:
        i = (sum_days_3 + (b-1)%7) %7
        answer = days[i]
    elif a == 5:
        i = (sum_days_4 + (b-1)%7) %7
        answer = days[i]
    elif a == 6:
        i = (sum_days_5 + (b-1)%7) %7
        answer = days[i]
    elif a == 7:
        i = (sum_days_6 + (b-1)%7) %7
        answer = days[i]
    elif a == 8:
        i = (sum_days_7 + (b-1)%7) %7
        answer = days[i]
    elif a == 9:
        i = (sum_days_8 + (b-1)%7) %7
        answer = days[i]
    elif a == 10:
        i = (sum_days_9 + (b-1)%7) %7
        answer = days[i]
    elif a == 11:
        i = (sum_days_10 + (b-1)%7) %7
        answer = days[i]
    elif a == 12:
        i = (sum_days_11 + (b-1)%7) %7
        answer = days[i]
    
    return answer
