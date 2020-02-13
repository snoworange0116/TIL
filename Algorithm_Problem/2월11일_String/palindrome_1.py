t = 10
for tc in range(t):
    n = int(input())
    arr = [list((input())) for i in range(8)]
    cnt = 0

    for i in range(8):  #가로 카운트
        for j in range(8-n+1):
            temp = ''.join(arr[i])[j:j+n]
            temp2 = temp[::-1]
            if temp == temp2:
                cnt+= 1

    for j in range(8): #세로 카운트
        for i in range(8-n+1):
            temp = ''
            for k in range(n):
                temp += arr[i+k][j]
            temp2 = temp[::-1]
            if temp == temp2:
                cnt+=1

    # for j in range(8):  진솔 세로 카운트
    #     for i in range(8-n+1):
    #         tem=[arr[k][j] for k in range(i,i+n)]
    #         print(tem)

    print('#{} {}'.format(tc+1,cnt))
