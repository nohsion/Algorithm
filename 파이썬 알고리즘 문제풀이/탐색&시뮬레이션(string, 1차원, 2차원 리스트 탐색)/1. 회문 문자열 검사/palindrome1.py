# [::-1] 대신 직접 코드를 구현하여 푸는 방법

import sys

sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    s = input()
    s = s.upper() # 대소문자 구분 x. lower()도 가능
    for j in range(len(s) // 2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else: # break else 구문
        print("#%d YES" % (i + 1))
