#sw expert tree 5178
t = int(input())
for tc in range(1,t+1):
    n,m,l = map(int,input().split()) # n은 노드개수, m은 리프노드의 개수, l은 값출력 노드 번호
    arr = {}
    tmp = 0
    for i in range(n+1):
        arr[i] = 0
    for i in range(m):
        a,b = map(int,input().split())
        arr[a] += b
    # print(arr)
    st = n
    while st != 0:
        tmp = st
        arr[tmp//2] += arr[st]
        st -= 1
    print('#{} {}'.format(tc,arr[l]))
