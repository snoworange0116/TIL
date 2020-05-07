#sw expert advanced 그리디 5202
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = []
    cnt = 0
    pop_st,pop_ed = 0,0
    flag = 0
    for i in range(n):
        st,ed = map(int,input().split())
        arr.append([st,ed])
    arr.sort(key=lambda x : x[1])
    # print(arr)
    while arr:
        # print(pop_st,pop_ed)
        if flag == 0:
            pop_st,pop_ed = arr.pop(0)
            cnt += 1
            flag = 1
        else:
            if pop_ed <= arr[0][0]:
                pop_st, pop_ed = arr.pop(0)
                cnt += 1
            else:
                arr.pop(0)
    print('#{} {}'.format(tc,cnt))