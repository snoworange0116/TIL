t = int(input())
for tc in range(t):
    r1,c1,r2,c2 = map(int,input().split())
    q1,w1,q2,w2 = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(10)]
    arr2 = []
    sum_a = 0
    sum_b = 0
    for i in range(10):
        arr2.append([])
        for j in range(10):
            arr2[i].append(arr[i][j])

    sum_a = 0
    sum_b = 0


    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            arr[i][j] = arr[i][j] * 2
            if arr[i][j] >= 255:
                arr[i][j] = 255

    for i in range(q1,q2+1):
        for j in range(w1,w2+1):
            arr[i][j] = arr[i][j]  // 2

    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            sum_a += arr[i][j] - arr2[i][j]

    for i in range(q1,q2+1):
        for j in range(w1,w2+1):
            sum_b += arr2[i][j] - arr[i][j]

    print("#{} {}".format(tc+1,sum_a+sum_b))