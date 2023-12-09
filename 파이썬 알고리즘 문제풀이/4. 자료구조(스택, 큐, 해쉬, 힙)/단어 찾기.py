n = int(input())
words: dict = {}
for _ in range(n):
    words[input()] = 1
for _ in range(n-1):
    words[input()] -= 1

for k in words.keys():
    if words[k] == 1:
        print(k)
        break
