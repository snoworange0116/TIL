dx,dy = [1,-1,0,0],[0,0,1,-1]
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    res = 0
    val = 0
    for i in range(n):
        for j in range(n):
            x,y = i,j
            n_x,n_y = i,j
            cnt = 1
            while True:
                for k in range(4):
                    n_x,n_y = x+dx[k], y+dy[k]
                    if 0<= n_x <n and 0<= n_y <n:
                       if arr[x][y] + 1 == arr[n_x][n_y]:
                           x = n_x
                           y = n_y
                           cnt +=1
                           break
                else:
                    break
            if cnt > res:
                res = cnt
                val = arr[i][j]
            elif cnt == res:
                val = min(val,arr[i][j])
    print('#{} {} {}'.format(tc,val,res))
