# https://www.acmicpc.net/problem/9093

n = int(input())
for _ in range(n):
    words = input().split()
    for w in words:
        print(w[::-1], end=' ')
