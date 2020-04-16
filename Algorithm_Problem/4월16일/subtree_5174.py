# sw expert tree 5174

def find_subtree(root):
    global cnt
    if tree[root]:
        while tree[root]:
            cnt += 1
            a = tree[root].pop(0)
            find_subtree(a)

t = int(input())
for tc in range(1,t+1):
    e, n = map(int, input().split()) # 간선 개수 e, 루트노드 n
    arr = list(map(int,input().split()))
    tree = []
    cnt = 0
    for i in range(e+2):
        tree.append([])
    for i in range(e):
        b = arr.pop()
        a = arr.pop()
        tree[a].append(b)
    # print(tree)
    find_subtree(n)
    print('#{} {}'.format(tc, cnt+1))
