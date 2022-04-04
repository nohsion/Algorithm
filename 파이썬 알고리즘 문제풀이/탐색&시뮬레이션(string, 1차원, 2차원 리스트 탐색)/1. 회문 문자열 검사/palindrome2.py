# 파이썬다운 풀이

import sys

sys.stdin = open("input.txt", "r")
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))