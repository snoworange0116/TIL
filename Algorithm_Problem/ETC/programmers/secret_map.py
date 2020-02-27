def solution(n, arr1, arr2):
    answer = []
    aft_arr1, aft_arr2, sum_arr = [],[],[]
    for i in range(n):
        if len(bin(arr1[i])) == n+2:
            aft_arr1.append(bin(arr1[i])[2:])
        else:
            aft_arr1.append('0' * (n+2-len(bin(arr1[i]))) + bin(arr1[i])[2:])
        if len(bin(arr2[i])) == n+2:
            aft_arr2.append(bin(arr2[i])[2:])
        else:
            aft_arr2.append('0' * (n+2-len(bin(arr2[i]))) + bin(arr2[i])[2:])
        # print(aft_arr1)
        # print(aft_arr2)

    for i in range(n):
        sum_tmp = ''
        for j in range(n):
            if (aft_arr1[i])[j] == '1' or (aft_arr2[i])[j] == '1':
                sum_tmp += '#'
            else:
                sum_tmp += ' '
        answer.append(sum_tmp)
    return answer
# n=5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
n=6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))