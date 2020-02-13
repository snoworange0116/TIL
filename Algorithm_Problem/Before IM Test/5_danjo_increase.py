t = int(input())
for t_i in range(1, t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    temp = []
    for i in range(n-1):
        for j in range(i+1,n):
            a = arr[i] * arr[j]
            len_a = len(str(a))
            cnt = 0
            for k in range(1, len_a):
                if len_a >= 2:
                    if str(a)[k] >= str(a)[k-1]:
                        cnt += 1
                    else:
                        break
                else:
                    temp.append(a)
                    break
            if cnt == len_a - 1:
                temp.append(a)
    if len(temp) == 0:
        print("#{} {}".format(t_i, -1))
    else:
        print("#{} {}".format(t_i, max(temp)))