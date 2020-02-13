for t in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    min_num = 1000
    idx = 0
    for k in range(100):
        if arr[0][k] == 1:
            j = k
            cnt = 0
            i = 0
            while i != 99:
                if j - 1 >= 0 and arr[i][j - 1] == 1:
                    while j - 1 >= 0 and arr[i][j - 1] == 1:
                        j -= 1
                        cnt += 1
                elif j + 1 <= 99 and arr[i][j + 1] == 1:
                    while j + 1 <= 99 and arr[i][j + 1] == 1:
                        j += 1
                        cnt += 1
                if cnt > min_num:
                    break
                i += 1
                cnt += 1
            if min_num > cnt:
                min_num = cnt
                idx = k

    print('#{} {}'.format(t, idx))