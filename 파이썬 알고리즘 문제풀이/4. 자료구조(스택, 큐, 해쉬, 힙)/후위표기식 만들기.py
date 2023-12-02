# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
# 중위표기식: (3+5)*2
# 후위표기식: 35+2*
a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():  # 피연산자
        res += x
    else:  # 연산자
        if x == '(':
            stack.append(x)
        elif x in ('*', '/'):
            while stack and stack[-1] in ('*', '/'):
                res += stack.pop()
            stack.append(x)
        elif x in ('+', '-'):
            while stack and stack[-1] in ('*', '/', '+', '-'):
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()  # 여는 괄호를 빼주되, res에 추가되면 안 됨
while stack:
    res += stack.pop()
print(res)
