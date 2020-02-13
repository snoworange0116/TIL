t = int(input())
for t_i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = []
    temp = []
    for i in range(len(arr) // 2):
        arr2.append(arr[i * 2:2 * i + 2])

    temp.append(arr2[0][0])
    temp.append(arr2[0][1])

    while True:
        for j in range(n):
            if temp[-1] == arr2[j][0]:
                temp.append(arr2[j][0])
                temp.append(arr2[j][1])
            elif temp[0] == arr2[j][1]:
                temp.insert(0, arr2[j][1])
                temp.insert(0, arr2[j][0])
        if len(temp) == len(arr):
            break

    print("#{} {}".format(t_i + 1, ' '.join(map(str,temp))))