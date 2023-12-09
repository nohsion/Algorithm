n = int(input())
words = sorted([input() for _ in range(n)])
a = sorted([input() for _ in range(n-1)])

while words:
    if not a:
        print(words.pop())
        break
    a_ = a.pop()
    w_ = words.pop()
    if a_ != w_:
        print(w_)
        break
