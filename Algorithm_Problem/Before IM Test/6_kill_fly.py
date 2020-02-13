t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = []
    max_sum = 0
    temp_sum = 0
    for i in range(n):
        arr.append(list(map(int, input().split())))
    # for k in range(n-(m-1)):
    #     for i in range(k,k+m-1):
    #         for j in range(k,k+m-1):
    #             temp_sum += arr[i][j]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            for k in range(i, i + m):
                for l in range(j, j + m):
                    temp_sum += arr[k][l]
            if temp_sum > max_sum:
                max_sum = temp_sum
                temp_sum = 0
            else:
                temp_sum = 0
    print('#{} {}'.format(tc, max_sum))