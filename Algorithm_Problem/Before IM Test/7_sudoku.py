t = int(input())
for tc in range(1, t + 1):
    arr = [list(map(int, input().split())) for i in range(9)]
    cnt = 0
    for i in range(9):  # 가로 탐색
        if sum(arr[i]) == 45 and len(arr[i]) == len(set(arr[i])):
            cnt += 1
    for j in range(len(arr[0])):  # 세로 탐색
        temp = 0
        temp_lst = []
        for i in range(len(arr)):
            temp += arr[i][j]
            temp_lst.append(arr[i][j])
        if temp == 45 and len(temp_lst) == len(set(temp_lst)):
            cnt += 1

    for i in range(0, 7, 3):  # 네모들
        for j in range(0, 7, 3):
            temp = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    temp += arr[k][l]
            if temp != 45:
                break
            else:
                cnt += 1

    if cnt == 27:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))