# https://www.acmicpc.net/problem/9012

n = int(input())
for _ in range(n):
    ps = [x for x in input()]  # (())())
    x = 0
    ans = ''
    for a in ps:
        if a == '(':
            x += 1
        else:  # ')'
            if x > 0:
                x -= 1
            else:
                ans = 'NO'
                break
    if not ans:
        ans = 'NO' if x > 0 else 'YES'
    print(ans)

