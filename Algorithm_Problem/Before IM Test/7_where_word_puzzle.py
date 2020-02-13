t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    cnt = 0
    word_cnt = 0
    arr = [list(map(int, input().split())) for i in range(n)]

    for i in range(n):  # 가로 탐색
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                if j + 1 <= n - 1:
                    if cnt == k and arr[i][j + 1] == 0:
                        word_cnt += 1
                        cnt = 0
            else:
                cnt = 0
        if cnt == k:
            word_cnt += 1
            cnt = 0

    for j in range(len(arr[0])):  # 세로 탐색
        cnt = 0
        for i in range(len(arr)):
            if arr[i][j] == 1:
                cnt += 1
                if i + 1 <= n - 1:
                    if cnt == k and arr[i + 1][j] == 0:
                        word_cnt += 1
                        cnt = 0
            else:
                cnt = 0
        if cnt == k:
            word_cnt += 1
            cnt = 0

    print('#{} {}'.format(tc + 1, word_cnt))