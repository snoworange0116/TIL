for i in range(1, 11):
    count = 0
    n = int(input())
    lst = list(map(int, input().strip().split(' ')))

    for j in range(2, n - 2):
        val1 = lst[j] - lst[j - 2]
        val2 = lst[j] - lst[j - 1]
        val3 = lst[j] - lst[j + 1]
        val4 = lst[j] - lst[j + 2]
        if val1 > 0 and val2 > 0 and val3 > 0 and val4 > 0:
            count += min(val1, val2, val3, val4)

    print("#{} {}".format(i, count))