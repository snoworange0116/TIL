t = 10
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    res = [[] for i in range(n)]
    cnt_lst = []

    for j in range(n):
        for i in range(n):
            if arr[i][j] != 0:
                res[j].append(arr[i][j])
    # print(res)

    for k in range(n):
        cnt = 0
        for l in range(len(res[k])-1): #루프 안에서 인덱스 값 확인해줄 때 어디에서 오는 인덱스인지 확인.....
            if res[k][l] == 1 and res[k][l+1] == 2:   # 새로 넣어준 res배열로 탐색해야 함
                cnt += 1
        cnt_lst.append(cnt)

    print('#{} {}'.format(tc,sum(cnt_lst)))
