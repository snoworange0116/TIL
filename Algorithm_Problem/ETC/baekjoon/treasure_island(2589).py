import collections
dx,dy = [0,0,1,-1],[1,-1,0,0]
n,m = map(int,input().split())
arr = [list(input()) for i in range(n)]
def island(i,j):
    q = collections.deque()
    q.append([i,j])
    visit = [[0] * m for i in range(n)]
    visit[i][j] = 1
    max_cnt = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            xn,yn = x+dx[k],y+dy[k]
            if 0 <= xn <= n-1 and 0 <= yn <= m-1:
                if arr[xn][yn] == 'L' and visit[xn][yn] == 0:
                    q.append([xn,yn])
                    visit[xn][yn] = visit[x][y] + 1
                    if visit[xn][yn] > max_cnt:
                        max_cnt = visit[xn][yn]
    return max_cnt
res_int = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            b = island(i,j)
            if b > res_int:
                res_int = b
print(res_int-1)