brackets = list(map(str, input()))

# 내 풀이
# res = [0] * len(brackets)
# stack = []  # 여는 괄호, 닫는 괄호
# for i, x in enumerate(brackets):
#     if stack and x == ')' and stack[-1][1] == '(':
#         top = stack.pop()
#         if i == top[0] + 1:
#             for tmp in stack:
#                 res[tmp[0]] += 1
#         continue
#     stack.append((i, x))
#
# answer = sum([x + 1 for x in res if x > 0])
# print(answer)


# 모범 답안
stack = []
cnt = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        stack.pop()
        if brackets[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)