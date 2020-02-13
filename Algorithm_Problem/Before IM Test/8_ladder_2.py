t = 10
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(100)]
    res = 0
    for j in range(100):
        if arr[0][j] == 1:
            i = 0
            temp = j
            while i != 99:
                # print(i,j)
                if 0 <= j-1  and arr[i][j-1] == 1:
                    while 0 <= j-1 and arr[i][j-1] == 1:
                        j -= 1
                elif  j+1 <= 99 and arr[i][j+1] == 1:
                    while  j+1 <= 99 and arr[i][j+1] == 1:
                        j += 1
                i += 1
            if arr[99][j] == 2:
                res = temp
    print('#{} {}'.format(tc,res))
