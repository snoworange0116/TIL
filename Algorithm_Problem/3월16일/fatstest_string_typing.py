t = int(input())
for tc in range(1,t+1):
    a,b = input().split()
    cnt = 0
    st = 0
    while st<= len(a) - len(b):
        if a[st:st+len(b)] == b:
            st += len(b)
            cnt+=1
        else:
            st +=1
    print('#{} {}'.format(tc,len(a)-cnt*len(b)+cnt))