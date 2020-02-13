t = int(input())

for t_i in range(t):
    n, m = map(int, (input().split()))
    lst = list(map(int, input().split()))
    min_temp = sum(list(lst[0:m]))
    max_temp = sum(list(lst[0:m]))


    for i in range(n-m+1):
        if sum(lst[i:i+m]) <= min_temp:
            min_temp = sum(lst[i:i+m])
        if sum(lst[i:i+m]) >= max_temp:
            max_temp = sum(lst[i:i+m])

    print("#{} {}".format(t_i+1, (max_temp - min_temp)))
