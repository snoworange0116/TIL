import collections
from itertools import combinations
import copy

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
visit = [[0]* m for i in range(n)]  # 방문 확인 여부 리스트
dx,dy = [0,0,1,-1],[1,-1,0,0]
pollution_lst = []  # 초기 arr에서 오염 시작지 리스트
wall_lst = [] # 벽이 될 수 있는 후보 리스트
min_num = 0

q = collections.deque()
q2 = collections.deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:  #퍼져나갈 감염 근원지 리스트에 넣기
            q.append([i,j])
        if arr[i][j] == 0:
            wall_lst.append([i,j])
wall_per = list(map(list,combinations(wall_lst,3)))  # 벽을 세개씩 세우는 경우들
for i in range(len(wall_per)):
    arr2 = copy.deepcopy(arr) # 벽을 세울 때마다 오염 케이스들이 달라지므로 딥카피로 초기 리스트를 매번 복사
    q2 = copy.deepcopy(q) # q2도 pop을 하면 값이 변하게 되므로 매번 루프때마다 deep copy로 값을 초기화
    visit2 = copy.deepcopy(visit) #visit리스트도 매번 새로 초기화해주기 위해 딥카피
    res_cnt = 0
    for j in range(3):
        tt,ss = (wall_per[i][j])[0] ,(wall_per[i][j])[1]
        arr2[tt][ss] = 1
    while q2: # 큐를 사용해서 bfs로 감염근원지 주변을 전염시키며 넓혀가기
        x,y = q2.popleft()
        visit2[x][y] = 1
        arr2[x][y] = 2
        for k in range(4):
            xn, yn = x + dx[k], y + dy[k]
            if 0 <= xn <= n-1 and 0<= yn <= m-1 and visit2[xn][yn] == 0 and arr2[xn][yn] != 1:
                q2.append([xn,yn])
                visit2[xn][yn] = 1
    for ii in range(n):  # 각 케이스별로 감염안된 구역을 카운트해서 최대값과 비교하는 루프
        for jj in range(m):
            if arr2[ii][jj] == 0:
                res_cnt += 1
    if res_cnt > min_num:
        min_num = res_cnt

print(min_num)