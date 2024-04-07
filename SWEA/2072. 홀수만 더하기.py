# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sum = 0
    nums = list(map(int, input().split()))
    for n in nums:
        if n % 2 != 0:
            sum += n

    print(f"#{test_case} {sum}")
