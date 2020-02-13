t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [[1] * i for i in range(1, n + 1)]
    for i in range(1, n):
        for j in range(i + 1):
            if i >= 2 and j >= 1 and j < len(arr[i]) - 1:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print("#{}".format(tc))
    for i in range(n):
        for j in range(i + 1):
            if j == i:
                print(arr[i][j])
            else:
                print(arr[i][j], end=' ')