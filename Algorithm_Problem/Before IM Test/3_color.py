t = int(input())
for t_i in range(t):
    color_3 = 3
    arr = [[0] * 10 for i in range(10)]
    area = int(input())
    cnt = 0

    for z in range(area):
        r1,c1,r2,c2,color = list(map(int,input().split()))
        for i in range(c1,c2+1):
            for j in range(r1,r2+1):
                if arr[i][j] == 0:
                    arr[i][j] = color
                elif arr[i][j] != 0 and arr[i][j] != color:
                    arr[i][j] = color_3
                    cnt += 1

    print("#{} {}".format(t_i + 1, cnt))