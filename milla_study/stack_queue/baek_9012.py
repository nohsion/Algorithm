# https://www.acmicpc.net/problem/9012

n = int(input())
for _ in range(n):
    ps = [x for x in input()]  # (())())
    stack = []
    ans = ''
    for a in ps:
        if a == '(':
            stack.append(a)
        else:  # ')'
            if stack:
                stack.pop()
            else:
                ans = 'NO'
                break
    if not ans:
        ans = 'NO' if stack else 'YES'
    print(ans)

