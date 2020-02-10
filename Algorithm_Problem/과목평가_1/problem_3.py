t = int(input())
for tc in range(t):
    n = int(input())

    arr = [list(map(int,input().split())) for i in range(n)]
    min_r = 500

    for x in range(1,n-1):
        for y in range(1,n-1):
            min_tmp = 0
            max_tmp = 0
            sum_a = 0
            for i in range(x): #구역1
                for j in range(y):
                    sum_a += arr[i][j]
            sum_b = 0
            for k in range(n): #구역3
                for l in range(y,n):
                    sum_b += arr[k][l]
            sum_c = 0
            for a in range(x,n): #구역2
                for b in range(y):
                    sum_c += arr[a][b]
            min_tmp = min(sum_a, sum_b, sum_c)
            max_tmp = max(sum_a, sum_b, sum_c)
            if min_r > max_tmp - min_tmp:
                min_r = max_tmp - min_tmp

    print("#{} {}".format(tc+1,min_r))