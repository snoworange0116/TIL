t = int(input())
for tc in range(1,t+1):
    v, m = map(int,input().split())
    node = [[0]*(v+1) for i in range(v+1)]
    adj_lst = [[] for i in range(v+1)]
    visit_lst = []
    stack = []
    current = 0

    for i in range(m):
        a,b = map(int,input().split())
        adj_lst[a].append(b)
    st, ed = map(int,input().split())

    stack.append(st)
    while stack:
        current = stack.pop()
        for neighbor in adj_lst[current]:
            if not neighbor in visit_lst:
                stack.append(neighbor)
        visit_lst.append(current)

    if ed in visit_lst:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,0))
