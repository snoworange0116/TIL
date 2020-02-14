t = int(input()) # 테스트케이스 개수

def motion(arr):
    for i in range(n):
        for j in range(n):
            if i + 1 <= n - 1 and arr[i][j] == 0:  # 0 땡기기
                idx = 1
                while 1:
                    if i + idx <= n - 1:
                        if arr[i + idx][j] != 0:
                            arr[i][j] = arr[i + idx][j]
                            arr[i + idx][j] = 0
                            break
                        else:
                            idx += 1
                    else:
                        break
    for i in range(n):  # 2048 연산
        for j in range(n):
            if i + 1 <= n - 1:
                if arr[i][j] == arr[i + 1][j]:
                    arr[i][j] = arr[i + 1][j] * 2
                    arr[i + 1][j] = 0
                    # if i+2 <= n-1:
                    #     arr[i+1][j] = arr[i+2][j]
                    #     if i+3 <= n-1:
                    #         arr[i+2][j] = arr[i+3][j]
                    #         if i+3 <= n-1:
                    #             arr[i+3][j] = 0
    for i in range(n):
        for j in range(n):
            if i + 1 <= n - 1 and arr[i][j] == 0:  # 0 땡기기
                idx = 1
                while 1:
                    if i + idx <= n - 1:
                        if arr[i + idx][j] != 0:
                            arr[i][j] = arr[i + idx][j]
                            arr[i + idx][j] = 0
                            break
                        else:
                            idx += 1
                    else:
                        break
    return arr

def turn(arr):  # 우측으로 90도 회전 함수
    turn_arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            turn_arr[i].append(arr[n - 1 - j][i])
    return turn_arr

for tc in range(1,t+1):
    n, dir = input().split()
    n = int(n)
    arr = [list(map(int,input().split())) for i in range(n)]

    if dir == 'up':
        result = motion(arr)
    elif dir == 'right':
        result = turn(turn(turn(arr)))
        result = motion(result)
        result = turn(result)
    elif dir == 'down':
        result = turn(turn(arr))
        result = motion(result)
        result = turn(turn(result))
    elif dir == 'left':
        result = turn(arr)
        result = motion(result)
        result = turn(turn(turn(result)))
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(result[i][j],end =' ')
        print()
