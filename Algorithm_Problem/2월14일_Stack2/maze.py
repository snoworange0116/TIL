def maze(arr):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    stack = [(1, 1)]
    result = 0
    while stack:
        X,Y = stack.pop()
        for i in range(4):
            x,y = X + dx[i] , Y + dy[i]
            if arr[x][y] == 0:
                stack.append((x,y))
            elif arr[x][y] == 3:
                # stack.clear()
                result = 1
                break
        arr[X][Y] = 5  #재방문 안하도록 지나온 길 값 바꾸기
    return result

for tc in range(1, 11):
    input()
    n = 16
    arr = [list(map(int, input())) for i in range(n)]
    a = maze(arr)
    print('#{} {}'.format(tc, a))

