for tc in range(1,int(input())+1):
    arr = list(input())
    cnt = 0
    stick_num = 0
    for i,v in enumerate(arr):
        if v == '(':
            stick_num += 1
        elif v == ')' and arr[i-1] == '(':
            stick_num -= 1
            cnt += stick_num
        else:
            stick_num -= 1
            cnt += 1
    print('#{} {}'.format(tc,cnt))