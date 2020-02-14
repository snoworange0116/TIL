def maze(x0,y0):
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    result = 0
    stack = []
    stack.append((x0,y0))
    while stack:
        X,Y = stack.pop()
        for k in range(4):
            x, y = X+dx[k], Y+dy[k]
            if arr[x][y] == 0 and visit[x][y] == -1:
                visit[x][y] = 0
                stack.append((x,y))
            elif arr[x][y] == 3:
                result = 1
                break
    return result
for tc in range(1,11):
    input()
    n = 16
    arr = [list(map(int,input())) for i in range(n)]
    visit = [[-1] * n for i in range(n)]
    res = maze(1,1)
    print('#{} {}'.format(tc,res))