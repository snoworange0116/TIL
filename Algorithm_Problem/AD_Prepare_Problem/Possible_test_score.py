t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    visit = [0] * (sum(arr)+1)
    result = [0]
    for i in arr:
        temp = []
        for j in result:
            if visit[i+j] == 0:
                visit[i+j] = 1
                temp.append(i+j)
        result.extend(temp)
    print('#{} {}'.format(tc,len(result)))