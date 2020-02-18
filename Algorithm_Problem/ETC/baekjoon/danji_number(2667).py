#백준 2667 단지번호 붙이기

n = int(input())
arr = [list(map(int,input())) for i in range(n)]
visit = [[0] * n for i in range(n)]
dx,dy = [0,0,1,-1],[1,-1,0,0]
res = []
stack = []

for i in range(n):
    for j in range(n):        
        if arr[i][j] == 1 and visit[i][j]==0: # visit[i][j] 한곳을 또 방문 안하도록 조건이 for loop를 돌때도 필요함.
            cnt = 0
            stack.append((i,j))
            while stack:
                xn,yn = stack.pop()
                visit[xn][yn] = 1
                cnt += 1
                for k in range(4):
                    x,y = xn+dx[k], yn+dy[k]
                    if 0<=x<=n-1 and 0<=y<=n-1 and arr[x][y]==1 and visit[x][y] == 0: # visit != 0 인지 == 0인지 확인
                        stack.append((x,y))
                        visit[x][y]=1     #delta를 이용해서 방문한 곳들도 visit에 넣어 주어야 함.
            res.append(cnt)
res.sort()
print(len(res))
for i in res:
    print(i)
