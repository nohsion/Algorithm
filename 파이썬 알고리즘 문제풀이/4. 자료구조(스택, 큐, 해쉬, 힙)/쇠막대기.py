brackets = list(map(str, input()))

res = [0] * len(brackets)
stack = []  # 여는 괄호, 닫는 괄호
for i, x in enumerate(brackets):
    if stack and x == ')' and stack[-1][1] == '(':
        if i == stack[-1][0] + 1:  # 바로 전 인덱스이면, 레이저
            stack.pop()
            for tmp in stack:  # 잘린 막대기 cnt
                res[tmp[0]] += 1
        else:
            stack.pop()
    else:
        stack.append((i, x))

answer = sum([x + 1 for x in res if x > 0])
print(answer)
