t = int(input())
for tc in range(1,t+1):
    str1 = input()
    stack = []

    for i,v in enumerate(str1):
        stack.append(v)
        if len(stack) > 1:
            if stack[-2] == v:
                stack.pop()
                stack.pop()

    print('#{} {}'.format(tc,len(stack)))
