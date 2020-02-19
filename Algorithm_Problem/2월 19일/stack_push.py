# 중위연산 후위연산으로 변환(괄호 제외)

stack = []
temp_stack = []
res = []
a = input()
priority = {'*':5 ,'/':5 ,'+':4 ,'-':4}
operator = ['+' , '-' , '/' , '*']
for i in a:
    if i.isdecimal():
        res.append(i)
    else:
        if len(stack) == 0:
            stack.append(i)
        elif priority[stack[-1]] < priority[i]:
            stack.append(i)
        else:
            while priority[stack[-1]] >= priority[i]:
                res.append(stack.pop())
                if len(stack) == 0:
                    break
            stack.append(i)
while stack:
    res.append(stack.pop())

print(res)