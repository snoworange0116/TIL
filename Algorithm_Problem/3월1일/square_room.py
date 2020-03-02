def dfs(i,j):
    global max_val
    global res
    min_i,min_j = 0,0
    cnt = 0
    stack = [(i,j)]
    while stack:
        x,y = stack.pop()
        for k in range(4):
            xn,yn = x + dx[k], y + dy[k]
            if 0 <= xn <= n-1 and 0 <= yn <= n-1 and arr[xn][yn] == arr[x][y] + 1:
                stack.append([xn,yn])
                cnt += 1
    if cnt > max_val:
        max_val = cnt
        res = arr[i][j]
    elif cnt == max_val:
        res = min(res,arr[i][j])
    return res, max_val

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    max_val = -99999
    res = 0
    for i in range(n):
        for j in range(n):
            res,max_val = dfs(i,j)
    print('#{} {} {}'.format(tc,res,max_val+1))