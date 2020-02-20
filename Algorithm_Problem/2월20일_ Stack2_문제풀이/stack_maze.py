t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int,input())) for i in range(n)]
    dx,dy = [0,0,1,-1],[1,-1,0,0]

    def maze(x,y):
        stack = [(x,y)]
        while stack:
            xn,yn = stack.pop()
            visit[xn][yn] == 1
            for k in range(4):
                xnn,ynn = xn+dx[k],yn+dy[k]
                if 0 <= xnn <= n-1 and 0 <= ynn <= n-1:
                    if arr[xnn][ynn] == 3:  #도착 값이 0이 아니므로 접근 자체를 못하기 때문에 미리 판별해줘야 함.
                        return 1
                    if visit[xnn][ynn] == 0 and arr[xnn][ynn] == 0:
                        stack.append((xnn,ynn))
                        visit[xnn][ynn] = 1
        return 0
    visit = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x = i
                y = j
    res = maze(x,y)
    print('#{} {}'.format(tc,res))
