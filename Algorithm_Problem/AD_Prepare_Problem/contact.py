def BFS():
    que = [st]
    order = [[] for i in range(100)]
    visit = []
    cnt = 0
    while que:
        for i in range(len(que)):
            current = que.pop(0)
            visit.append(current)
            for neighbor in adj[current]:
                if neighbor not in visit and neighbor not in que:
                    que.append(neighbor)
                    order[cnt].append(neighbor)
        cnt+=1
    return order, visit
for tc in range(1,11):
    n, st = map(int,input().split())
    lst = list(map(int,input().split()))
    adj = []
    max_n = max(lst)
    for i in range(max_n+1):
        adj.append([])
    for i in range(0,n,2):
        adj[lst[i]].append(lst[i+1])
    # print(adj)
    order,visit = BFS()
    for i in range(99,-1,-1):
        if len(order[i]) != 0:
            idx = i
            break
    print('#{} {}'.format(tc,max(order[idx])))