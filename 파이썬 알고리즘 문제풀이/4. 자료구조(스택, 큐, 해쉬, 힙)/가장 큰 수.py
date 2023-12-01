n, m = map(int, input().split())

# 내 답안
a = [int(i) for i in str(n)]
stack = []
for x in a:
    if not stack or x <= stack[-1] or m == 0:
        stack.append(x)
        continue
    while x > stack[-1]:
        stack.pop()
        m -= 1
        if not stack or m == 0:
            break
    stack.append(x)

for i in range(m):
    stack.pop()
for s in stack:
    print(s, end='')

