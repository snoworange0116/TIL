t = 10
for t_i in range(t):
    tc = int(input())
    max_pal_len = 0
    arr = [list(input()) for i in range(100)]

    for i in range(100):  #가로 탐색
        for j in range(100):
            temp = ''
            for k in range(2,101):
                if j+k <= 101:
                    temp = arr[i][j:j+k]
                    temp2 = temp[::-1]
                    if temp == temp2:
                        temp_num = len(temp)
                        if temp_num > max_pal_len:
                            max_pal_len = temp_num
                            break

    for i in range(100):
        for j in range(i,100):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(100):  #세로를 가로로 바꿔 탐색
        for j in range(100):
            temp = ''
            for k in range(2,101):
                if j+k <= 101:
                    temp = arr[i][j:j+k]
                    temp2 = temp[::-1]
                    if temp == temp2:
                        temp_num = len(temp)
                        if temp_num > max_pal_len:
                            max_pal_len = temp_num
                            break
    print('#{} {}'.format(tc,max_pal_len))