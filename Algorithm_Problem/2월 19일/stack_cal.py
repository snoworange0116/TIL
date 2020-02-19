# 후위연산 stack 계산
a = input()
stack = []
for i in a:
    if i.isdecimal():
        stack.append(i)
    else:
        if len(stack) >= 2:
            op2 = stack.pop()
            op1 = stack.pop()
            if i == '+':
                res = int(op1) + int(op2)
            elif i == '-':
                res = int(op1) - int(op2)
            elif i == '*':
                res = int(op1) * int(op2)
            elif i == '/':
                res = int(op1) / int(op2)
            stack.append(res)
print(res)
