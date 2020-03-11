t = int(input())
for tc in range(1,t+1):
    str_1 = list(input())
    n = int(input())
    position = list(sorted(map(int,input().split()),reverse=True))
    for i in position:
        str_1.insert(i,'-')
    print('#{} {}'.format(tc,''.join(str_1)))