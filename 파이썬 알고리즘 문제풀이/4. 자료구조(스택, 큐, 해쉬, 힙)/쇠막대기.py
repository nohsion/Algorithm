brackets = list(map(str, input()))

res = [0] * len(brackets)
stack = []  # 여는 괄호, 닫는 괄호
for i, x in enumerate(brackets):
    if stack and x == ')' and stack[-1][1] == '(':
        top = stack.pop()
        if i == top[0] + 1:
            for tmp in stack:
                res[tmp[0]] += 1
        continue
    stack.append((i, x))

answer = sum([x + 1 for x in res if x > 0])
print(answer)
