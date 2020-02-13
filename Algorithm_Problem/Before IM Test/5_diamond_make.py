t = int(input())
for t_i in range(t):
    n = input()
    flag = 'a'
    i_cnt = 0

    arr = [['.'] * (len(n) * 4 + 1) for i in range(5)]
    for i in range(1, len(n) + 1):
        arr[0][4 * i - 2] = '#'
    for i in range(1, len(n) * 4 + 1):
        if i % 2 == 1:
            arr[1][i] = '#'
    for i in range(0, len(n) * 4):
        if i % 2 == 0:
            if flag == 'a':
                arr[2][i] = '#'
                arr[2][-1] = '#'
                flag = 'b'
            elif flag == 'b':
                arr[2][i] = n[i_cnt]
                flag = 'a'
                i_cnt += 1
    for i in range(1, len(n) * 4 + 1):
        if i % 2 == 1:
            arr[3][i] = '#'
    for i in range(1, len(n) + 1):
        arr[4][4 * i - 2] = '#'
    for i in range(5):
        print("".join(arr[i]))

# print(arr)