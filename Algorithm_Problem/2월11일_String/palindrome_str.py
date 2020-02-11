t = int(input())
for tc in range(t):
    n,m = map(int, input().split())
    arr = [list(input()) for i in range(n)]
    for i in range(n): #가로
        for j in range(n-m+1):
            temp = ''.join(arr[i])[j:j + m]
            if temp == temp[::-1] and len(temp) == m:
                print('#{} {}'.format(tc+1,temp))

    for i in range(n): #세로를 가로로
        for j in range(i,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

    for i in range(n): #가로2
        for j in range(n-m+1):
            temp = ''.join(arr[i])[j:j + m]
            if temp == temp[::-1] and len(temp) == m:
                print('#{} {}'.format(tc+1, temp))