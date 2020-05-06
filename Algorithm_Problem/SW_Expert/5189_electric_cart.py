# sw expert advanced 완전탐색 5189

def move(cnt,st,sum_val):
    global minval
    if cnt == n:
        if sum_val < minval:
            minval = sum_val
        return
    elif cnt == n-1:
        move(cnt+1,0,sum_val + arr[st][0])
    else:
        visit[st] = 1
        for i in range(1,n):
            if visit[i] == 0:
                visit[i] = 1
                move(cnt+1,i,sum_val + arr[st][i])
                visit[i] = 0

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    visit = [0] * n
    minval = 99999999
    # print(arr)
    # print(visit)
    move(0,0,0) # 카운트,출발위치,합의 값
    print('#{} {}'.format(tc,minval))