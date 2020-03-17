import math

for tc in range(1,11):
    n = int(input())
    arr = [list((input())) for i in range(8)]
    res_cnt = 0
    upper_n = math.ceil(n/2)

    for i in range(8): # 행 탐색
        for j in range(8-n+1):
            cnt = 0
            for k in range(upper_n):
                if arr[i][j+k] == arr[i][j+n-1-k]:
                    cnt+=1
                else:
                    break
            if cnt == upper_n:
                res_cnt+=1

    for j in range(8): # 열 탐색
        for i in range(8-n+1):
            cnt = 0
            for k in range(upper_n):
                if arr[i+k][j] == arr[i+n-1-k][j]:
                    cnt+=1
                else:
                    break
            if cnt == upper_n:
                res_cnt+=1
    print('#{} {}'.format(tc,res_cnt))