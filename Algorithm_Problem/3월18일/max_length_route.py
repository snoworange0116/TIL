# sw expert 2814 최장경로
def dfs(st,num):
    global max_cnt # 모든 재귀마다의 최대 카운트 값을 비교해 갱신해줘야하므로
    visit[st] = 1
    max_cnt = max(max_cnt,num)
    for i in range(len(arr[st])):  # 첫 스타트 노드의 인접개수만큼 반복을 돌고
        if visit[arr[st][i]] == 0:  # 해당 노드가 방문 안했다면
            dfs(arr[st][i],num+1)  # 그 노드를 시작점으로, 카운트를 1 늘려서 다시 재귀를 보냄
    visit[st] = 0  # 하단의 반복문 안의 dfs가 그 이전의 방문여부에 영향을 받지 않도록 다시 출발점을 방문 안한것으로 수정
    return max_cnt
for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr = [[] for i in range(n+1)]
    max_cnt = -999
    visit = [0] * (n+1)
    for i in range(m):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in range(1,n+1):
        res = dfs(i,1)
    print('#{} {}'.format(tc,max_cnt))
