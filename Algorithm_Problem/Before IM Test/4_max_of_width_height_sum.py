t = 10
for t_i in range(t):
    n = 100
    temp = []
    sum = 0
    test_num = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    for i in range(100):
        for j in range(100):
            sum += arr[i][j]

        temp.append(sum)
        sum = 0

    for j in range(100):
        for i in range(100):
            sum += arr[i][j]
        temp.append(sum)
        sum = 0

    for i in range(100):
        sum += arr[i][i]
    temp.append(sum)
    sum = 0

    for i in range(100):
        sum += arr[i][n - i - 1]
    temp.append(sum)

    print("#{} {}".format(t_i + 1, max(temp)))