# https://www.acmicpc.net/problem/11399

n = int(input())
a = list(map(int, input().split()))
tmp, result = 0, 0
for idx, x in enumerate(sorted(a)):
    # print(f"이전것({tmp}) + 현재것({x}) = {tmp + x}")
    tmp += x
    result += tmp
print(result)
