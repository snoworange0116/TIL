def solution(n, arr1, arr2):
    answer = []
    tmp = ''
    aft_arr1, aft_arr2, sum_arr = [],[],[]
    for i in range(len(arr1)):
        aft_arr1.append([])
        aft_arr2.append([])
        if len(bin(arr1[i])) == 7:
            aft_arr1.append(bin(arr1[i][2:]))
        else:
            tmp = '0' + arr1[i][2:]
            aft_arr1.append(tmp)
        if len(bin(arr2[i])) == 7:
            aft_arr2.append(bin(arr2[i][2:]))
        else:
            aft_arr2.append('0' + arr2[i][2:])
        aft_arr1[i].append(bin(arr1[i]))
        aft_arr2[i].append(bin(arr2[i]))

    # for i in range(len(arr1)):
    #     sum_arr.append([])
    #     sum_arr[i].append(aft_arr1[i] | aft_arr2[i])
    return aft_arr1

n=5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))