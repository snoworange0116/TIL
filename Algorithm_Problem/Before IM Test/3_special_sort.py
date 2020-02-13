t = int(input())
for t_i in range(t):

    n = int(input())
    arr = list(map(int,input().split()))
    temp = []
    sort_arr = sorted(arr)

    for i in range(n // 2):
            temp.append(sort_arr.pop(-1))
            temp.append(sort_arr.pop(0))
    str1 = ''
    for k in range(10):
        str1 += str(temp[k])
        str1 += ' '

    print("#{} {}".format(t_i+1, str1))