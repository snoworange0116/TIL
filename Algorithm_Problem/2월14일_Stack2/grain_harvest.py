t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input())) for i in range(n)]
    sum = 0
    k1,k2 = 0,0

    for i in range(n):
        if i <= n//2 :
            for j in range(n//2-k1,n//2+k1+1): #2,3 // 1,4  // 0,5
                sum += arr[i][j]
            k1 += 1
        else:
            for j in range(k2+1,n-k2-1):
                sum += arr[i][j]
            k2 += 1
    print('#{} {}'.format(tc,sum))