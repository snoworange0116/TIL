# sw expert 노드의 거리 5102
def BFS(st,ed,arr,visit):
    que = [[st, 0]]
    while que:
        x, cnt = que.pop(0)
        # print(x,cnt)
        visit[x] = 1
        for adj in arr[x]:
            if adj == ed:
                cnt += 1
                return cnt
            elif visit[adj] == 0:
                que.append([adj, cnt+1])
                visit[adj] = 1
    return 0
t = int(input())
for tc in range(1,t+1):
    v,e = map(int,input().split())
    nodes = [list(map(int,input().split())) for i in range(e)]
    st,ed = map(int,input().split())
    arr = [[] for i in range(v+1)]
    visit = [0] * (v+1)
    for node in nodes:
        arr[node[0]].append(node[1])
        arr[node[1]].append(node[0])
    # print(arr)
    result = BFS(st,ed,arr,visit)
    print('#{} {}'.format(tc,result))
