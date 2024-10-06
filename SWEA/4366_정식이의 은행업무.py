def get_ten(lst, jinsu):
    n = len(lst)
    lst_r = lst[::-1]
    sm = 0
    for i in range(n):
        sm += int(lst_r[i])*(jinsu**i)
    return sm


def solve():
    # 2진수 자리수마다 바꿔보기
    for i2 in range(len(list(two))):
        lst2 = list(two)
        for i in range(2):
            if str(i) == lst2[i2]:
                continue
            lst2[i2] = str(i) # 1자리 바꿔본다.
            ten2 = get_ten(lst2, 2)

            # 3진수 자리수마다 바꿔보기
            for i3 in range(len(list(three))):
                lst3 = list(three)
                for i in range(3):
                    if str(i) == lst3[i3]:
                        continue
                    lst3[i3] = str(i) # 1자리 바꿔본다.
                    ten3 = get_ten(lst3, 3)
                    if ten2 == ten3:
                        return ten2


T = int(input())
for test_case in range(1, T + 1):
    two = input()   # 2진수 '1010'
    three = input() # 3진수 '212'

    ans = solve()

    print(f"#{test_case} {ans}")