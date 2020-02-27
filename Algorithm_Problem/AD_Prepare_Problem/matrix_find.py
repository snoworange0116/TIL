t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    cnt = 0
    matrix_lst = []
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    for i in range(n):
        for j in range(n):
            r_cnt , c_cnt = 1,1
            if arr[i][j] != 0:
                st_x,st_y = i,j
                x,y = i,j #행렬의 시작점 설정
                while x+1 <= n-1 and arr[x+1][y] != 0:
                        x = x+1
                        c_cnt += 1
                while y+1 <= n-1 and arr[x][y+1] != 0:
                        y = y+1
                        r_cnt +=1
                for k in range(c_cnt): #한 구역의 행렬 값을 구한 다음 해당 값들을 0으로 바꿔주기
                    for l in range(r_cnt):
                        arr[st_x+k][st_y+l] = 0
                matrix_lst.append([c_cnt,r_cnt])
    res = ''
    matrix_lst.sort(key= lambda x: (x[0]*x[1],x[0]))
    for i in range(len(matrix_lst)):
        res += str(matrix_lst[i][0]) + ' ' + str(matrix_lst[i][1]) + ' '
    print('#{} {} {}'.format(tc,len(matrix_lst),res.rstrip()))