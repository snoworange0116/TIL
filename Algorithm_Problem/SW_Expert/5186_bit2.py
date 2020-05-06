# sw expert advanced 5186 이진수2
t = int(input())
for tc in range(1,t+1):
    num = float(input())
    cnt = 0                                                            
    res = ''
    while num != 0 and cnt < 13:
        cnt += 1
        num *= 2
        if num >= 1:
            res += '1'
            num -= 1
        else:
            res += '0'
        if cnt > 12:
            res = 'overflow'
            break
        # print(res)
    print('#{} {}'.format(tc,res))