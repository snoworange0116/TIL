# sw expert advanced 완전탐색 5188

def move(r,c,sum):
    global minval
    sum += arr[r][c]
    if sum > minval:
        return
    if r == n-1 and c == n-1:
        if sum < minval:
            minval = sum
        return
    elif r < n-1 and c < n-1:
        move(r+1,c,sum)
        move(r,c+1,sum)
    elif c < n-1:
        move(r,c+1,sum)
    elif r < n-1:
        move(r+1,c,sum)

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    # print(arr)
    minval = 9999999
    move(0,0,0)
    print('#{} {}'.format(tc, minval))