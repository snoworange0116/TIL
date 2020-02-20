t = int(input())
for tc in range(1,t+1):
    cal = input().split()
    stack = []
    for i in cal:
        if i.isdecimal():
            stack.append(i)
        elif i == '.':
            break
        else:
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    res = int(a) + int(b)
                elif i == '-':
                    res = int(a) - int(b)
                elif i == '*':
                    res = int(a) * int(b)
                elif i == '/':
                    res = int(a) // int(b)
                else:
                    res = 'error'
                    stack.append(res)
                    break
                stack.append(res)
            elif len(stack) <= 1 and (i=='+' or i=='-' or i=='/' or i=='*'):
                res = 'error'
                stack.append(res)
                break
    if len(stack) >= 2:
        res = 'error'
    print('#{} {}'.format(tc,res))