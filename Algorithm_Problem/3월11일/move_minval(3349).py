t = int(input())
for tc in range(1,t+1):
    w,h,n = map(int,input().split())
    result = 0
    cnt = 0
    arr = []
    for i in range(n):
        a,b = map(int,input().split())
        arr.append([a,b])
    cur = arr.pop(0)
    while arr:
        next = arr[0]
        if (cur[0]-next[0]) * (cur[1]-next[1]) < 0:
            cnt = (abs(next[0]-cur[0])+abs(next[1] - cur[1]))
            result += cnt
            cur = arr.pop(0)
        else:
            cnt = max(abs(next[0]-cur[0]),abs(next[1] - cur[1]))
            result+=cnt
            cur=arr.pop(0)
    print('#{} {}'.format(tc,result))