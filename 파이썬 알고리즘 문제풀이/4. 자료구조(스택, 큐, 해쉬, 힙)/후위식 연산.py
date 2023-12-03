# 후위 연산식이 주어지면 연산 결과를 출력하세요.
a = input()
n_stack = []
for x in a:
    if x.isdecimal():
        n_stack.append(int(x))
    else:
        if x == '+':
            n1 = n_stack.pop()
            n2 = n_stack.pop()
            n_stack.append(n2 + n1)
        elif x == '-':
            n1 = n_stack.pop()
            n2 = n_stack.pop()
            n_stack.append(n2 - n1)
        elif x == '*':
            n1 = n_stack.pop()
            n2 = n_stack.pop()
            n_stack.append(n2 * n1)
        elif x == '/':
            n1 = n_stack.pop()
            n2 = n_stack.pop()
            n_stack.append(n2 / n1)

print(n_stack[0])
