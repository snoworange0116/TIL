#검은색 승리 1, 흰색 승리 2
#검은돌 1, 흰돌 2

arr = [list(map(int,input().split())) for i in range(19)]
for i in range(19):
    for j in range(19):
        cnt_b = 0
        for k in range(5): #흑돌 우측 이동
            if j+k <= 18:
                if arr[i][j+k] == 1:
                    cnt_b += 1
        if j+k+1 <= 18:
            if cnt_b == 5 and arr[i][j+k+1] != 1:
                print('흑돌 승리')
                break
        cnt_w = 0
        for k in range(5): #백돌 우측 이동
            if i+k <= 18:
                if arr[i+k][j] == 2:
                    cnt_w += 1
        if i+k+1 <= 18:
            if cnt_w == 5 and arr[i+k+1][j] != 2:
                print('백돌 승리')
                break
        cnt_b = 0
        for k in range(5): #흑돌 우측 아래 이동
            if i+k <= 18 and j+k <= 18:
                if arr[i+k][j+k] == 1:
                    cnt_b += 1
        if i+k+1 <= 18 and j+k+1 <= 18:
            if cnt_b == 5 and arr[i+k+1][i+k+1] != 1:
                print('흑돌 승리')
                break
        cnt_w = 0
        for k in range(5): #백돌 우측 아래 이동
            if i+k <= 18 and j+k <= 18:
                if arr[i+k][j+k] == 2:
                    cnt_b += 1
        if i+k+1 <= 18 and j+k+1 <= 18:
            if cnt_b == 5 and arr[i+k+1][i+k+1] != 2:
                print('백돌 승리')
                break
        cnt_b = 0
        for k in range(5): #흑돌 아래 이동
            if i+k <= 18:
                if arr[i+k][j] == 1:
                    cnt_b+= 1
        if i+k+1<= 18:
            if cnt_b == 5 and arr[i+k+1][j] != 1:
                print('흑돌 승리')
                break
        cnt_w = 0
        for k in range(5): #백돌 아래 이동
            if i+k <= 18:
                if arr[i+k][j] == 2:
                    cnt_b+= 1
        if i+k+1 <= 18:
            if cnt_b == 5 and arr[i+k+1][j] != 2:
                print('백돌 승리')
                break
        cnt_b = 0
        for k in range(5): #흑돌 좌측 아래 이동
            if i+k <= 18 and j-k >= 0:
                if arr[i+k][j-k] == 1:
                    cnt_b+= 1
        if i+k+1 <= 18 and j-k-1 >= 0:
            if cnt_b == 5 and arr[i+k+1][j-k-1] != 1:
                print('흑돌 승리')
                break
        cnt_w = 0
        for k in range(5): #백돌 좌측 아래 이동
            if i+k <= 18 and j-k >= 0:
                if arr[i + k][j - k] == 2:
                    cnt_b += 1
        if i+k+1 <= 18 and j-k-1 >= 0:
            if cnt_b == 5 and arr[i + k + 1][j - k - 1] != 2:
                print('백돌 승리')
                break

