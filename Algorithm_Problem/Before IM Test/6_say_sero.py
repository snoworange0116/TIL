t = int(input())
for tc in range(1, t + 1):
    temp = []
    arr = [input() for i in range(5)]
    temp_arr = ''
    # print(arr)
    max_len = 0
    for i in range(5):
        if len(arr[i]) >= max_len:
            max_len = len(arr[i])

    for i in range(5):
        temp_len = len(arr[i])
        num = max_len - temp_len
        arr[i] += ' ' * num

    for i in range(max_len):
        for j in range(5):
            temp.append(arr[j][i])
    for i in temp:
        temp_arr += i
    print('#{} {}'.format(tc, temp_arr.replace('*', '', max_len * 5)))