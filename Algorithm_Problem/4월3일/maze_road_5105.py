# sw expert que 미로의 거리
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for i in range(n)]
    dx,dy = [0,0,1,-1], [1,-1,0,0]
    que = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                que.append([i,j])
                arr[i][j] = 0
                break
    res_cnt = 0
    while que:
        x,y = que.pop(0)
        cnt = arr[x][y] + 1 # pop했을 때 이전의 방문 위치 값 보다 +1씩 증가시켜준 값을 cnt에 설정
        for k in range(4):
            xn,yn = x + dx[k], y + dy[k]
            if 0 <= xn < n and 0 <= yn < n :
                if arr[xn][yn] == '0':
                    que.append([xn,yn])
                    arr[xn][yn] = cnt # 방문 예정인 위치 값에 cnt를 미리 할당해 줌!
                elif arr[xn][yn] == '3':
                    res_cnt = cnt - 1
                    break
    print('#{} {}'.format(tc,res_cnt))