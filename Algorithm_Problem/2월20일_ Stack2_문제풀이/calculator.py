for tc in range(1, 11):
    stack = []
    res = []
    res2 = 0
    n = int(input())
    a = input()
    isp = {'*':2,'/':2 ,'+':1 ,'-':1,'(':0}
    icp = {'*':2,'/':2, '+':1, '-':1,'(':3}
    operator = ['+', '-', '/', '*']
    for i in a:
        if i.isdecimal():
            res.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
            elif isp[stack[-1]] < icp[i]:
                stack.append(i)
            else:
                while isp[stack[-1]] >= icp[i]:
                    res.append(stack.pop())
                    if len(stack) == 0:
                        break
                stack.append(i)
    while stack:
        res.append(stack.pop())

    for i in res:
        if i.isdecimal():
            stack.append(i)
        else:
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    res2 = int(op1) + int(op2)
                elif i == '-':
                    res2 = int(op1) - int(op2)
                elif i == '*':
                    res2 = int(op1) * int(op2)
                elif i == '/':
                    res2 = int(op1) / int(op2)
                stack.append(res2)
    print('#{} {}'.format(tc,res2))