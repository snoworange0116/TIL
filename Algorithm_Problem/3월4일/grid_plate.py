def recur(x,y,tmp,num):
    global res_lst
    tmp += str(arr[x][y])
    if num == 7:
        res_lst.append(tmp)
        return
    else:
        for k in range(4):
            xn,yn = x+dx[k], y+dy[k]
            if 0 <= xn <= 3 and 0 <= yn <= 3:
                recur(xn,yn,tmp,num+1)
        return

t = int(input())
for tc in range(1,t+1):
    arr = [list(map(int,input().split())) for i in range(4)]
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    res_lst = []
    for i in range(4):
        for j in range(4):
            num = 1
            tmp = ''
            recur(i,j,tmp,num)
    print('#{} {}'.format(tc,len(set(res_lst))))