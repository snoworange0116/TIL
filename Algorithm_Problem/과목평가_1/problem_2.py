t = int(input())
for tc in range(t):
    r,c,n = map(int,input().split())
    arr = [[0] * c for i in range(r)]
    for k in range(n):
        r1,c1,r2,c2 = map(int,input().split())
        for i in range(r1-1,r2):
            for j in range(c1-1,c2):
                arr[i][j] += 1
    max = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] >= max:
                max = arr[i][j]
    cnt = 0
    for a in range(r):
        for b in range(c):
            if max == arr[a][b]:
                cnt += 1
    print("#{} {}".format(tc+1,cnt))