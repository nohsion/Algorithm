def is_baby(cnts, idx):
    # [1] run 체크
    if cnts[idx] >= 3:
        return True
    # [2] triplet 체크
    for i in (idx-2, idx-1, idx):
        if 0<=i<=7 and cnts[i]>0 and cnts[i+1]>0 and cnts[i+2]>0:
            return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = 12
    M = 6
    cnts1, cnts2 = [0]*10, [0]*10   # 빈도수 배열. 카드숫자 빈도수를 저장한다.
    ans = 0
    for i in range(N):
        if i%2 == 0:
            cnts1[lst[i]] += 1
            if is_baby(cnts1, lst[i]):
                ans = 1
                break
        else:
            cnts2[lst[i]] += 1
            if is_baby(cnts2, lst[i]):
                ans = 2
                break

    print(f"#{test_case} {ans}")