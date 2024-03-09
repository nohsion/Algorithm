# https://www.acmicpc.net/problem/9093

n = int(input())
for _ in range(n):
    words = input().split()
    for w in words:
        w = list(w)
        for i in range(len(w)-1):
            for j in range(i+1, len(w)):
                w[i], w[j] = w[j], w[i]
        print("".join(w), end=' ')
